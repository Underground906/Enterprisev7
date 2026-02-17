import { NextRequest, NextResponse } from 'next/server';
import { readDirectory, readFileContent, getDirectoryStats } from '@/lib/files';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const path = searchParams.get('path') || '';
  const action = searchParams.get('action') || 'list';
  const depth = parseInt(searchParams.get('depth') || '1');

  try {
    if (action === 'read') {
      const content = readFileContent(path);
      if (content === null) {
        return NextResponse.json({ error: 'File not found' }, { status: 404 });
      }
      return NextResponse.json({ path, content });
    }

    if (action === 'stats') {
      const stats = getDirectoryStats(path);
      return NextResponse.json({ path, stats });
    }

    // Default: list directory
    const entries = readDirectory(path, depth);
    return NextResponse.json({ path, entries });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    );
  }
}
