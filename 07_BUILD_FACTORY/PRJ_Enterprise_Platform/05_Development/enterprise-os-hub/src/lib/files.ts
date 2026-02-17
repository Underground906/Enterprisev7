// Server-side file system utilities for reading V7 folder structure
import fs from 'fs';
import path from 'path';
import { V7_ROOT } from './constants';

export interface FileEntry {
  name: string;
  path: string;         // relative to V7_ROOT
  absolutePath: string;
  type: 'file' | 'directory';
  extension?: string;
  size?: number;
  modified?: string;
  children?: FileEntry[];
}

export interface FileStats {
  totalFiles: number;
  totalDirs: number;
  totalSize: number;
  byExtension: Record<string, number>;
}

const IGNORED = new Set([
  'node_modules', '.git', '.next', '__pycache__', '.venv',
  'figma_library_v2', 'enterprise-os-hub', '.gitignore',
]);

const IGNORED_EXTENSIONS = new Set([
  '.pyc', '.pyo', '.exe', '.dll', '.so', '.dylib',
]);

export function readDirectory(relativePath: string = '', depth: number = 1): FileEntry[] {
  const absPath = path.join(V7_ROOT, relativePath);

  if (!fs.existsSync(absPath)) return [];

  const entries = fs.readdirSync(absPath, { withFileTypes: true });
  const result: FileEntry[] = [];

  for (const entry of entries) {
    if (IGNORED.has(entry.name)) continue;
    if (entry.name.startsWith('~$')) continue; // temp files
    if (entry.name.startsWith('.')) continue;

    const entryRelPath = relativePath ? `${relativePath}/${entry.name}` : entry.name;
    const entryAbsPath = path.join(absPath, entry.name);

    if (entry.isDirectory()) {
      const dirEntry: FileEntry = {
        name: entry.name,
        path: entryRelPath,
        absolutePath: entryAbsPath,
        type: 'directory',
      };

      if (depth > 1) {
        dirEntry.children = readDirectory(entryRelPath, depth - 1);
      }

      result.push(dirEntry);
    } else if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();
      if (IGNORED_EXTENSIONS.has(ext)) continue;

      try {
        const stat = fs.statSync(entryAbsPath);
        result.push({
          name: entry.name,
          path: entryRelPath,
          absolutePath: entryAbsPath,
          type: 'file',
          extension: ext,
          size: stat.size,
          modified: stat.mtime.toISOString(),
        });
      } catch {
        // Skip files we can't stat
      }
    }
  }

  // Sort: directories first, then alphabetical
  return result.sort((a, b) => {
    if (a.type !== b.type) return a.type === 'directory' ? -1 : 1;
    return a.name.localeCompare(b.name);
  });
}

export function readFileContent(relativePath: string): string | null {
  const absPath = path.join(V7_ROOT, relativePath);
  if (!fs.existsSync(absPath)) return null;

  try {
    return fs.readFileSync(absPath, 'utf-8');
  } catch {
    return null;
  }
}

export function getDirectoryStats(relativePath: string = ''): FileStats {
  const stats: FileStats = {
    totalFiles: 0,
    totalDirs: 0,
    totalSize: 0,
    byExtension: {},
  };

  function walk(dirPath: string) {
    const absPath = path.join(V7_ROOT, dirPath);
    if (!fs.existsSync(absPath)) return;

    const entries = fs.readdirSync(absPath, { withFileTypes: true });
    for (const entry of entries) {
      if (IGNORED.has(entry.name) || entry.name.startsWith('.') || entry.name.startsWith('~$')) continue;

      const entryRelPath = dirPath ? `${dirPath}/${entry.name}` : entry.name;

      if (entry.isDirectory()) {
        stats.totalDirs++;
        walk(entryRelPath);
      } else if (entry.isFile()) {
        const ext = path.extname(entry.name).toLowerCase() || '.other';
        if (IGNORED_EXTENSIONS.has(ext)) continue;

        stats.totalFiles++;
        stats.byExtension[ext] = (stats.byExtension[ext] || 0) + 1;

        try {
          const stat = fs.statSync(path.join(V7_ROOT, entryRelPath));
          stats.totalSize += stat.size;
        } catch { /* skip */ }
      }
    }
  }

  walk(relativePath);
  return stats;
}

export function searchFiles(query: string, relativePath: string = ''): FileEntry[] {
  const results: FileEntry[] = [];
  const lowerQuery = query.toLowerCase();

  function walk(dirPath: string) {
    const absPath = path.join(V7_ROOT, dirPath);
    if (!fs.existsSync(absPath)) return;

    const entries = fs.readdirSync(absPath, { withFileTypes: true });
    for (const entry of entries) {
      if (IGNORED.has(entry.name) || entry.name.startsWith('.') || entry.name.startsWith('~$')) continue;

      const entryRelPath = dirPath ? `${dirPath}/${entry.name}` : entry.name;
      const entryAbsPath = path.join(absPath, entry.name);

      if (entry.isDirectory()) {
        // Check folder name match
        if (entry.name.toLowerCase().includes(lowerQuery)) {
          results.push({
            name: entry.name,
            path: entryRelPath,
            absolutePath: entryAbsPath,
            type: 'directory',
          });
        }
        walk(entryRelPath);
      } else if (entry.isFile()) {
        const ext = path.extname(entry.name).toLowerCase();
        if (IGNORED_EXTENSIONS.has(ext)) continue;

        // Check filename match
        if (entry.name.toLowerCase().includes(lowerQuery)) {
          try {
            const stat = fs.statSync(entryAbsPath);
            results.push({
              name: entry.name,
              path: entryRelPath,
              absolutePath: entryAbsPath,
              type: 'file',
              extension: ext,
              size: stat.size,
              modified: stat.mtime.toISOString(),
            });
          } catch { /* skip */ }
        }
        // Check file content match for text files
        else if (['.md', '.txt', '.json', '.py', '.js', '.ts', '.sql', '.csv'].includes(ext)) {
          try {
            const content = fs.readFileSync(entryAbsPath, 'utf-8');
            if (content.toLowerCase().includes(lowerQuery)) {
              const stat = fs.statSync(entryAbsPath);
              results.push({
                name: entry.name,
                path: entryRelPath,
                absolutePath: entryAbsPath,
                type: 'file',
                extension: ext,
                size: stat.size,
                modified: stat.mtime.toISOString(),
              });
            }
          } catch { /* skip */ }
        }

        if (results.length >= 50) return; // Cap results
      }
    }
  }

  walk(relativePath);
  return results;
}
