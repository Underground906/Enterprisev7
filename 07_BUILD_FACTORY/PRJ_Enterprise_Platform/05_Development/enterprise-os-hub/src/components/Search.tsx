'use client';

import { useState, useEffect, useRef } from 'react';
import { Search as SearchIcon, File, Folder, X } from 'lucide-react';
import { useRouter } from 'next/navigation';

interface SearchResult {
  name: string;
  path: string;
  type: 'file' | 'directory';
  extension?: string;
}

export function Search() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const router = useRouter();

  useEffect(() => {
    if (query.length < 2) {
      setResults([]);
      return;
    }

    const timer = setTimeout(async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/search?q=${encodeURIComponent(query)}`);
        const data = await res.json();
        setResults(data.results || []);
      } catch {
        setResults([]);
      }
      setLoading(false);
    }, 300);

    return () => clearTimeout(timer);
  }, [query]);

  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        inputRef.current?.focus();
        setIsOpen(true);
      }
      if (e.key === 'Escape') {
        setIsOpen(false);
        setQuery('');
      }
    }
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  function handleSelect(result: SearchResult) {
    // Find which module this belongs to
    const parts = result.path.split('/');
    const topFolder = parts[0];
    const moduleMap: Record<string, string> = {
      '00_SYSTEM_ROOT': 'system-root',
      '01_NAVIGATION_CENTRE': 'navigation',
      '02_COMMAND_DECK': 'command-deck',
      '03_CORE_ENGINE': 'core-engine',
      '04_KNOWLEDGE_LIBRARY': 'knowledge-library',
      '05_TEMPLATE_HUB': 'template-hub',
      '06_DOMAIN_PILLARS': 'domain-pillars',
      '07_BUILD_FACTORY': 'build-factory',
      '08_OPERATIONS': 'operations',
    };
    const moduleId = moduleMap[topFolder] || 'system-root';

    if (result.type === 'file') {
      router.push(`/module/${moduleId}?file=${encodeURIComponent(result.path)}`);
    } else {
      router.push(`/module/${moduleId}?path=${encodeURIComponent(result.path)}`);
    }
    setIsOpen(false);
    setQuery('');
  }

  return (
    <div style={{ position: 'relative' }}>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 8,
        background: 'var(--bg-tertiary)',
        border: '1px solid var(--border-default)',
        borderRadius: 'var(--radius-md)',
        padding: '8px 14px',
      }}>
        <SearchIcon size={16} color="var(--text-tertiary)" />
        <input
          ref={inputRef}
          type="text"
          placeholder="Search files and content... (Ctrl+K)"
          value={query}
          onChange={(e) => { setQuery(e.target.value); setIsOpen(true); }}
          onFocus={() => setIsOpen(true)}
          style={{
            flex: 1,
            background: 'none',
            border: 'none',
            outline: 'none',
            fontSize: '0.875rem',
            color: 'var(--text-primary)',
          }}
        />
        {query && (
          <button
            onClick={() => { setQuery(''); setResults([]); }}
            style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 2 }}
          >
            <X size={14} color="var(--text-tertiary)" />
          </button>
        )}
        <span style={{
          fontSize: '0.7rem',
          color: 'var(--text-tertiary)',
          background: 'var(--bg-secondary)',
          padding: '2px 6px',
          borderRadius: 4,
          border: '1px solid var(--border-default)',
        }}>
          Ctrl+K
        </span>
      </div>

      {/* Results dropdown */}
      {isOpen && (query.length >= 2) && (
        <div style={{
          position: 'absolute',
          top: '100%',
          left: 0,
          right: 0,
          marginTop: 4,
          background: 'var(--bg-secondary)',
          border: '1px solid var(--border-default)',
          borderRadius: 'var(--radius-md)',
          boxShadow: 'var(--shadow-lg)',
          maxHeight: 400,
          overflowY: 'auto',
          zIndex: 50,
        }}>
          {loading ? (
            <div style={{ padding: 16, textAlign: 'center', color: 'var(--text-tertiary)', fontSize: '0.85rem' }}>
              Searching...
            </div>
          ) : results.length === 0 ? (
            <div style={{ padding: 16, textAlign: 'center', color: 'var(--text-tertiary)', fontSize: '0.85rem' }}>
              No results for &ldquo;{query}&rdquo;
            </div>
          ) : (
            results.map((result, i) => (
              <button
                key={i}
                onClick={() => handleSelect(result)}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 10,
                  width: '100%',
                  padding: '10px 14px',
                  border: 'none',
                  background: 'none',
                  cursor: 'pointer',
                  textAlign: 'left',
                  borderBottom: i < results.length - 1 ? '1px solid var(--border-subtle)' : 'none',
                }}
                onMouseOver={(e) => e.currentTarget.style.background = 'var(--bg-tertiary)'}
                onMouseOut={(e) => e.currentTarget.style.background = 'none'}
              >
                {result.type === 'directory' ? (
                  <Folder size={16} color="var(--accent-amber)" />
                ) : (
                  <File size={16} color="var(--accent-purple)" />
                )}
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{ fontSize: '0.85rem', color: 'var(--text-primary)', fontWeight: 500 }}>
                    {result.name}
                  </div>
                  <div style={{
                    fontSize: '0.75rem',
                    color: 'var(--text-tertiary)',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                  }}>
                    {result.path}
                  </div>
                </div>
              </button>
            ))
          )}
        </div>
      )}
    </div>
  );
}
