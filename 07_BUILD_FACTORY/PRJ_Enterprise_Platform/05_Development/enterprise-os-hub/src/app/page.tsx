import { MODULES } from '@/lib/constants';
import { getDirectoryStats } from '@/lib/files';
import Link from 'next/link';
import { Search } from '@/components/Search';
import {
  Shield, Brain, Terminal, Cpu, BookOpen,
  Dna, Layers, Hammer, Activity
} from 'lucide-react';

const ICONS: Record<string, React.ElementType> = {
  Shield, Brain, Terminal, Cpu, BookOpen, Dna, Layers, Hammer, Activity,
};

export const dynamic = 'force-dynamic';

export default function Home() {
  // Get live stats for each module
  const moduleStats = MODULES.map(mod => ({
    ...mod,
    stats: getDirectoryStats(mod.folder),
  }));

  return (
    <div style={{ minHeight: '100vh', background: 'var(--bg-primary)' }}>
      {/* Header */}
      <header style={{
        background: 'var(--bg-secondary)',
        borderBottom: '1px solid var(--border-default)',
        padding: '24px 40px',
      }}>
        <div style={{ maxWidth: 1400, margin: '0 auto' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 20 }}>
            <div>
              <h1 style={{
                fontSize: '1.5rem',
                fontWeight: 700,
                color: 'var(--text-primary)',
                letterSpacing: '-0.02em',
              }}>
                Enterprise OS
              </h1>
              <p style={{ fontSize: '0.875rem', color: 'var(--text-tertiary)', marginTop: 2 }}>
                Knowledge Architecture &amp; Business Operating System
              </p>
            </div>
            <div style={{
              display: 'flex',
              gap: 12,
              alignItems: 'center',
              fontSize: '0.8rem',
              color: 'var(--text-tertiary)',
            }}>
              <span>V7.0</span>
              <span style={{ color: 'var(--border-default)' }}>|</span>
              <span>{new Date().toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })}</span>
            </div>
          </div>

          {/* Search */}
          <Search />
        </div>
      </header>

      {/* Module Grid */}
      <main style={{ maxWidth: 1400, margin: '0 auto', padding: '32px 40px' }}>
        <h2 style={{
          fontSize: '0.75rem',
          fontWeight: 600,
          textTransform: 'uppercase',
          letterSpacing: '0.05em',
          color: 'var(--text-tertiary)',
          marginBottom: 16,
        }}>
          System Components
        </h2>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
          gap: 16,
        }}>
          {moduleStats.map((mod) => {
            const Icon = ICONS[mod.icon] || Layers;

            return (
              <Link
                key={mod.id}
                href={`/module/${mod.id}`}
                style={{ textDecoration: 'none', color: 'inherit' }}
              >
                <div
                  style={{
                    background: 'var(--bg-secondary)',
                    border: '1px solid var(--border-default)',
                    borderRadius: 'var(--radius-lg)',
                    padding: 24,
                    cursor: 'pointer',
                    transition: 'all 0.15s ease',
                    position: 'relative',
                    overflow: 'hidden',
                  }}
                  className="module-card"
                >
                  {/* Color accent bar */}
                  <div style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    right: 0,
                    height: 3,
                    background: mod.color,
                  }} />

                  <div style={{ display: 'flex', alignItems: 'flex-start', gap: 16 }}>
                    {/* Icon */}
                    <div style={{
                      width: 44,
                      height: 44,
                      borderRadius: 'var(--radius-md)',
                      background: `${mod.color}12`,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      flexShrink: 0,
                    }}>
                      <Icon size={22} color={mod.color} />
                    </div>

                    <div style={{ flex: 1, minWidth: 0 }}>
                      {/* Module name + number */}
                      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                        <span style={{
                          fontSize: '0.7rem',
                          fontWeight: 600,
                          color: mod.color,
                          background: `${mod.color}12`,
                          padding: '2px 6px',
                          borderRadius: 4,
                        }}>
                          {mod.number}
                        </span>
                        <h3 style={{
                          fontSize: '1rem',
                          fontWeight: 600,
                          color: 'var(--text-primary)',
                        }}>
                          {mod.name}
                        </h3>
                      </div>

                      {/* Organ + description */}
                      <p style={{
                        fontSize: '0.8rem',
                        color: 'var(--text-tertiary)',
                        marginBottom: 12,
                      }}>
                        <span style={{ fontStyle: 'italic' }}>{mod.organ}</span>
                        {' — '}
                        {mod.description}
                      </p>

                      {/* Stats */}
                      <div style={{
                        display: 'flex',
                        gap: 16,
                        fontSize: '0.75rem',
                        color: 'var(--text-tertiary)',
                      }}>
                        <span>
                          <strong style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>
                            {mod.stats.totalFiles}
                          </strong>{' '}files
                        </span>
                        <span>
                          <strong style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>
                            {mod.stats.totalDirs}
                          </strong>{' '}folders
                        </span>
                        {mod.stats.byExtension['.md'] && (
                          <span>
                            <strong style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>
                              {mod.stats.byExtension['.md']}
                            </strong>{' '}docs
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </main>

      <style>{`
        .module-card:hover {
          border-color: var(--border-accent) !important;
          box-shadow: var(--shadow-md) !important;
          transform: translateY(-1px);
        }
      `}</style>
    </div>
  );
}
