/**
 * Export all screens from a Figma file as PNGs (v2 - deep export)
 * Usage: node scripts/export-figma-screens.js [file_key] [output_dir] [--clean]
 *
 * v2 improvements:
 * - Uses depth=4 to find screens nested inside grouping canvases
 * - Recursively walks the document tree to find screen-like frames
 * - Heuristic: frames wider than 2500px (or taller than 5000px) with 2+
 *   screen-sized children are treated as grouping canvases — their children
 *   are exported instead of the giant canvas itself
 * - --clean flag removes old exports before starting fresh
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const FIGMA_TOKEN = 'figd_g9DpIKh1XeMwfLCR5ScuKOv_N7FhRCYbBqxIFHdi';
const DEFAULT_FILE_KEY = '6hCuwRI0GsBmIOJelAVpND'; // Brainwave 2.0

const positionalArgs = process.argv.slice(2).filter(a => !a.startsWith('--'));
const flags = new Set(process.argv.slice(2).filter(a => a.startsWith('--')));

const fileKey = positionalArgs[0] || DEFAULT_FILE_KEY;
const outputDir = positionalArgs[1] || path.join(__dirname, '..', 'public', 'figma-exports', fileKey);
const cleanMode = flags.has('--clean');

function figmaGet(endpoint) {
  return new Promise((resolve, reject) => {
    const url = `https://api.figma.com/v1${endpoint}`;
    console.log(`  GET ${url.substring(0, 100)}...`);
    const req = https.get(url, {
      headers: { 'X-Figma-Token': FIGMA_TOKEN }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode !== 200) {
          reject(new Error(`Figma API ${res.statusCode}: ${data.substring(0, 200)}`));
          return;
        }
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`JSON parse error: ${e.message}`)); }
      });
    });
    req.on('error', reject);
    req.setTimeout(120000, () => { req.destroy(); reject(new Error('Timeout')); });
  });
}

function downloadFile(url, dest) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(dest);
    const doGet = (targetUrl) => {
      const mod = targetUrl.startsWith('https') ? https : require('http');
      mod.get(targetUrl, (res) => {
        if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
          doGet(res.headers.location);
          return;
        }
        res.pipe(file);
        file.on('finish', () => { file.close(); resolve(); });
      }).on('error', (err) => { fs.unlink(dest, () => {}); reject(err); });
    };
    doGet(url);
  });
}

function slugify(name) {
  return name.replace(/[^a-zA-Z0-9]+/g, '_').replace(/^_|_$/g, '').toLowerCase();
}

/**
 * Recursively find screen-like frames in the Figma document tree.
 *
 * Heuristic:
 * - A FRAME wider than 2500px OR taller than 5000px that contains 2+
 *   frame children >= 300px wide is a grouping canvas → recurse into children
 * - Everything else that's a FRAME/COMPONENT/COMPONENT_SET >= 300px wide → screen
 */
function findScreenFrames(node, pageName, ancestors) {
  const results = [];
  const EXPORTABLE = new Set(['FRAME', 'COMPONENT', 'COMPONENT_SET']);

  if (!node) return results;

  // Pages and document: always recurse
  if (node.type === 'CANVAS' || node.type === 'DOCUMENT') {
    const pName = node.type === 'CANVAS' ? node.name : pageName;
    for (const child of (node.children || [])) {
      results.push(...findScreenFrames(child, pName, []));
    }
    return results;
  }

  if (!EXPORTABLE.has(node.type)) return results;

  const w = node.absoluteBoundingBox?.width || 0;
  const h = node.absoluteBoundingBox?.height || 0;
  if (w < 300) return results;

  // Check for screen-like frame children
  const frameChildren = (node.children || []).filter(c => EXPORTABLE.has(c.type));
  const screenLikeChildren = frameChildren.filter(c => {
    const cw = c.absoluteBoundingBox?.width || 0;
    const ch = c.absoluteBoundingBox?.height || 0;
    return cw >= 300 && ch >= 200;
  });

  const isGroupingCanvas = screenLikeChildren.length >= 2 && (w > 2500 || h > 5000);

  if (isGroupingCanvas) {
    // Container frame — recurse into its frame children
    for (const child of frameChildren) {
      results.push(...findScreenFrames(child, pageName, [...ancestors, node.name]));
    }
  } else {
    // Actual screen — export it
    const nameParts = [pageName, ...ancestors, node.name];
    // Remove consecutive duplicate name segments
    const deduped = nameParts.filter((p, i) => i === 0 || p !== nameParts[i - 1]);

    results.push({
      id: node.id,
      name: node.name,
      page: pageName,
      type: node.type,
      width: Math.round(w),
      height: Math.round(h),
      is_screen: w >= 800,
      slug: slugify(deduped.join('_')),
      exported: false
    });
  }

  return results;
}

async function main() {
  console.log(`\n=== FIGMA SCREEN EXPORTER v2 (deep) ===`);
  console.log(`File: ${fileKey}`);
  console.log(`Output: ${outputDir}`);
  console.log(`Clean mode: ${cleanMode}\n`);

  // Clean old exports if requested
  if (cleanMode) {
    for (const sub of ['screens', 'components']) {
      const dir = path.join(outputDir, sub);
      if (fs.existsSync(dir)) {
        fs.rmSync(dir, { recursive: true });
        console.log(`  Cleaned ${dir}`);
      }
    }
    const inv = path.join(outputDir, 'component_inventory.json');
    if (fs.existsSync(inv)) {
      fs.unlinkSync(inv);
      console.log(`  Removed stale component_inventory.json`);
    }
    console.log('');
  }

  // Create output directories
  fs.mkdirSync(path.join(outputDir, 'screens'), { recursive: true });
  fs.mkdirSync(path.join(outputDir, 'components'), { recursive: true });

  // Step 1: Get file structure at depth=4 (catches nested screens)
  console.log('Step 1: Fetching file structure (depth=4)...');
  const file = await figmaGet(`/files/${fileKey}?depth=4`);
  console.log(`  File: ${file.name}`);
  console.log(`  Pages: ${file.document.children.length}\n`);

  // Step 2: Recursively find all screen-like frames
  console.log('Step 2: Finding screen frames (recursive walk)...');
  const allFrames = findScreenFrames(file.document, '', []);

  // Deduplicate slugs (add numeric suffix on collisions)
  const slugCount = {};
  for (const frame of allFrames) {
    if (slugCount[frame.slug]) {
      slugCount[frame.slug]++;
      frame.slug = `${frame.slug}_${slugCount[frame.slug]}`;
    } else {
      slugCount[frame.slug] = 1;
    }
  }

  const manifest = {
    file_name: file.name,
    file_key: fileKey,
    exported_at: new Date().toISOString(),
    export_depth: 4,
    pages: file.document.children.map(p => ({
      name: p.name,
      id: p.id,
      frame_count: allFrames.filter(f => f.page === p.name).length
    })),
    screens: allFrames,
    total_screens: allFrames.length,
    total_exported: 0
  };

  const frameIds = allFrames.filter(f => f.width >= 300);

  // Show per-page breakdown
  for (const p of manifest.pages) {
    console.log(`  Page "${p.name}": ${p.frame_count} frames`);
  }
  console.log(`\n  Total screen frames found: ${allFrames.length}`);
  console.log(`  Frames to export: ${frameIds.length}\n`);

  // Step 3: Export in batches of 8
  const BATCH_SIZE = 8;
  let exported = 0;

  for (let i = 0; i < frameIds.length; i += BATCH_SIZE) {
    const batch = frameIds.slice(i, i + BATCH_SIZE);
    const ids = batch.map(f => f.id).join(',');

    console.log(`Step 3: Exporting batch ${Math.floor(i / BATCH_SIZE) + 1}/${Math.ceil(frameIds.length / BATCH_SIZE)} (${batch.length} frames)...`);

    try {
      const images = await figmaGet(`/images/${fileKey}?ids=${ids}&format=png&scale=1`);

      for (const frame of batch) {
        const imageUrl = images.images?.[frame.id];
        if (imageUrl) {
          const subdir = frame.is_screen ? 'screens' : 'components';
          const filename = `${frame.slug}.png`;
          const dest = path.join(outputDir, subdir, filename);

          try {
            await downloadFile(imageUrl, dest);
            frame.exported = true;
            frame.file = `${subdir}/${filename}`;
            exported++;
            process.stdout.write(`  ${frame.name} (${frame.width}x${frame.height})\n`);
          } catch (err) {
            process.stdout.write(`  FAIL ${frame.name}: ${err.message}\n`);
          }
        }
      }
    } catch (err) {
      console.error(`  Batch error: ${err.message}`);
    }

    // Checkpoint: save manifest after each batch
    manifest.total_exported = exported;
    fs.writeFileSync(path.join(outputDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
    console.log(`  Checkpoint saved (${exported}/${frameIds.length} exported)\n`);

    // Rate limit pause
    if (i + BATCH_SIZE < frameIds.length) {
      await new Promise(r => setTimeout(r, 1000));
    }
  }

  // Final manifest
  manifest.total_exported = exported;
  fs.writeFileSync(path.join(outputDir, 'manifest.json'), JSON.stringify(manifest, null, 2));

  console.log(`\n=== EXPORT COMPLETE ===`);
  console.log(`Screens exported: ${exported}/${frameIds.length}`);
  console.log(`Manifest: ${path.join(outputDir, 'manifest.json')}`);
  console.log(`Screens: ${path.join(outputDir, 'screens/')}`);
  console.log(`Components: ${path.join(outputDir, 'components/')}\n`);
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});
