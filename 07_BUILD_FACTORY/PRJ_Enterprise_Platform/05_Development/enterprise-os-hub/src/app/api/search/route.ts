import { NextRequest, NextResponse } from 'next/server';
import { searchFiles } from '@/lib/files';

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q') || '';

  if (!query || query.length < 2) {
    return NextResponse.json({ results: [], query });
  }

  try {
    const results = searchFiles(query);
    return NextResponse.json({ results, query, count: results.length });
  } catch (error) {
    return NextResponse.json(
      { error: error instanceof Error ? error.message : 'Unknown error' },
      { status: 500 }
    );
  }
}
