/**
 * AI Vision Screen Identifier using Groq (Llama Vision)
 * Drop-in replacement for identify-screens-gemini.js
 *
 * Usage: node scripts/identify-screens-groq.js [screens_dir] [output_file]
 *
 * Setup:
 *   1. Get free API key from https://console.groq.com/keys
 *   2. Set env: GROQ_API_KEY=your_key_here
 *   3. Run: node scripts/identify-screens-groq.js
 *
 * Checkpoints after every screen. Resume-safe.
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

// Config
const DEFAULT_SCREENS_DIR = path.join(__dirname, '..', 'public', 'figma-exports');
const API_HOST = 'api.groq.com';
const MODEL = 'meta-llama/llama-4-maverick-17b-128e-instruct';
const MAX_RETRIES = 3;
const CONCURRENCY = 10; // parallel requests - paid tier supports 300k TPM
const DELAY_BETWEEN_BATCHES_MS = 200;

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

// Downscale large images to stay under Groq limits
// Groq vision has token limits on images - smaller images = fewer tokens
function getImageSize(filePath) {
  const stats = fs.statSync(filePath);
  return stats.size;
}

function callGroqAPI(apiKey, imageBase64, filename) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({
      model: MODEL,
      messages: [{
        role: 'user',
        content: [
          {
            type: 'text',
            text: IDENTIFICATION_PROMPT + `\n\nFilename: ${filename}`
          },
          {
            type: 'image_url',
            image_url: {
              url: `data:image/png;base64,${imageBase64}`
            }
          }
        ]
      }],
      temperature: 0.1,
      max_tokens: 8192,
      response_format: { type: 'json_object' }
    });

    const options = {
      hostname: API_HOST,
      path: '/openai/v1/chat/completions',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
        'Content-Length': Buffer.byteLength(body)
      },
      timeout: 90000
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (parsed.error) {
            const errMsg = parsed.error.message || JSON.stringify(parsed.error);
            // Check for rate limit
            if (res.statusCode === 429) {
              const retryAfter = res.headers['retry-after'] || '30';
              reject(new Error(`RATE_LIMIT:${retryAfter}:${errMsg}`));
              return;
            }
            reject(new Error(`Groq API error: ${errMsg}`));
            return;
          }
          const text = parsed.choices?.[0]?.message?.content;
          if (!text) {
            reject(new Error(`No content in Groq response. Raw: ${data.substring(0, 300)}`));
            return;
          }
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

  // Warn if image is very large (>5MB base64 could be slow)
  const sizeKB = Math.round(imageBase64.length * 0.75 / 1024);
  if (sizeKB > 5000 && retries === 0) {
    console.log(`  [${sizeKB}KB image - may be slow] `);
  }

  try {
    const result = await callGroqAPI(apiKey, imageBase64, filename);
    result.screen_slug = result.screen_slug || filename;
    return result;
  } catch (err) {
    // Handle rate limits with longer backoff
    if (err.message.startsWith('RATE_LIMIT:') && retries < MAX_RETRIES) {
      const parts = err.message.split(':');
      const waitSec = parseInt(parts[1]) || 30;
      console.log(`  Rate limited - waiting ${waitSec}s...`);
      await sleep(waitSec * 1000);
      return processScreen(apiKey, filePath, retries + 1);
    }
    if (retries < MAX_RETRIES) {
      console.log(`  Retry ${retries + 1}/${MAX_RETRIES} for ${filename}: ${err.message}`);
      await sleep(3000 * (retries + 1));
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
  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    console.error('ERROR: Set GROQ_API_KEY environment variable');
    console.error('Get a free key at: https://console.groq.com/keys');
    process.exit(1);
  }

  let screensDir = process.argv[2];
  let outputFile = process.argv[3];

  if (!screensDir) {
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
    console.error('Usage: node scripts/identify-screens-groq.js [screens_dir] [output_file]');
    process.exit(1);
  }

  outputFile = outputFile || path.join(path.dirname(screensDir), 'component_inventory.json');
  const checkpointFile = outputFile + '.checkpoint';

  console.log('\n=== GROQ VISION SCREEN IDENTIFIER ===');
  console.log(`Screens: ${screensDir}`);
  console.log(`Output: ${outputFile}`);
  console.log(`Model: ${MODEL}`);

  const allFiles = fs.readdirSync(screensDir)
    .filter(f => f.endsWith('.png'))
    .sort();

  console.log(`\nTotal screens found: ${allFiles.length}`);

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

  // Process in concurrent batches
  for (let i = 0; i < remaining.length; i += CONCURRENCY) {
    const batch = remaining.slice(i, i + CONCURRENCY);
    const promises = batch.map(async (file) => {
      const filePath = path.join(screensDir, file);
      const slug = path.basename(file, '.png');
      const idx = successCount + failCount + batch.indexOf(file) + 1;
      process.stdout.write(`[${idx}/${allFiles.length}] ${slug}... `);
      const result = await processScreen(apiKey, filePath);
      if (result.error) {
        console.log(`FAILED (${result.error})`);
      } else {
        const compCount = result.components?.length || 0;
        console.log(`OK (${compCount} components)`);
      }
      return { slug, result };
    });

    const batchResults = await Promise.all(promises);

    for (const { slug, result } of batchResults) {
      if (result.error) {
        failCount++;
      } else {
        successCount++;
      }
      results.push(result);
    }

    // Checkpoint after every batch
    fs.writeFileSync(checkpointFile, JSON.stringify({
      results,
      last_processed: batchResults[batchResults.length - 1].slug,
      timestamp: new Date().toISOString(),
      progress: `${successCount + failCount}/${allFiles.length}`
    }, null, 2));

    if (i + CONCURRENCY < remaining.length) {
      await sleep(DELAY_BETWEEN_BATCHES_MS);
    }
  }

  const summary = {
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

  fs.writeFileSync(outputFile, JSON.stringify(summary, null, 2));

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
