/**
 * Export all screens from a Figma file as PNGs
 * Usage: node scripts/export-figma-screens.js [file_key] [output_dir]
 *
 * Exports every top-level frame from each page as a PNG image,
 * plus generates a manifest.json cataloguing every component.
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const FIGMA_TOKEN = 'figd_g9DpIKh1XeMwfLCR5ScuKOv_N7FhRCYbBqxIFHdi';
const DEFAULT_FILE_KEY = '6hCuwRI0GsBmIOJelAVpND'; // Brainwave 2.0

const fileKey = process.argv[2] || DEFAULT_FILE_KEY;
const outputDir = process.argv[3] || path.join(__dirname, '..', 'public', 'figma-exports', fileKey);

function figmaGet(endpoint) {
  return new Promise((resolve, reject) => {
    const url = `https://api.figma.com/v1${endpoint}`;
    console.log(`  GET ${url.substring(0, 80)}...`);
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

async function main() {
  console.log(`\n=== FIGMA SCREEN EXPORTER ===`);
  console.log(`File: ${fileKey}`);
  console.log(`Output: ${outputDir}\n`);

  // Create output directories
  fs.mkdirSync(path.join(outputDir, 'screens'), { recursive: true });
  fs.mkdirSync(path.join(outputDir, 'components'), { recursive: true });

  // Step 1: Get file structure
  console.log('Step 1: Fetching file structure...');
  const file = await figmaGet(`/files/${fileKey}?depth=2`);
  console.log(`  File: ${file.name}`);
  console.log(`  Pages: ${file.document.children.length}\n`);

  const manifest = {
    file_name: file.name,
    file_key: fileKey,
    exported_at: new Date().toISOString(),
    pages: [],
    screens: [],
    total_screens: 0,
    total_exported: 0
  };

  // Step 2: Collect all exportable frames
  const frameIds = [];

  for (const page of file.document.children) {
    const pageInfo = {
      name: page.name,
      id: page.id,
      frames: []
    };

    if (page.children) {
      for (const child of page.children) {
        // Export frames that are likely screens (width > 300px)
        if (child.type === 'FRAME' || child.type === 'COMPONENT' || child.type === 'COMPONENT_SET') {
          const w = child.absoluteBoundingBox?.width || 0;
          const h = child.absoluteBoundingBox?.height || 0;

          const frameInfo = {
            id: child.id,
            name: child.name,
            page: page.name,
            type: child.type,
            width: Math.round(w),
            height: Math.round(h),
            is_screen: w >= 800, // likely a full screen
            slug: slugify(`${page.name}_${child.name}`),
            exported: false
          };

          pageInfo.frames.push(frameInfo);
          manifest.screens.push(frameInfo);

          if (w >= 300) { // export anything reasonably sized
            frameIds.push(frameInfo);
          }
        }
      }
    }

    manifest.pages.push(pageInfo);
    console.log(`  Page "${page.name}": ${pageInfo.frames.length} frames`);
  }

  manifest.total_screens = manifest.screens.length;
  console.log(`\nTotal frames found: ${manifest.total_screens}`);
  console.log(`Frames to export (width >= 300px): ${frameIds.length}\n`);

  // Step 3: Export in batches of 20 (Figma API limit)
  const BATCH_SIZE = 8; // Smaller batches to avoid Figma API timeouts
  let exported = 0;

  for (let i = 0; i < frameIds.length; i += BATCH_SIZE) {
    const batch = frameIds.slice(i, i + BATCH_SIZE);
    const ids = batch.map(f => f.id).join(',');

    console.log(`Step 3: Exporting batch ${Math.floor(i/BATCH_SIZE) + 1}/${Math.ceil(frameIds.length/BATCH_SIZE)} (${batch.length} frames)...`);

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
            process.stdout.write(`  ✓ ${frame.name} (${frame.width}x${frame.height})\n`);
          } catch (err) {
            process.stdout.write(`  ✗ ${frame.name}: ${err.message}\n`);
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
