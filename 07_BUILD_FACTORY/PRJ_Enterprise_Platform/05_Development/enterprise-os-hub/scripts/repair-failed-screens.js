/**
 * Repair failed screen identifications
 * Scans all component_inventory.json files, finds screens with errors,
 * re-runs Groq vision on just those screens, and patches the results back in.
 *
 * Usage: GROQ_API_KEY=xxx node scripts/repair-failed-screens.js
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const EXPORTS_DIR = path.join(__dirname, '..', 'public', 'figma-exports');
const API_HOST = 'api.groq.com';
const MODEL = 'meta-llama/llama-4-maverick-17b-128e-instruct';
const CONCURRENCY = 10;

const IDENTIFICATION_PROMPT = `You are a UI component identification system. Analyze this screen from a Figma UI kit and return a JSON object with this EXACT structure:

{
  "screen_slug": "filename without extension",
  "screen_name": "Human readable name",
  "screen_type": "full_page | modal | overlay | state_variant",
  "is_variant_of": null,
  "layout": {
    "type": "sidebar_content | split | centered | full_canvas | grid",
    "has_sidebar": true/false,
    "sidebar_style": "expanded | collapsed | none",
    "has_topbar": true/false,
    "has_footer": true/false
  },
  "components": [
    {
      "type": "sidebar | topbar | card | button | input | modal | dropdown | avatar | search_bar | breadcrumb | tabs | toggle | badge | notification | pricing_card | form | table | grid | image | icon | tooltip | menu | dialog | checkbox | radio | select | textarea | progress | pagination | tag | chip | divider | accordion",
      "name": "descriptive name",
      "location": "left | right | top | center | bottom | overlay",
      "approximate_dimensions": "WxH or description",
      "details": "visual details - colors, text, icons, borders, shadows",
      "reusable": true/false,
      "reuse_category": "navigation | data_display | input | feedback | layout | action | overlay"
    }
  ],
  "color_palette": ["#hex1", "#hex2"],
  "typography_notes": "font observations",
  "primary_purpose": "what this screen is for",
  "enterprise_os_potential": "how this layout could be reused"
}

Be thorough - identify EVERY visible component including small elements like badges, dividers, icons.
Return ONLY valid JSON, no markdown fences, no extra text.`;

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function callGroqAPI(apiKey, imageBase64, filename) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      model: MODEL,
      messages: [{ role: 'user', content: [
        { type: 'text', text: IDENTIFICATION_PROMPT + `\n\nFilename: ${filename}` },
        { type: 'image_url', image_url: { url: `data:image/png;base64,${imageBase64}` } }
      ]}],
      temperature: 0.1,
      max_tokens: 8192,
      response_format: { type: 'json_object' }
    });

    const options = {
      hostname: API_HOST, path: '/openai/v1/chat/completions', method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${apiKey}`, 'Content-Length': Buffer.byteLength(body) },
      timeout: 90000
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (parsed.error) { reject(new Error(parsed.error.message || JSON.stringify(parsed.error))); return; }
          const text = parsed.choices?.[0]?.message?.content;
          if (!text) { reject(new Error('No content in response')); return; }
          const cleaned = text.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
          resolve(JSON.parse(cleaned));
        } catch (e) { reject(new Error(`Parse error: ${e.message}`)); }
      });
    });
    req.on('error', reject);
    req.on('timeout', () => { req.destroy(); reject(new Error('Request timeout')); });
    req.write(body);
    req.end();
  });
}

async function processScreen(apiKey, filePath, retries = 0) {
  const filename = path.basename(filePath, '.png');
  const imageBase64 = fs.readFileSync(filePath).toString('base64');
  const sizeKB = Math.round(imageBase64.length * 0.75 / 1024);

  // Skip images that are too large or have extreme aspect ratios
  if (sizeKB > 15000) {
    return { screen_slug: filename, error: 'Image too large to process', screen_type: 'unknown', components: [] };
  }

  try {
    const result = await callGroqAPI(apiKey, imageBase64, filename);
    result.screen_slug = result.screen_slug || filename;
    return result;
  } catch (err) {
    if (retries < 3) {
      await sleep(3000 * (retries + 1));
      return processScreen(apiKey, filePath, retries + 1);
    }
    return { screen_slug: filename, error: err.message, screen_type: 'unknown', components: [] };
  }
}

async function main() {
  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) { console.error('ERROR: Set GROQ_API_KEY'); process.exit(1); }

  // Find all kits with failed screens
  const kitDirs = fs.readdirSync(EXPORTS_DIR).filter(d =>
    fs.statSync(path.join(EXPORTS_DIR, d)).isDirectory()
  );

  let totalRepairs = 0;
  let totalFixed = 0;
  let totalStillFailed = 0;

  for (const kitDir of kitDirs) {
    const invPath = path.join(EXPORTS_DIR, kitDir, 'component_inventory.json');
    const screensDir = path.join(EXPORTS_DIR, kitDir, 'screens');
    if (!fs.existsSync(invPath) || !fs.existsSync(screensDir)) continue;

    const inventory = JSON.parse(fs.readFileSync(invPath, 'utf8'));
    const failedScreens = inventory.screens.filter(s => s.error);
    if (failedScreens.length === 0) continue;

    console.log(`\n=== ${kitDir} : ${failedScreens.length} failed screens to repair ===`);

    // Process failed screens in concurrent batches
    for (let i = 0; i < failedScreens.length; i += CONCURRENCY) {
      const batch = failedScreens.slice(i, i + CONCURRENCY);
      const promises = batch.map(async (screen) => {
        const pngPath = path.join(screensDir, screen.screen_slug + '.png');
        if (!fs.existsSync(pngPath)) {
          console.log(`  SKIP ${screen.screen_slug} (PNG not found)`);
          return null;
        }
        process.stdout.write(`  ${screen.screen_slug}... `);
        totalRepairs++;
        const result = await processScreen(apiKey, pngPath);
        if (result.error) {
          console.log(`STILL FAILED (${result.error})`);
          totalStillFailed++;
        } else {
          console.log(`FIXED (${result.components?.length || 0} components)`);
          totalFixed++;
        }
        return { slug: screen.screen_slug, result };
      });

      const results = await Promise.all(promises);

      // Patch results back into inventory
      for (const r of results) {
        if (!r) continue;
        const idx = inventory.screens.findIndex(s => s.screen_slug === r.slug);
        if (idx !== -1) {
          inventory.screens[idx] = r.result;
        }
      }

      if (i + CONCURRENCY < failedScreens.length) await sleep(200);
    }

    // Recalculate stats
    inventory.successful = inventory.screens.filter(s => !s.error).length;
    inventory.failed = inventory.screens.filter(s => s.error).length;
    inventory.component_types = {};
    inventory.reuse_categories = {};
    inventory.layout_types = {};
    for (const screen of inventory.screens) {
      if (screen.components) {
        for (const comp of screen.components) {
          inventory.component_types[comp.type] = (inventory.component_types[comp.type] || 0) + 1;
          if (comp.reuse_category) {
            inventory.reuse_categories[comp.reuse_category] = (inventory.reuse_categories[comp.reuse_category] || 0) + 1;
          }
        }
      }
      if (screen.layout?.type) {
        inventory.layout_types[screen.layout.type] = (inventory.layout_types[screen.layout.type] || 0) + 1;
      }
    }
    inventory.repaired_at = new Date().toISOString();

    fs.writeFileSync(invPath, JSON.stringify(inventory, null, 2));
    console.log(`  Saved. Now ${inventory.successful}/${inventory.total_screens} successful.`);
  }

  console.log('\n========================================');
  console.log('  REPAIR COMPLETE');
  console.log('========================================');
  console.log(`Attempted: ${totalRepairs}`);
  console.log(`Fixed: ${totalFixed}`);
  console.log(`Still failed: ${totalStillFailed}`);
}

main().catch(err => { console.error('Fatal:', err.message); process.exit(1); });
