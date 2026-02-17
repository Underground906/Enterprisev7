'use client';

import { useState } from 'react';
import SearchResults, { type SearchResult } from '@/components/boilerplates/SearchResults';

// ============================================================
// DEMO: Semantic Search (LIB_D)
// Shows the SearchResults boilerplate with sample knowledge data
// ============================================================

const SAMPLE_RESULTS: SearchResult[] = [
  {
    id: '1',
    title: 'MASTER_CONTEXT.md',
    snippet: 'Enterprise OS is a knowledge architecture and business automation platform. It organises every artifact, thread, and framework into an 8-component structure with 23 domain pillars...',
    source: 'Core Engine',
    type: 'Framework',
    relevance: 97,
    date: '2026-02-16',
    pillar: 'Enterprise OS',
    tags: ['architecture', 'governance', 'canonical'],
  },
  {
    id: '2',
    title: 'PRD_Enterprise_OS_V7_MASTER.md',
    snippet: 'Product requirements for Enterprise OS V7 platform build. Covers 8 modules with 41 core screens, S>C>E governance model, 7-level permissions, and agent-powered knowledge management...',
    source: 'Build Factory',
    type: 'Template',
    relevance: 92,
    date: '2026-02-13',
    pillar: 'Product Dev',
    tags: ['PRD', 'requirements', 'screens'],
  },
  {
    id: '3',
    title: 'keyword_lattice_property.json',
    snippet: 'Comprehensive keyword lattice for Property Connect London. 847 keywords across 12 topic clusters including estate agents, property search, AI chatbot, and London property market...',
    source: 'Domain Pillars',
    type: 'Schema',
    relevance: 78,
    date: '2026-02-15',
    pillar: 'Property',
    tags: ['keywords', 'SEO', 'property', 'lattice'],
  },
  {
    id: '4',
    title: 'brand_voice_rules.md',
    snippet: 'Canonical brand voice guidelines. Tone: authoritative but accessible. Avoid: corporate jargon, passive voice, hedging. Use: direct statements, British English, industry terminology when appropriate...',
    source: 'Canon',
    type: 'Canonical Ref',
    relevance: 85,
    date: '2026-02-10',
    pillar: 'Branding',
    tags: ['brand', 'voice', 'tone', 'guidelines'],
  },
  {
    id: '5',
    title: 'competitor_analysis_q1.md',
    snippet: 'Q1 competitor analysis covering 14 property tech companies. Key finding: no competitor combines AI chatbot with knowledge management. Opportunity gap in the £200-500/month price point...',
    source: 'Market Research',
    type: 'Market Intel',
    relevance: 71,
    date: '2026-02-14',
    pillar: 'Market Research',
    tags: ['competitors', 'property tech', 'analysis'],
  },
  {
    id: '6',
    title: 'UI_ASSEMBLY_PIPELINE_SPEC.md',
    snippet: 'Specification for the 6-stage UI assembly pipeline: Export > Identify > Structure > Match > Extract > Assemble. Covers 38 Figma kits, 15 boilerplate types, and automated screen generation...',
    source: 'Build Factory',
    type: 'SOP',
    relevance: 88,
    date: '2026-02-16',
    pillar: 'UI Library',
    tags: ['pipeline', 'UI', 'Figma', 'assembly'],
  },
  {
    id: '7',
    title: 'headline_formulas.json',
    snippet: '142 proven headline formulas categorised by purpose: curiosity (23), benefit-driven (31), urgency (18), social proof (22), question-based (19), how-to (14), list-based (15)...',
    source: 'Canon',
    type: 'Canonical Ref',
    relevance: 65,
    date: '2026-02-08',
    pillar: 'Copy',
    tags: ['headlines', 'copywriting', 'formulas'],
  },
  {
    id: '8',
    title: 'ROUTING_MANIFEST.md',
    snippet: 'Routing rules for the Enterprise OS ingestion pipeline. Defines how incoming content gets classified, tagged, and routed to the correct pillar and subfolder based on content type and domain...',
    source: 'Core Engine',
    type: 'SOP',
    relevance: 82,
    date: '2026-02-12',
    pillar: 'Core Engine',
    tags: ['routing', 'ingestion', 'pipeline', 'rules'],
  },
];

export default function SemanticSearchPage() {
  const [results, setResults] = useState<SearchResult[]>([]);
  const [selected, setSelected] = useState<SearchResult | null>(null);

  return (
    <SearchResults
      title="Semantic Search"
      placeholder="Search across all knowledge, frameworks, and artifacts..."
      results={results}
      totalCount={results.length}
      onSearch={(query) => {
        if (!query) {
          setResults([]);
          return;
        }
        // Demo: filter sample results by query
        const q = query.toLowerCase();
        setResults(
          SAMPLE_RESULTS.filter(
            (r) =>
              r.title.toLowerCase().includes(q) ||
              r.snippet.toLowerCase().includes(q) ||
              r.tags?.some((t) => t.includes(q)) ||
              r.pillar?.toLowerCase().includes(q)
          )
        );
      }}
      filters={[
        {
          key: 'type',
          label: 'Content Type',
          options: [
            { value: 'Framework', label: 'Framework', count: 12 },
            { value: 'Schema', label: 'Schema', count: 34 },
            { value: 'Template', label: 'Template', count: 28 },
            { value: 'SOP', label: 'SOP', count: 15 },
            { value: 'Canonical Ref', label: 'Canonical Ref', count: 42 },
            { value: 'Market Intel', label: 'Market Intel', count: 8 },
          ],
        },
        {
          key: 'pillar',
          label: 'Pillar',
          options: [
            { value: 'Enterprise OS', label: 'Enterprise OS', count: 156 },
            { value: 'Property', label: 'Property', count: 89 },
            { value: 'Branding', label: 'Branding', count: 45 },
            { value: 'Copy', label: 'Copy', count: 67 },
            { value: 'UI Library', label: 'UI Library', count: 34 },
            { value: 'Market Research', label: 'Market Research', count: 23 },
          ],
        },
        {
          key: 'state',
          label: 'State',
          options: [
            { value: 'staging', label: 'Staging', count: 1412 },
            { value: 'canonical', label: 'Canonical', count: 1203 },
            { value: 'execution', label: 'Execution', count: 232 },
          ],
        },
      ]}
      sortOptions={[
        { value: 'relevance', label: 'Most Relevant' },
        { value: 'date', label: 'Most Recent' },
        { value: 'title', label: 'Alphabetical' },
      ]}
      activeSort="relevance"
      recentSearches={['property connect', 'headline formulas', 'routing rules', 'agent framework']}
      suggestions={['knowledge architecture', 'UI components', 'brand guidelines', 'keyword lattice', 'fitness app']}
      onResultClick={setSelected}
      selectedResult={selected}
      previewPanel={(result) => (
        <div>
          <h3 style={{ fontSize: 16, fontWeight: 600, marginBottom: 16, color: 'var(--text-primary)' }}>{result.title}</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Type</div>
              <span style={{ fontSize: 12, padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', color: 'var(--text-secondary)' }}>
                {result.type}
              </span>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Pillar</div>
              <span style={{ fontSize: 12, padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-purple-light)', color: 'var(--accent-purple)' }}>
                {result.pillar}
              </span>
            </div>
            {result.relevance !== undefined && (
              <div>
                <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Relevance Score</div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <div style={{ flex: 1, height: 6, borderRadius: 3, background: 'var(--bg-tertiary)' }}>
                    <div style={{ width: `${result.relevance}%`, height: '100%', borderRadius: 3, background: 'var(--accent-green)' }} />
                  </div>
                  <span style={{ fontSize: 13, fontWeight: 500, color: 'var(--text-primary)' }}>{result.relevance}%</span>
                </div>
              </div>
            )}
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Content Preview</div>
              <p style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.6, margin: 0 }}>
                {result.snippet}
              </p>
            </div>
            {result.tags && (
              <div>
                <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Tags</div>
                <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap' }}>
                  {result.tags.map((tag) => (
                    <span key={tag} style={{ fontSize: 11, padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', color: 'var(--text-tertiary)' }}>
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            )}
            <div style={{ marginTop: 8, display: 'flex', gap: 8 }}>
              <button style={{ flex: 1, padding: '8px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-purple)', color: '#fff', fontSize: 13, cursor: 'pointer', fontWeight: 500 }}>
                Open File
              </button>
              <button style={{ flex: 1, padding: '8px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-default)', background: 'var(--bg-secondary)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer' }}>
                Copy Path
              </button>
            </div>
          </div>
        </div>
      )}
    />
  );
}
