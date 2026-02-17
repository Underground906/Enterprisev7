'use client';

import { useState } from 'react';
import { Search, X, SlidersHorizontal, ChevronDown, ChevronUp, FileText, ExternalLink } from 'lucide-react';

// ============================================================
// SEARCH RESULTS BOILERPLATE
// Used by: Semantic Search (LIB_D), Global Search,
//          any screen with search → results → detail preview
// Layout: Search bar + Filter sidebar + Results list + Preview
// ============================================================

export interface SearchResult {
  id: string;
  title: string;
  snippet: string;
  source?: string;
  type?: string;
  relevance?: number;
  date?: string;
  pillar?: string;
  tags?: string[];
  url?: string;
}

export interface SearchFilter {
  key: string;
  label: string;
  options: { value: string; label: string; count?: number }[];
  multi?: boolean;
}

interface SearchResultsProps {
  title?: string;
  placeholder?: string;
  results: SearchResult[];
  totalCount?: number;
  filters?: SearchFilter[];
  onSearch: (query: string) => void;
  onFilterChange?: (filters: Record<string, string[]>) => void;
  onResultClick?: (result: SearchResult) => void;
  selectedResult?: SearchResult | null;
  previewPanel?: (result: SearchResult) => React.ReactNode;
  loading?: boolean;
  suggestions?: string[];
  recentSearches?: string[];
  sortOptions?: { value: string; label: string }[];
  activeSort?: string;
  onSortChange?: (sort: string) => void;
}

function RelevanceMeter({ score }: { score: number }) {
  const width = Math.min(Math.max(score, 0), 100);
  const color = width >= 80 ? 'var(--accent-green)' : width >= 50 ? 'var(--accent-amber)' : 'var(--accent-red)';
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
      <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
        <div style={{ width: `${width}%`, height: '100%', borderRadius: 2, background: color, transition: 'width 0.3s' }} />
      </div>
      <span style={{ fontSize: 11, color: 'var(--text-tertiary)', fontWeight: 500 }}>{score}%</span>
    </div>
  );
}

function ResultCard({
  result,
  isSelected,
  onClick,
}: {
  result: SearchResult;
  isSelected: boolean;
  onClick: () => void;
}) {
  return (
    <div
      onClick={onClick}
      style={{
        padding: '14px 16px',
        background: isSelected ? 'var(--bg-active)' : 'var(--bg-card)',
        border: `1px solid ${isSelected ? 'var(--border-accent)' : 'var(--border-default)'}`,
        borderRadius: 'var(--radius-md)',
        cursor: 'pointer',
        transition: 'all 0.15s',
      }}
      onMouseEnter={(e) => {
        if (!isSelected) e.currentTarget.style.borderColor = 'var(--border-accent)';
      }}
      onMouseLeave={(e) => {
        if (!isSelected) e.currentTarget.style.borderColor = 'var(--border-default)';
      }}
    >
      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: 6 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <FileText size={14} style={{ color: 'var(--accent-purple)', flexShrink: 0 }} />
          <span style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>{result.title}</span>
        </div>
        {result.relevance !== undefined && <RelevanceMeter score={result.relevance} />}
      </div>
      <p style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.5, margin: '0 0 8px', paddingLeft: 22 }}>
        {result.snippet}
      </p>
      <div style={{ display: 'flex', alignItems: 'center', gap: 12, paddingLeft: 22 }}>
        {result.type && (
          <span style={{ fontSize: 11, padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', color: 'var(--text-tertiary)', fontWeight: 500 }}>
            {result.type}
          </span>
        )}
        {result.pillar && (
          <span style={{ fontSize: 11, padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-purple-light)', color: 'var(--accent-purple)', fontWeight: 500 }}>
            {result.pillar}
          </span>
        )}
        {result.source && (
          <span style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>{result.source}</span>
        )}
        {result.date && (
          <span style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>{result.date}</span>
        )}
      </div>
      {result.tags && result.tags.length > 0 && (
        <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap', marginTop: 8, paddingLeft: 22 }}>
          {result.tags.map((tag) => (
            <span key={tag} style={{ fontSize: 10, padding: '1px 6px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', color: 'var(--text-tertiary)' }}>
              {tag}
            </span>
          ))}
        </div>
      )}
    </div>
  );
}

export default function SearchResults({
  title,
  placeholder = 'Search across all knowledge...',
  results,
  totalCount,
  filters,
  onSearch,
  onFilterChange,
  onResultClick,
  selectedResult,
  previewPanel,
  loading,
  suggestions,
  recentSearches,
  sortOptions,
  activeSort,
  onSortChange,
}: SearchResultsProps) {
  const [query, setQuery] = useState('');
  const [showFilters, setShowFilters] = useState(true);
  const [activeFilters, setActiveFilters] = useState<Record<string, string[]>>({});
  const [showPreview, setShowPreview] = useState(false);
  const [expandedFilterGroups, setExpandedFilterGroups] = useState<Set<string>>(
    new Set(filters?.map((f) => f.key) || [])
  );

  const handleSearch = (value: string) => {
    setQuery(value);
    onSearch(value);
  };

  const toggleFilter = (filterKey: string, value: string) => {
    setActiveFilters((prev) => {
      const current = prev[filterKey] || [];
      const updated = current.includes(value)
        ? current.filter((v) => v !== value)
        : [...current, value];
      const next = { ...prev, [filterKey]: updated };
      onFilterChange?.(next);
      return next;
    });
  };

  const toggleFilterGroup = (key: string) => {
    setExpandedFilterGroups((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const handleResultClick = (result: SearchResult) => {
    onResultClick?.(result);
    setShowPreview(true);
  };

  const hasNoResults = !loading && query && results.length === 0;
  const showSuggestions = !query && (suggestions || recentSearches);

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Filter Sidebar */}
      {showFilters && filters && filters.length > 0 && (
        <div
          style={{
            width: 240,
            minWidth: 240,
            borderRight: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            overflow: 'auto',
            padding: '20px 16px',
          }}
        >
          <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 16 }}>Filters</div>
          {filters.map((filter) => (
            <div key={filter.key} style={{ marginBottom: 16 }}>
              <button
                onClick={() => toggleFilterGroup(filter.key)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  width: '100%',
                  padding: '6px 0',
                  border: 'none',
                  background: 'transparent',
                  fontSize: 12,
                  fontWeight: 500,
                  color: 'var(--text-secondary)',
                  cursor: 'pointer',
                  textTransform: 'uppercase',
                  letterSpacing: '0.04em',
                }}
              >
                {filter.label}
                {expandedFilterGroups.has(filter.key) ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
              </button>
              {expandedFilterGroups.has(filter.key) && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 4, marginTop: 8 }}>
                  {filter.options.map((opt) => {
                    const isActive = (activeFilters[filter.key] || []).includes(opt.value);
                    return (
                      <label
                        key={opt.value}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: 8,
                          fontSize: 13,
                          color: isActive ? 'var(--text-primary)' : 'var(--text-secondary)',
                          cursor: 'pointer',
                          padding: '4px 0',
                        }}
                      >
                        <input
                          type="checkbox"
                          checked={isActive}
                          onChange={() => toggleFilter(filter.key, opt.value)}
                          style={{ accentColor: 'var(--accent-purple)' }}
                        />
                        {opt.label}
                        {opt.count !== undefined && (
                          <span style={{ fontSize: 11, color: 'var(--text-tertiary)', marginLeft: 'auto' }}>
                            {opt.count}
                          </span>
                        )}
                      </label>
                    );
                  })}
                </div>
              )}
            </div>
          ))}
        </div>
      )}

      {/* Main Results */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        <div style={{ padding: '20px 24px 0' }}>
          {/* Title */}
          {title && (
            <h2 style={{ fontSize: 18, fontWeight: 600, color: 'var(--text-primary)', margin: '0 0 16px' }}>{title}</h2>
          )}

          {/* Search Bar */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 16px',
              border: '1px solid var(--border-default)',
              borderRadius: 'var(--radius-lg)',
              background: 'var(--bg-card)',
              marginBottom: 16,
              boxShadow: 'var(--shadow-sm)',
            }}
          >
            <Search size={18} style={{ color: 'var(--text-tertiary)', flexShrink: 0 }} />
            <input
              type="text"
              placeholder={placeholder}
              value={query}
              onChange={(e) => handleSearch(e.target.value)}
              style={{
                border: 'none',
                outline: 'none',
                background: 'transparent',
                fontSize: 14,
                color: 'var(--text-primary)',
                width: '100%',
              }}
            />
            {query && (
              <button
                onClick={() => handleSearch('')}
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 0 }}
              >
                <X size={16} />
              </button>
            )}
            <button
              onClick={() => setShowFilters(!showFilters)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 6,
                padding: '6px 12px',
                border: '1px solid var(--border-default)',
                borderRadius: 'var(--radius-md)',
                background: showFilters ? 'var(--bg-active)' : 'var(--bg-secondary)',
                color: showFilters ? 'var(--accent-purple)' : 'var(--text-secondary)',
                fontSize: 12,
                cursor: 'pointer',
                flexShrink: 0,
              }}
            >
              <SlidersHorizontal size={12} /> Filters
            </button>
          </div>

          {/* Results meta row */}
          {query && results.length > 0 && (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
              <span style={{ fontSize: 13, color: 'var(--text-tertiary)' }}>
                {totalCount || results.length} results for &ldquo;{query}&rdquo;
              </span>
              {sortOptions && (
                <select
                  value={activeSort}
                  onChange={(e) => onSortChange?.(e.target.value)}
                  style={{
                    padding: '5px 10px',
                    border: '1px solid var(--border-default)',
                    borderRadius: 'var(--radius-md)',
                    background: 'var(--bg-secondary)',
                    fontSize: 12,
                    color: 'var(--text-secondary)',
                    cursor: 'pointer',
                    outline: 'none',
                  }}
                >
                  {sortOptions.map((opt) => (
                    <option key={opt.value} value={opt.value}>{opt.label}</option>
                  ))}
                </select>
              )}
            </div>
          )}
        </div>

        {/* Results List */}
        <div style={{ flex: 1, overflow: 'auto', padding: '0 24px 24px' }}>
          {loading ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {[...Array(6)].map((_, i) => (
                <div
                  key={i}
                  style={{
                    height: 80,
                    background: 'var(--bg-tertiary)',
                    borderRadius: 'var(--radius-md)',
                    opacity: 1 - i * 0.12,
                  }}
                />
              ))}
            </div>
          ) : hasNoResults ? (
            <div style={{ textAlign: 'center', padding: '60px 24px' }}>
              <div style={{ fontSize: 16, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 8 }}>
                No results found
              </div>
              <div style={{ fontSize: 13, color: 'var(--text-tertiary)' }}>
                Try different keywords or adjust your filters
              </div>
            </div>
          ) : showSuggestions ? (
            <div style={{ padding: '20px 0' }}>
              {recentSearches && recentSearches.length > 0 && (
                <div style={{ marginBottom: 24 }}>
                  <div style={{ fontSize: 12, fontWeight: 500, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: 12 }}>
                    Recent Searches
                  </div>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                    {recentSearches.map((s) => (
                      <button
                        key={s}
                        onClick={() => handleSearch(s)}
                        style={{
                          padding: '6px 14px',
                          borderRadius: 20,
                          border: '1px solid var(--border-default)',
                          background: 'var(--bg-card)',
                          color: 'var(--text-secondary)',
                          fontSize: 13,
                          cursor: 'pointer',
                        }}
                      >
                        {s}
                      </button>
                    ))}
                  </div>
                </div>
              )}
              {suggestions && suggestions.length > 0 && (
                <div>
                  <div style={{ fontSize: 12, fontWeight: 500, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: 12 }}>
                    Suggested Searches
                  </div>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
                    {suggestions.map((s) => (
                      <button
                        key={s}
                        onClick={() => handleSearch(s)}
                        style={{
                          padding: '6px 14px',
                          borderRadius: 20,
                          border: '1px solid var(--border-default)',
                          background: 'var(--bg-card)',
                          color: 'var(--text-secondary)',
                          fontSize: 13,
                          cursor: 'pointer',
                        }}
                      >
                        {s}
                      </button>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              {results.map((result) => (
                <ResultCard
                  key={result.id}
                  result={result}
                  isSelected={selectedResult?.id === result.id}
                  onClick={() => handleResultClick(result)}
                />
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Preview Panel */}
      {showPreview && selectedResult && previewPanel && (
        <div
          style={{
            width: 400,
            minWidth: 400,
            borderLeft: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            overflow: 'auto',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <div
            style={{
              padding: '16px 20px',
              borderBottom: '1px solid var(--border-subtle)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
            }}
          >
            <span style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>Preview</span>
            <button
              onClick={() => setShowPreview(false)}
              style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 4 }}
            >
              <X size={16} />
            </button>
          </div>
          <div style={{ flex: 1, padding: '16px 20px', overflow: 'auto' }}>
            {previewPanel(selectedResult)}
          </div>
        </div>
      )}
    </div>
  );
}
