'use client';

import { useState } from 'react';
import { ChevronLeft, ChevronRight, X, Maximize2, Minimize2 } from 'lucide-react';

// ============================================================
// SPLIT VIEW BOILERPLATE
// Used by: Thread Viewer, File Comparison, Side-by-side Editor,
//          Canon Reader, any screen needing two panes
// Layout: Left pane (list/tree) + Right pane (content/preview)
// ============================================================

export interface SplitItem {
  id: string;
  title: string;
  subtitle?: string;
  icon?: React.ReactNode;
  badge?: { label: string; color?: string };
  meta?: string;
  group?: string;
}

interface SplitViewProps {
  title?: string;
  description?: string;
  items: SplitItem[];
  selectedItem?: SplitItem | null;
  onItemSelect: (item: SplitItem) => void;
  contentPanel: (item: SplitItem) => React.ReactNode;
  listWidth?: number;
  groups?: { key: string; label: string }[];
  searchable?: boolean;
  onSearch?: (query: string) => void;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' }[];
  emptyContent?: React.ReactNode;
  headerActions?: (item: SplitItem) => React.ReactNode;
}

export default function SplitView({
  title,
  description,
  items,
  selectedItem,
  onItemSelect,
  contentPanel,
  listWidth = 320,
  groups,
  searchable = true,
  onSearch,
  actions,
  emptyContent,
  headerActions,
}: SplitViewProps) {
  const [searchQuery, setSearchQuery] = useState('');
  const [collapsedGroups, setCollapsedGroups] = useState<Set<string>>(new Set());
  const [isListCollapsed, setIsListCollapsed] = useState(false);

  const handleSearch = (q: string) => {
    setSearchQuery(q);
    onSearch?.(q);
  };

  const toggleGroup = (key: string) => {
    setCollapsedGroups((prev) => {
      const next = new Set(prev);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  };

  const groupedItems = groups
    ? groups.map((g) => ({
        ...g,
        items: items.filter((item) => item.group === g.key),
      }))
    : null;

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Left Panel: Item List */}
      {!isListCollapsed && (
        <div
          style={{
            width: listWidth,
            minWidth: listWidth,
            borderRight: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            display: 'flex',
            flexDirection: 'column',
            overflow: 'hidden',
          }}
        >
          {/* List Header */}
          <div style={{ padding: '16px', borderBottom: '1px solid var(--border-default)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: searchable ? 12 : 0 }}>
              <div>
                {title && <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{title}</div>}
                {description && <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginTop: 2 }}>{description}</div>}
              </div>
              <button
                onClick={() => setIsListCollapsed(true)}
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 4 }}
                title="Collapse panel"
              >
                <ChevronLeft size={16} />
              </button>
            </div>

            {searchable && (
              <input
                type="text"
                placeholder="Search..."
                value={searchQuery}
                onChange={(e) => handleSearch(e.target.value)}
                style={{
                  width: '100%',
                  padding: '8px 12px',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-md)',
                  fontSize: 13,
                  color: 'var(--text-primary)',
                  background: 'var(--bg-primary)',
                  outline: 'none',
                  boxSizing: 'border-box',
                }}
              />
            )}
          </div>

          {/* Item List */}
          <div style={{ flex: 1, overflow: 'auto' }}>
            {groupedItems ? (
              groupedItems.map((group) => (
                <div key={group.key}>
                  <button
                    onClick={() => toggleGroup(group.key)}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      width: '100%',
                      padding: '8px 16px',
                      border: 'none',
                      background: 'var(--bg-tertiary)',
                      fontSize: 11,
                      fontWeight: 600,
                      color: 'var(--text-tertiary)',
                      cursor: 'pointer',
                      textTransform: 'uppercase',
                      letterSpacing: '0.05em',
                    }}
                  >
                    <span>{group.label} ({group.items.length})</span>
                    {collapsedGroups.has(group.key) ? <ChevronRight size={12} /> : <ChevronLeft size={12} style={{ transform: 'rotate(-90deg)' }} />}
                  </button>
                  {!collapsedGroups.has(group.key) &&
                    group.items.map((item) => (
                      <ItemRow key={item.id} item={item} isSelected={selectedItem?.id === item.id} onClick={() => onItemSelect(item)} />
                    ))}
                </div>
              ))
            ) : (
              items.map((item) => (
                <ItemRow key={item.id} item={item} isSelected={selectedItem?.id === item.id} onClick={() => onItemSelect(item)} />
              ))
            )}
          </div>

          {/* List Actions */}
          {actions && (
            <div style={{ padding: '12px 16px', borderTop: '1px solid var(--border-default)', display: 'flex', gap: 8 }}>
              {actions.map((action, i) => (
                <button
                  key={i}
                  onClick={action.onClick}
                  style={{
                    flex: 1,
                    padding: '8px',
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

      {/* Collapsed toggle */}
      {isListCollapsed && (
        <button
          onClick={() => setIsListCollapsed(false)}
          style={{
            width: 32,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            borderRight: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            border: 'none',
            borderRightStyle: 'solid',
            borderRightWidth: 1,
            borderRightColor: 'var(--border-default)',
            cursor: 'pointer',
            color: 'var(--text-tertiary)',
          }}
          title="Expand panel"
        >
          <ChevronRight size={16} />
        </button>
      )}

      {/* Right Panel: Content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {selectedItem ? (
          <>
            {/* Content Header */}
            <div
              style={{
                padding: '14px 24px',
                borderBottom: '1px solid var(--border-default)',
                background: 'var(--bg-secondary)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                {selectedItem.icon}
                <div>
                  <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{selectedItem.title}</div>
                  {selectedItem.subtitle && (
                    <div style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>{selectedItem.subtitle}</div>
                  )}
                </div>
              </div>
              {headerActions && headerActions(selectedItem)}
            </div>

            {/* Content Body */}
            <div style={{ flex: 1, overflow: 'auto', padding: '24px' }}>
              {contentPanel(selectedItem)}
            </div>
          </>
        ) : (
          <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            {emptyContent || (
              <div style={{ textAlign: 'center', color: 'var(--text-tertiary)' }}>
                <div style={{ fontSize: 16, fontWeight: 500, marginBottom: 4 }}>Select an item</div>
                <div style={{ fontSize: 13 }}>Choose from the list to view details</div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

function ItemRow({ item, isSelected, onClick }: { item: SplitItem; isSelected: boolean; onClick: () => void }) {
  return (
    <div
      onClick={onClick}
      style={{
        padding: '10px 16px',
        cursor: 'pointer',
        background: isSelected ? 'var(--bg-active)' : 'transparent',
        borderLeft: isSelected ? '3px solid var(--accent-purple)' : '3px solid transparent',
        transition: 'background 0.1s',
        display: 'flex',
        alignItems: 'center',
        gap: 10,
      }}
      onMouseEnter={(e) => {
        if (!isSelected) e.currentTarget.style.background = 'var(--bg-card-hover)';
      }}
      onMouseLeave={(e) => {
        if (!isSelected) e.currentTarget.style.background = 'transparent';
      }}
    >
      {item.icon && <span style={{ flexShrink: 0 }}>{item.icon}</span>}
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={{ fontSize: 13, fontWeight: isSelected ? 500 : 400, color: 'var(--text-primary)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {item.title}
        </div>
        {item.subtitle && (
          <div style={{ fontSize: 12, color: 'var(--text-tertiary)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
            {item.subtitle}
          </div>
        )}
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 4, flexShrink: 0 }}>
        {item.badge && (
          <span
            style={{
              fontSize: 10,
              padding: '1px 6px',
              borderRadius: 'var(--radius-sm)',
              background: item.badge.color ? `${item.badge.color}18` : 'var(--bg-tertiary)',
              color: item.badge.color || 'var(--text-tertiary)',
              fontWeight: 500,
            }}
          >
            {item.badge.label}
          </span>
        )}
        {item.meta && <span style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>{item.meta}</span>}
      </div>
    </div>
  );
}
