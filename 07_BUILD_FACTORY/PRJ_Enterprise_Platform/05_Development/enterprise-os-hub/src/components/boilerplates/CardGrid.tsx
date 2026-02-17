'use client';

import { useState } from 'react';
import { Search, X, Star } from 'lucide-react';

// ============================================================
// CARD GRID BOILERPLATE
// Used by: Agent Registry, Template Catalogue, Pillar Grid,
//          Schema Library, plus any searchable catalogue screen
// Layout: Search + Category Tabs + Card Grid + Detail Panel
// ============================================================

export interface CardItem {
  id: string;
  title: string;
  description?: string;
  category?: string;
  icon?: React.ReactNode;
  badges?: { label: string; color?: string }[];
  meta?: string;
  starred?: boolean;
}

export interface CardGridTab {
  key: string;
  label: string;
  count?: number;
}

interface CardGridProps {
  title?: string;
  description?: string;
  items: CardItem[];
  tabs?: CardGridTab[];
  activeTab?: string;
  onTabChange?: (tab: string) => void;
  onSearch?: (query: string) => void;
  onItemClick?: (item: CardItem) => void;
  onStar?: (item: CardItem) => void;
  selectedItem?: CardItem | null;
  detailPanel?: (item: CardItem) => React.ReactNode;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' }[];
  columns?: 2 | 3 | 4;
  emptyState?: { title: string; description: string };
  loading?: boolean;
  featuredSection?: { title: string; items: CardItem[] };
}

export default function CardGrid({
  title,
  description,
  items,
  tabs,
  activeTab,
  onTabChange,
  onSearch,
  onItemClick,
  onStar,
  selectedItem,
  detailPanel,
  actions,
  columns = 3,
  emptyState,
  loading,
  featuredSection,
}: CardGridProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [showDetail, setShowDetail] = useState(false);

  const handleItemClick = (item: CardItem) => {
    onItemClick?.(item);
    setShowDetail(true);
  };

  const gridTemplateColumns = {
    2: 'repeat(auto-fill, minmax(320px, 1fr))',
    3: 'repeat(auto-fill, minmax(280px, 1fr))',
    4: 'repeat(auto-fill, minmax(240px, 1fr))',
  };

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Main Content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
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
                        background: action.variant === 'primary' ? 'var(--accent-purple)' : 'var(--bg-secondary)',
                        color: action.variant === 'primary' ? '#fff' : 'var(--text-primary)',
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

          {/* Search */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 8,
              padding: '8px 12px',
              border: '1px solid var(--border-default)',
              borderRadius: 'var(--radius-md)',
              background: 'var(--bg-secondary)',
              marginBottom: 16,
              maxWidth: 400,
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
                      }}
                    >
                      {tab.count}
                    </span>
                  )}
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Grid */}
        <div style={{ flex: 1, overflow: 'auto', padding: '0 24px 24px' }}>
          {loading ? (
            <div style={{ display: 'grid', gridTemplateColumns: gridTemplateColumns[columns], gap: 16 }}>
              {[...Array(9)].map((_, i) => (
                <div
                  key={i}
                  style={{
                    height: 160,
                    background: 'var(--bg-tertiary)',
                    borderRadius: 'var(--radius-lg)',
                    opacity: 1 - i * 0.08,
                  }}
                />
              ))}
            </div>
          ) : items.length === 0 && emptyState ? (
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
              <div style={{ fontSize: 13, color: 'var(--text-tertiary)' }}>{emptyState.description}</div>
            </div>
          ) : (
            <>
              {/* Featured Section */}
              {featuredSection && featuredSection.items.length > 0 && (
                <div style={{ marginBottom: 24 }}>
                  <h3 style={{ fontSize: 13, fontWeight: 500, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: 12 }}>
                    {featuredSection.title}
                  </h3>
                  <div style={{ display: 'flex', gap: 12, overflowX: 'auto', paddingBottom: 4 }}>
                    {featuredSection.items.map((item) => (
                      <div
                        key={item.id}
                        onClick={() => handleItemClick(item)}
                        style={{
                          minWidth: 200,
                          padding: '12px 16px',
                          background: 'var(--bg-card)',
                          border: '1px solid var(--border-default)',
                          borderRadius: 'var(--radius-md)',
                          cursor: 'pointer',
                          transition: 'border-color 0.15s, box-shadow 0.15s',
                        }}
                        onMouseEnter={(e) => {
                          e.currentTarget.style.borderColor = 'var(--border-accent)';
                          e.currentTarget.style.boxShadow = 'var(--shadow-md)';
                        }}
                        onMouseLeave={(e) => {
                          e.currentTarget.style.borderColor = 'var(--border-default)';
                          e.currentTarget.style.boxShadow = 'none';
                        }}
                      >
                        <div style={{ fontSize: 13, fontWeight: 500, color: 'var(--text-primary)' }}>{item.title}</div>
                        {item.meta && <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginTop: 4 }}>{item.meta}</div>}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Main Grid */}
              <div style={{ display: 'grid', gridTemplateColumns: gridTemplateColumns[columns], gap: 16 }}>
                {items.map((item) => {
                  const isSelected = selectedItem?.id === item.id;
                  return (
                    <div
                      key={item.id}
                      onClick={() => handleItemClick(item)}
                      style={{
                        background: 'var(--bg-card)',
                        border: `1px solid ${isSelected ? 'var(--border-accent)' : 'var(--border-default)'}`,
                        borderRadius: 'var(--radius-lg)',
                        padding: '16px',
                        cursor: 'pointer',
                        transition: 'border-color 0.15s, box-shadow 0.15s, transform 0.15s',
                        boxShadow: isSelected ? 'var(--shadow-md)' : 'var(--shadow-sm)',
                      }}
                      onMouseEnter={(e) => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--border-accent)';
                          e.currentTarget.style.boxShadow = 'var(--shadow-md)';
                          e.currentTarget.style.transform = 'translateY(-1px)';
                        }
                      }}
                      onMouseLeave={(e) => {
                        if (!isSelected) {
                          e.currentTarget.style.borderColor = 'var(--border-default)';
                          e.currentTarget.style.boxShadow = 'var(--shadow-sm)';
                          e.currentTarget.style.transform = 'none';
                        }
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', marginBottom: 8 }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                          {item.icon && (
                            <div
                              style={{
                                width: 40,
                                height: 40,
                                borderRadius: 'var(--radius-md)',
                                background: 'var(--bg-tertiary)',
                                display: 'flex',
                                alignItems: 'center',
                                justifyContent: 'center',
                                flexShrink: 0,
                              }}
                            >
                              {item.icon}
                            </div>
                          )}
                          <div>
                            <div style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>{item.title}</div>
                            {item.category && (
                              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginTop: 2 }}>{item.category}</div>
                            )}
                          </div>
                        </div>
                        {onStar && (
                          <button
                            onClick={(e) => { e.stopPropagation(); onStar(item); }}
                            style={{
                              border: 'none',
                              background: 'transparent',
                              cursor: 'pointer',
                              color: item.starred ? 'var(--accent-amber)' : 'var(--text-tertiary)',
                              padding: 2,
                            }}
                          >
                            <Star size={14} fill={item.starred ? 'var(--accent-amber)' : 'none'} />
                          </button>
                        )}
                      </div>

                      {item.description && (
                        <p style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.5, margin: '0 0 10px' }}>
                          {item.description}
                        </p>
                      )}

                      {item.badges && item.badges.length > 0 && (
                        <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                          {item.badges.map((badge, i) => (
                            <span
                              key={i}
                              style={{
                                fontSize: 11,
                                padding: '2px 8px',
                                borderRadius: 'var(--radius-sm)',
                                background: badge.color ? `${badge.color}18` : 'var(--bg-tertiary)',
                                color: badge.color || 'var(--text-tertiary)',
                                fontWeight: 500,
                              }}
                            >
                              {badge.label}
                            </span>
                          ))}
                        </div>
                      )}

                      {item.meta && !item.category && (
                        <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginTop: 8 }}>{item.meta}</div>
                      )}
                    </div>
                  );
                })}
              </div>
            </>
          )}
        </div>
      </div>

      {/* Detail Panel */}
      {showDetail && selectedItem && detailPanel && (
        <div
          style={{
            width: 380,
            minWidth: 380,
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
            <span style={{ fontSize: 14, fontWeight: 500 }}>Details</span>
            <button
              onClick={() => setShowDetail(false)}
              style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 4 }}
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
