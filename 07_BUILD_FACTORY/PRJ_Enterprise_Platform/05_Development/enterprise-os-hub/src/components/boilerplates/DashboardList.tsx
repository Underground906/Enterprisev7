'use client';

import { useState } from 'react';
import { Search, Filter, ChevronDown, ChevronRight, MoreHorizontal, X } from 'lucide-react';

// ============================================================
// DASHBOARD LIST BOILERPLATE
// Used by: Universal Index, Session History, Ingestion Inbox,
//          Error Log, Thread Archive, Project Registry,
//          Approval Queue, User Management
// Layout: Table + Filter bar + Search + Detail Panel (right)
// ============================================================

export interface Column<T> {
  key: string;
  label: string;
  width?: string;
  render?: (item: T) => React.ReactNode;
}

export interface FilterOption {
  key: string;
  label: string;
  options: { value: string; label: string }[];
}

export interface Tab {
  key: string;
  label: string;
  count?: number;
}

interface DashboardListProps<T> {
  title?: string;
  description?: string;
  columns: Column<T>[];
  data: T[];
  getRowKey: (item: T) => string;
  tabs?: Tab[];
  activeTab?: string;
  onTabChange?: (tab: string) => void;
  filters?: FilterOption[];
  stats?: { label: string; value: string | number; color?: string }[];
  onSearch?: (query: string) => void;
  onRowClick?: (item: T) => void;
  selectedItem?: T | null;
  detailPanel?: (item: T) => React.ReactNode;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' | 'danger' }[];
  emptyState?: { title: string; description: string; action?: { label: string; onClick: () => void } };
  loading?: boolean;
}

function Badge({ children, color }: { children: React.ReactNode; color?: string }) {
  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        padding: '2px 8px',
        borderRadius: 'var(--radius-sm)',
        fontSize: 12,
        fontWeight: 500,
        background: color ? `${color}18` : 'var(--bg-tertiary)',
        color: color || 'var(--text-secondary)',
      }}
    >
      {children}
    </span>
  );
}

function StatCard({ label, value, color }: { label: string; value: string | number; color?: string }) {
  return (
    <div
      style={{
        background: 'var(--bg-card)',
        border: '1px solid var(--border-default)',
        borderRadius: 'var(--radius-md)',
        padding: '12px 16px',
        flex: 1,
        minWidth: 120,
      }}
    >
      <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>{label}</div>
      <div style={{ fontSize: 20, fontWeight: 600, color: color || 'var(--text-primary)' }}>
        {value}
      </div>
    </div>
  );
}

export default function DashboardList<T>({
  title,
  description,
  columns,
  data,
  getRowKey,
  tabs,
  activeTab,
  onTabChange,
  filters,
  stats,
  onSearch,
  onRowClick,
  selectedItem,
  detailPanel,
  actions,
  emptyState,
  loading,
}: DashboardListProps<T>) {
  const [searchQuery, setSearchQuery] = useState('');
  const [activeFilters, setActiveFilters] = useState<Record<string, string>>({});
  const [showDetail, setShowDetail] = useState(false);

  const handleRowClick = (item: T) => {
    onRowClick?.(item);
    setShowDetail(true);
  };

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Main Content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* Header */}
        <div style={{ padding: '20px 24px 0' }}>
          {/* Title Row */}
          {(title || actions) && (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
              <div>
                {title && <h2 style={{ fontSize: 18, fontWeight: 600, color: 'var(--text-primary)', margin: 0 }}>{title}</h2>}
                {description && <p style={{ fontSize: 13, color: 'var(--text-tertiary)', margin: '4px 0 0' }}>{description}</p>}
              </div>
              {actions && (
                <div style={{ display: 'flex', gap: 8 }}>
                  {actions.map((action, i) => (
                    <button
                      key={i}
                      onClick={action.onClick}
                      style={{
                        padding: '8px 16px',
                        borderRadius: 'var(--radius-md)',
                        border: action.variant === 'primary' ? 'none' : '1px solid var(--border-default)',
                        background: action.variant === 'primary' ? 'var(--accent-purple)' : action.variant === 'danger' ? 'var(--accent-red)' : 'var(--bg-secondary)',
                        color: action.variant === 'primary' || action.variant === 'danger' ? '#fff' : 'var(--text-primary)',
                        fontSize: 13,
                        fontWeight: 500,
                        cursor: 'pointer',
                      }}
                    >
                      {action.label}
                    </button>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* Stats Row */}
          {stats && stats.length > 0 && (
            <div style={{ display: 'flex', gap: 12, marginBottom: 16 }}>
              {stats.map((stat, i) => (
                <StatCard key={i} {...stat} />
              ))}
            </div>
          )}

          {/* Tabs */}
          {tabs && (
            <div
              style={{
                display: 'flex',
                gap: 0,
                borderBottom: '1px solid var(--border-default)',
                marginBottom: 16,
              }}
            >
              {tabs.map((tab) => (
                <button
                  key={tab.key}
                  onClick={() => onTabChange?.(tab.key)}
                  style={{
                    padding: '8px 16px',
                    border: 'none',
                    background: 'transparent',
                    borderBottom: activeTab === tab.key ? '2px solid var(--accent-purple)' : '2px solid transparent',
                    color: activeTab === tab.key ? 'var(--accent-purple)' : 'var(--text-secondary)',
                    fontSize: 13,
                    fontWeight: activeTab === tab.key ? 500 : 400,
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                  }}
                >
                  {tab.label}
                  {tab.count !== undefined && (
                    <span
                      style={{
                        fontSize: 11,
                        background: activeTab === tab.key ? 'var(--accent-purple-light)' : 'var(--bg-tertiary)',
                        padding: '1px 6px',
                        borderRadius: 10,
                        color: activeTab === tab.key ? 'var(--accent-purple)' : 'var(--text-tertiary)',
                      }}
                    >
                      {tab.count}
                    </span>
                  )}
                </button>
              ))}
            </div>
          )}

          {/* Search + Filters Row */}
          <div style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                padding: '7px 12px',
                border: '1px solid var(--border-default)',
                borderRadius: 'var(--radius-md)',
                background: 'var(--bg-secondary)',
                flex: 1,
                maxWidth: 360,
              }}
            >
              <Search size={14} style={{ color: 'var(--text-tertiary)', flexShrink: 0 }} />
              <input
                type="text"
                placeholder="Search..."
                value={searchQuery}
                onChange={(e) => {
                  setSearchQuery(e.target.value);
                  onSearch?.(e.target.value);
                }}
                style={{
                  border: 'none',
                  outline: 'none',
                  background: 'transparent',
                  fontSize: 13,
                  color: 'var(--text-primary)',
                  width: '100%',
                }}
              />
              {searchQuery && (
                <button
                  onClick={() => { setSearchQuery(''); onSearch?.(''); }}
                  style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 0 }}
                >
                  <X size={14} />
                </button>
              )}
            </div>

            {filters?.map((filter) => (
              <select
                key={filter.key}
                value={activeFilters[filter.key] || ''}
                onChange={(e) =>
                  setActiveFilters((prev) => ({ ...prev, [filter.key]: e.target.value }))
                }
                style={{
                  padding: '7px 12px',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-md)',
                  background: 'var(--bg-secondary)',
                  fontSize: 13,
                  color: 'var(--text-secondary)',
                  cursor: 'pointer',
                  outline: 'none',
                }}
              >
                <option value="">{filter.label}</option>
                {filter.options.map((opt) => (
                  <option key={opt.value} value={opt.value}>
                    {opt.label}
                  </option>
                ))}
              </select>
            ))}
          </div>
        </div>

        {/* Table */}
        <div style={{ flex: 1, overflow: 'auto', padding: '0 24px 24px' }}>
          {loading ? (
            // Skeleton loader
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {[...Array(8)].map((_, i) => (
                <div
                  key={i}
                  style={{
                    height: 48,
                    background: 'var(--bg-tertiary)',
                    borderRadius: 'var(--radius-md)',
                    animation: 'pulse 1.5s ease-in-out infinite',
                    opacity: 1 - i * 0.1,
                  }}
                />
              ))}
            </div>
          ) : data.length === 0 && emptyState ? (
            // Empty state
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '80px 24px',
                textAlign: 'center',
              }}
            >
              <div style={{ fontSize: 16, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 8 }}>
                {emptyState.title}
              </div>
              <div style={{ fontSize: 13, color: 'var(--text-tertiary)', marginBottom: 16 }}>
                {emptyState.description}
              </div>
              {emptyState.action && (
                <button
                  onClick={emptyState.action.onClick}
                  style={{
                    padding: '8px 20px',
                    borderRadius: 'var(--radius-md)',
                    border: 'none',
                    background: 'var(--accent-purple)',
                    color: '#fff',
                    fontSize: 13,
                    fontWeight: 500,
                    cursor: 'pointer',
                  }}
                >
                  {emptyState.action.label}
                </button>
              )}
            </div>
          ) : (
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr>
                  {columns.map((col) => (
                    <th
                      key={col.key}
                      style={{
                        textAlign: 'left',
                        padding: '10px 12px',
                        fontSize: 12,
                        fontWeight: 500,
                        color: 'var(--text-tertiary)',
                        borderBottom: '1px solid var(--border-default)',
                        width: col.width,
                        textTransform: 'uppercase',
                        letterSpacing: '0.03em',
                      }}
                    >
                      {col.label}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {data.map((item) => (
                  <tr
                    key={getRowKey(item)}
                    onClick={() => handleRowClick(item)}
                    style={{
                      cursor: onRowClick ? 'pointer' : 'default',
                      transition: 'background 0.1s',
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.background = 'var(--bg-card-hover)';
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.background = 'transparent';
                    }}
                  >
                    {columns.map((col) => (
                      <td
                        key={col.key}
                        style={{
                          padding: '10px 12px',
                          fontSize: 13,
                          color: 'var(--text-secondary)',
                          borderBottom: '1px solid var(--border-subtle)',
                        }}
                      >
                        {col.render
                          ? col.render(item)
                          : String((item as Record<string, unknown>)[col.key] ?? '')}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      </div>

      {/* Detail Panel */}
      {showDetail && selectedItem && detailPanel && (
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
            <span style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>Details</span>
            <button
              onClick={() => setShowDetail(false)}
              style={{
                border: 'none',
                background: 'transparent',
                cursor: 'pointer',
                color: 'var(--text-tertiary)',
                padding: 4,
              }}
            >
              <X size={16} />
            </button>
          </div>
          <div style={{ flex: 1, padding: '16px 20px', overflow: 'auto' }}>
            {detailPanel(selectedItem)}
          </div>
        </div>
      )}
    </div>
  );
}

export { Badge, StatCard };
