/**
 * Batch Export & Identify ALL 38 UI Kits
 *
 * Usage:
 *   node scripts/batch-export-all-kits.js                    # Export + Identify all
 *   node scripts/batch-export-all-kits.js --export-only       # Just export PNGs
 *   node scripts/batch-export-all-kits.js --identify-only     # Just run Groq vision (PNGs must exist)
 *   node scripts/batch-export-all-kits.js --skip "Brainwave"  # Skip already-done kits
 *
 * Requirements:
 *   - Figma token in export script (already set)
 *   - GROQ_API_KEY env var for identification (free from console.groq.com)
 *
 * Progress is saved to batch_progress.json. Resume-safe.
 */

const { execSync, spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const SCRIPTS_DIR = __dirname;
const ROOT_DIR = path.join(SCRIPTS_DIR, '..');
const KIT_INDEX_PATH = path.resolve(ROOT_DIR, '../../../PRJ_UI_Component_Library/03_Design/KIT_INDEX.json');
const EXPORTS_DIR = path.join(ROOT_DIR, 'public', 'figma-exports');
const PROGRESS_FILE = path.join(EXPORTS_DIR, 'batch_progress.json');

function loadProgress() {
  if (fs.existsSync(PROGRESS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(PROGRESS_FILE, 'utf8'));
    } catch (e) {
      console.log('Progress file corrupt, starting fresh');
    }
  }
  return { exported: {}, identified: {}, started_at: new Date().toISOString() };
}

function saveProgress(progress) {
  progress.last_updated = new Date().toISOString();
  fs.writeFileSync(PROGRESS_FILE, JSON.stringify(progress, null, 2));
}

function runScript(scriptPath, args = []) {
  return new Promise((resolve, reject) => {
    const proc = spawn('node', [scriptPath, ...args], {
      stdio: 'inherit',
      cwd: ROOT_DIR
    });
    proc.on('close', code => {
      if (code === 0) resolve();
      else reject(new Error(`Script exited with code ${code}`));
    });
    proc.on('error', reject);
  });
}

async function main() {
  const args = process.argv.slice(2);
  const exportOnly = args.includes('--export-only');
  const identifyOnly = args.includes('--identify-only');
  const skipIdx = args.indexOf('--skip');
  const skipKits = new Set();
  if (skipIdx !== -1) {
    // Collect all kit names after --skip until next flag
    for (let i = skipIdx + 1; i < args.length; i++) {
      if (args[i].startsWith('--')) break;
      skipKits.add(args[i]);
    }
  }

  // Always skip Brainwave (already done)
  skipKits.add('Brainwave 2.0');

  // Load kit index
  if (!fs.existsSync(KIT_INDEX_PATH)) {
    console.error('ERROR: KIT_INDEX.json not found at', KIT_INDEX_PATH);
    process.exit(1);
  }
  const kitIndex = JSON.parse(fs.readFileSync(KIT_INDEX_PATH, 'utf8'));
  const kits = Object.entries(kitIndex)
    .map(([name, data]) => ({ name, file_key: data.file_key, items: data.total_items }))
    .filter(k => !skipKits.has(k.name));

  console.log('\n========================================');
  console.log('  BATCH KIT EXPORT & IDENTIFY');
  console.log('========================================');
  console.log(`Total kits in index: 38`);
  console.log(`Skipping: ${skipKits.size} (${[...skipKits].join(', ')})`);
  console.log(`Processing: ${kits.length} kits`);
  console.log(`Mode: ${exportOnly ? 'EXPORT ONLY' : identifyOnly ? 'IDENTIFY ONLY' : 'EXPORT + IDENTIFY'}`);

  if (!identifyOnly) {
    console.log(`\nFigma exports → ${EXPORTS_DIR}`);
  }
  // Check for Groq API key
  if (!process.env.GROQ_API_KEY) {
    console.warn('WARNING: GROQ_API_KEY not set - identification will be skipped');
    console.warn('Get a free key at: https://console.groq.com/keys');
  }

  const progress = loadProgress();
  let exportCount = 0;
  let identifyCount = 0;
  let errorCount = 0;

  // Pipeline: export kit N+1 while identifying kit N
  let pendingIdentify = null; // promise for background identification

  for (let i = 0; i < kits.length; i++) {
    const kit = kits[i];
    console.log(`\n[${ i + 1}/${kits.length}] === ${kit.name} (${kit.items} items, key: ${kit.file_key}) ===`);

    // EXPORT (foreground)
    if (!identifyOnly && !progress.exported[kit.file_key]) {
      console.log(`  Exporting PNGs...`);
      try {
        await runScript(path.join(SCRIPTS_DIR, 'export-figma-screens.js'), [kit.file_key]);
        progress.exported[kit.file_key] = {
          kit_name: kit.name,
          completed_at: new Date().toISOString()
        };
        saveProgress(progress);
        exportCount++;
        console.log(`  ✓ Export complete`);
      } catch (err) {
        console.error(`  ✗ Export failed: ${err.message}`);
        errorCount++;
        continue;
      }
      await new Promise(r => setTimeout(r, 1000));
    } else if (!identifyOnly) {
      console.log(`  Export already done (skipping)`);
    }

    // Wait for any previous identification to finish before starting new one
    if (pendingIdentify) {
      await pendingIdentify;
      pendingIdentify = null;
    }

    // IDENTIFY (launch in background so next export can start)
    if (!exportOnly && process.env.GROQ_API_KEY && !progress.identified[kit.file_key]) {
      const screensDir = path.join(EXPORTS_DIR, kit.file_key, 'screens');
      if (fs.existsSync(screensDir)) {
        console.log(`  Running Groq vision identification...`);
        const kitRef = kit;
        pendingIdentify = runScript(path.join(SCRIPTS_DIR, 'identify-screens-groq.js'), [screensDir])
          .then(() => {
            progress.identified[kitRef.file_key] = {
              kit_name: kitRef.name,
              completed_at: new Date().toISOString()
            };
            saveProgress(progress);
            identifyCount++;
            console.log(`  ✓ Identification complete for ${kitRef.name}`);
          })
          .catch(err => {
            console.error(`  ✗ Identification failed for ${kitRef.name}: ${err.message}`);
            errorCount++;
          });

        // If this is the last kit, wait for it
        if (i === kits.length - 1) {
          await pendingIdentify;
          pendingIdentify = null;
        }
      } else {
        console.log(`  No screens directory found, skipping identification`);
      }
    } else if (!exportOnly) {
      console.log(`  Identification already done (skipping)`);
    }
  }

  // Final wait for any trailing identification
  if (pendingIdentify) await pendingIdentify;

  // Summary
  console.log('\n========================================');
  console.log('  BATCH COMPLETE');
  console.log('========================================');
  console.log(`Exported: ${exportCount} kits`);
  console.log(`Identified: ${identifyCount} kits`);
  console.log(`Errors: ${errorCount}`);
  console.log(`Total exported so far: ${Object.keys(progress.exported).length + 1}/38`); // +1 for Brainwave
  console.log(`Total identified so far: ${Object.keys(progress.identified).length + 1}/38`);
  console.log(`\nProgress saved to: ${PROGRESS_FILE}`);
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});
