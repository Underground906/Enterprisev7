/**
 * AI Vision Screen Identifier using Gemini Flash
 * Usage: node scripts/identify-screens-gemini.js [screens_dir] [output_file]
 *
 * Sends each PNG to Gemini 2.0 Flash for component identification.
 * Cost: ~$0.02 for 48 screens (practically free)
 *
 * Setup:
 *   1. Get free API key from https://aistudio.google.com/apikey
 *   2. Set env: GEMINI_API_KEY=your_key_here
 *   3. Run: node scripts/identify-screens-gemini.js
 *
 * Checkpoints after every screen. Resume-safe.
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

// Config
const DEFAULT_SCREENS_DIR = path.join(__dirname, '..', 'public', 'figma-exports');
const API_BASE = 'generativelanguage.googleapis.com';
const MODEL = 'gemini-2.0-flash';
const MAX_RETRIES = 3;
const DELAY_BETWEEN_REQUESTS_MS = 500; // stay under rate limits

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

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function readImageAsBase64(filePath) {
  const buffer = fs.readFileSync(filePath);
  return buffer.toString('base64');
}

function callGeminiAPI(apiKey, imageBase64, filename) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      contents: [{
        parts: [
          {
            text: IDENTIFICATION_PROMPT + `\n\nFilename: ${filename}`
          },
          {
            inline_data: {
              mime_type: 'image/png',
              data: imageBase64
            }
          }
        ]
      }],
      generationConfig: {
        temperature: 0.1,
        maxOutputTokens: 8192,
        responseMimeType: 'application/json'
      }
    });

    const options = {
      hostname: API_BASE,
      path: `/v1beta/models/${MODEL}:generateContent?key=${apiKey}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body)
      },
      timeout: 60000
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (parsed.error) {
            reject(new Error(`Gemini API error: ${parsed.error.message}`));
            return;
          }
          const text = parsed.candidates?.[0]?.content?.parts?.[0]?.text;
          if (!text) {
            reject(new Error('No text in Gemini response'));
            return;
          }
          // Parse the JSON response
          const cleaned = text.replace(/```json\n?/g, '').replace(/```\n?/g, '').trim();
          const result = JSON.parse(cleaned);
          resolve(result);
        } catch (e) {
          reject(new Error(`Parse error: ${e.message}\nRaw: ${data.substring(0, 500)}`));
        }
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
  const imageBase64 = readImageAsBase64(filePath);

  try {
    const result = await callGeminiAPI(apiKey, imageBase64, filename);
    result.screen_slug = result.screen_slug || filename;
    return result;
  } catch (err) {
    if (retries < MAX_RETRIES) {
      console.log(`  Retry ${retries + 1}/${MAX_RETRIES} for ${filename}: ${err.message}`);
      await sleep(2000 * (retries + 1)); // exponential backoff
      return processScreen(apiKey, filePath, retries + 1);
    }
    console.error(`  FAILED: ${filename}: ${err.message}`);
    return {
      screen_slug: filename,
      error: err.message,
      screen_type: 'unknown',
      components: []
    };
  }
}

async function main() {
  const apiKey = process.env.GEMINI_API_KEY || 'AIzaSyBKdZ6OMS5kxPoMigdrk8BJCaEfHoFx4kE';
  if (!apiKey) {
    console.error('ERROR: Set GEMINI_API_KEY environment variable');
    console.error('Get a free key at: https://aistudio.google.com/apikey');
    process.exit(1);
  }

  // Find screens directory
  let screensDir = process.argv[2];
  let outputFile = process.argv[3];

  if (!screensDir) {
    // Auto-detect: find the first figma export with screens
    const exportsDir = DEFAULT_SCREENS_DIR;
    if (fs.existsSync(exportsDir)) {
      const subdirs = fs.readdirSync(exportsDir);
      for (const sub of subdirs) {
        const candidate = path.join(exportsDir, sub, 'screens');
        if (fs.existsSync(candidate)) {
          screensDir = candidate;
          outputFile = outputFile || path.join(exportsDir, sub, 'component_inventory.json');
          break;
        }
      }
    }
  }

  if (!screensDir || !fs.existsSync(screensDir)) {
    console.error('ERROR: Screens directory not found');
    console.error('Usage: node scripts/identify-screens-gemini.js [screens_dir] [output_file]');
    process.exit(1);
  }

  outputFile = outputFile || path.join(path.dirname(screensDir), 'component_inventory.json');
  const checkpointFile = outputFile + '.checkpoint';

  console.log('\n=== GEMINI VISION SCREEN IDENTIFIER ===');
  console.log(`Screens: ${screensDir}`);
  console.log(`Output: ${outputFile}`);
  console.log(`Model: ${MODEL}`);

  // Get all PNGs
  const allFiles = fs.readdirSync(screensDir)
    .filter(f => f.endsWith('.png'))
    .sort();

  console.log(`\nTotal screens found: ${allFiles.length}`);

  // Load checkpoint if exists
  let results = [];
  let processed = new Set();
  if (fs.existsSync(checkpointFile)) {
    try {
      const checkpoint = JSON.parse(fs.readFileSync(checkpointFile, 'utf8'));
      results = checkpoint.results || [];
      processed = new Set(results.map(r => r.screen_slug));
      console.log(`Resuming from checkpoint: ${processed.size}/${allFiles.length} already done`);
    } catch (e) {
      console.log('Checkpoint corrupt, starting fresh');
    }
  }

  const remaining = allFiles.filter(f => !processed.has(path.basename(f, '.png')));
  console.log(`Screens to process: ${remaining.length}\n`);

  let successCount = processed.size;
  let failCount = 0;

  for (let i = 0; i < remaining.length; i++) {
    const file = remaining[i];
    const filePath = path.join(screensDir, file);
    const slug = path.basename(file, '.png');

    process.stdout.write(`[${successCount + failCount + 1}/${allFiles.length}] ${slug}... `);

    const result = await processScreen(apiKey, filePath);

    if (result.error) {
      failCount++;
      console.log(`FAILED (${result.error})`);
    } else {
      successCount++;
      const compCount = result.components?.length || 0;
      console.log(`OK (${compCount} components)`);
    }

    results.push(result);

    // Checkpoint after EVERY screen
    fs.writeFileSync(checkpointFile, JSON.stringify({
      results,
      last_processed: slug,
      timestamp: new Date().toISOString(),
      progress: `${successCount + failCount}/${allFiles.length}`
    }, null, 2));

    // Rate limit delay
    if (i < remaining.length - 1) {
      await sleep(DELAY_BETWEEN_REQUESTS_MS);
    }
  }

  // Generate summary
  const summary = {
    kit_name: 'Brainwave 2.0',
    generated_at: new Date().toISOString(),
    model_used: MODEL,
    total_screens: allFiles.length,
    successful: successCount,
    failed: failCount,
    component_types: {},
    reuse_categories: {},
    layout_types: {},
    screens: results
  };

  // Aggregate stats
  for (const screen of results) {
    if (screen.components) {
      for (const comp of screen.components) {
        summary.component_types[comp.type] = (summary.component_types[comp.type] || 0) + 1;
        if (comp.reuse_category) {
          summary.reuse_categories[comp.reuse_category] = (summary.reuse_categories[comp.reuse_category] || 0) + 1;
        }
      }
    }
    if (screen.layout?.type) {
      summary.layout_types[screen.layout.type] = (summary.layout_types[screen.layout.type] || 0) + 1;
    }
  }

  // Write final output
  fs.writeFileSync(outputFile, JSON.stringify(summary, null, 2));

  // Clean up checkpoint
  if (fs.existsSync(checkpointFile)) {
    fs.unlinkSync(checkpointFile);
  }

  console.log('\n=== IDENTIFICATION COMPLETE ===');
  console.log(`Screens: ${successCount}/${allFiles.length} successful`);
  console.log(`Output: ${outputFile}`);
  console.log(`\nComponent type breakdown:`);
  const sorted = Object.entries(summary.component_types).sort((a, b) => b[1] - a[1]);
  for (const [type, count] of sorted.slice(0, 15)) {
    console.log(`  ${type}: ${count}`);
  }
  console.log(`\nLayout types:`);
  for (const [type, count] of Object.entries(summary.layout_types)) {
    console.log(`  ${type}: ${count}`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});
