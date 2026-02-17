'use client';

import { useState } from 'react';
import { Check, X, Eye, Clock, ChevronRight, AlertCircle } from 'lucide-react';

// ============================================================
// APPROVAL QUEUE BOILERPLATE
// Used by: Staging Review (ENG_B), Content Approval,
//          Ingestion Queue (LIB_A), any screen with
//          pending items that need accept/reject/review
// Layout: Queue list + Preview + Action buttons
// ============================================================

export interface QueueItem {
  id: string;
  title: string;
  description?: string;
  source?: string;
  type?: string;
  submittedAt?: string;
  submittedBy?: string;
  priority?: 'low' | 'medium' | 'high' | 'critical';
  status?: 'pending' | 'reviewing' | 'approved' | 'rejected';
  preview?: React.ReactNode;
  meta?: Record<string, string>;
}

interface ApprovalQueueProps {
  title?: string;
  description?: string;
  items: QueueItem[];
  onApprove: (item: QueueItem) => void;
  onReject: (item: QueueItem) => void;
  onReview?: (item: QueueItem) => void;
  onBulkApprove?: (items: QueueItem[]) => void;
  onBulkReject?: (items: QueueItem[]) => void;
  stats?: { pending: number; reviewing: number; approved: number; rejected: number };
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' }[];
}

const PRIORITY_STYLES: Record<string, { bg: string; color: string; label: string }> = {
  low: { bg: 'var(--bg-tertiary)', color: 'var(--text-tertiary)', label: 'Low' },
  medium: { bg: 'var(--accent-blue-light)', color: 'var(--accent-blue)', label: 'Medium' },
  high: { bg: 'var(--accent-amber-light)', color: '#92400E', label: 'High' },
  critical: { bg: 'var(--accent-red-light)', color: 'var(--accent-red)', label: 'Critical' },
};

const STATUS_STYLES: Record<string, { bg: string; color: string; label: string }> = {
  pending: { bg: 'var(--accent-amber-light)', color: '#92400E', label: 'Pending' },
  reviewing: { bg: 'var(--accent-blue-light)', color: 'var(--accent-blue)', label: 'Reviewing' },
  approved: { bg: 'var(--accent-green-light)', color: 'var(--accent-green)', label: 'Approved' },
  rejected: { bg: 'var(--accent-red-light)', color: 'var(--accent-red)', label: 'Rejected' },
};

export default function ApprovalQueue({
  title,
  description,
  items,
  onApprove,
  onReject,
  onReview,
  onBulkApprove,
  onBulkReject,
  stats,
  actions,
}: ApprovalQueueProps) {
  const [selectedItem, setSelectedItem] = useState<QueueItem | null>(null);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [activeFilter, setActiveFilter] = useState<string>('pending');

  const filteredItems = activeFilter === 'all'
    ? items
    : items.filter((item) => item.status === activeFilter);

  const toggleSelect = (id: string) => {
    setSelectedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const toggleSelectAll = () => {
    if (selectedIds.size === filteredItems.length) {
      setSelectedIds(new Set());
    } else {
      setSelectedIds(new Set(filteredItems.map((i) => i.id)));
    }
  };

  const selectedItems = items.filter((i) => selectedIds.has(i.id));

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Queue List */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        <div style={{ padding: '20px 24px 0' }}>
          {/* Header */}
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

          {/* Stats */}
          {stats && (
            <div style={{ display: 'flex', gap: 12, marginBottom: 16 }}>
              {Object.entries(stats).map(([key, count]) => {
                const style = STATUS_STYLES[key] || STATUS_STYLES.pending;
                return (
                  <div
                    key={key}
                    onClick={() => setActiveFilter(key)}
                    style={{
                      flex: 1,
                      padding: '10px 14px',
                      borderRadius: 'var(--radius-md)',
                      background: activeFilter === key ? style.bg : 'var(--bg-card)',
                      border: `1px solid ${activeFilter === key ? style.color : 'var(--border-default)'}`,
                      cursor: 'pointer',
                      transition: 'all 0.15s',
                    }}
                  >
                    <div style={{ fontSize: 20, fontWeight: 600, color: style.color }}>{count}</div>
                    <div style={{ fontSize: 12, color: 'var(--text-tertiary)', textTransform: 'capitalize' }}>{key}</div>
                  </div>
                );
              })}
            </div>
          )}

          {/* Bulk actions */}
          {selectedIds.size > 0 && (
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                padding: '10px 16px',
                background: 'var(--accent-purple-light)',
                borderRadius: 'var(--radius-md)',
                marginBottom: 12,
              }}
            >
              <span style={{ fontSize: 13, color: 'var(--accent-purple)', fontWeight: 500 }}>
                {selectedIds.size} selected
              </span>
              <div style={{ marginLeft: 'auto', display: 'flex', gap: 8 }}>
                {onBulkApprove && (
                  <button
                    onClick={() => onBulkApprove(selectedItems)}
                    style={{ padding: '6px 14px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-green)', color: '#fff', fontSize: 12, fontWeight: 500, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                  >
                    <Check size={12} /> Approve All
                  </button>
                )}
                {onBulkReject && (
                  <button
                    onClick={() => onBulkReject(selectedItems)}
                    style={{ padding: '6px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--accent-red)', background: 'transparent', color: 'var(--accent-red)', fontSize: 12, fontWeight: 500, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 4 }}
                  >
                    <X size={12} /> Reject All
                  </button>
                )}
              </div>
            </div>
          )}

          {/* Select all checkbox */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, padding: '8px 0', borderBottom: '1px solid var(--border-default)', marginBottom: 8 }}>
            <input
              type="checkbox"
              checked={selectedIds.size === filteredItems.length && filteredItems.length > 0}
              onChange={toggleSelectAll}
              style={{ accentColor: 'var(--accent-purple)' }}
            />
            <span style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>
              {filteredItems.length} items
            </span>
          </div>
        </div>

        {/* Queue Items */}
        <div style={{ flex: 1, overflow: 'auto', padding: '0 24px 24px' }}>
          {filteredItems.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '60px 24px', color: 'var(--text-tertiary)' }}>
              <div style={{ fontSize: 16, fontWeight: 500, marginBottom: 4 }}>Queue empty</div>
              <div style={{ fontSize: 13 }}>No items matching this filter</div>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
              {filteredItems.map((item) => {
                const isSelected = selectedItem?.id === item.id;
                const priority = PRIORITY_STYLES[item.priority || 'medium'];
                const status = STATUS_STYLES[item.status || 'pending'];

                return (
                  <div
                    key={item.id}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 12,
                      padding: '12px 16px',
                      background: isSelected ? 'var(--bg-active)' : 'var(--bg-card)',
                      border: `1px solid ${isSelected ? 'var(--border-accent)' : 'var(--border-default)'}`,
                      borderRadius: 'var(--radius-md)',
                      cursor: 'pointer',
                      transition: 'all 0.15s',
                    }}
                    onClick={() => setSelectedItem(item)}
                  >
                    <input
                      type="checkbox"
                      checked={selectedIds.has(item.id)}
                      onChange={(e) => { e.stopPropagation(); toggleSelect(item.id); }}
                      style={{ accentColor: 'var(--accent-purple)', flexShrink: 0 }}
                    />
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
                        <span style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>{item.title}</span>
                        <span style={{ fontSize: 10, padding: '1px 6px', borderRadius: 'var(--radius-sm)', background: priority.bg, color: priority.color, fontWeight: 500 }}>
                          {priority.label}
                        </span>
                      </div>
                      {item.description && (
                        <div style={{ fontSize: 13, color: 'var(--text-secondary)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                          {item.description}
                        </div>
                      )}
                      <div style={{ display: 'flex', gap: 12, marginTop: 6, fontSize: 12, color: 'var(--text-tertiary)' }}>
                        {item.type && <span>{item.type}</span>}
                        {item.source && <span>via {item.source}</span>}
                        {item.submittedAt && <span><Clock size={10} style={{ marginRight: 3 }} />{item.submittedAt}</span>}
                      </div>
                    </div>
                    <div style={{ display: 'flex', gap: 6, flexShrink: 0 }}>
                      <button
                        onClick={(e) => { e.stopPropagation(); onApprove(item); }}
                        style={{ width: 32, height: 32, borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-green)', color: '#fff', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                        title="Approve"
                      >
                        <Check size={14} />
                      </button>
                      <button
                        onClick={(e) => { e.stopPropagation(); onReject(item); }}
                        style={{ width: 32, height: 32, borderRadius: 'var(--radius-md)', border: '1px solid var(--accent-red)', background: 'transparent', color: 'var(--accent-red)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                        title="Reject"
                      >
                        <X size={14} />
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>

      {/* Preview Panel */}
      {selectedItem && (
        <div
          style={{
            width: 420,
            minWidth: 420,
            borderLeft: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            overflow: 'auto',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border-subtle)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <span style={{ fontSize: 14, fontWeight: 500 }}>Review</span>
            <button onClick={() => setSelectedItem(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 4 }}>
              <X size={16} />
            </button>
          </div>
          <div style={{ flex: 1, padding: '16px 20px', overflow: 'auto' }}>
            <h3 style={{ fontSize: 16, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 16 }}>{selectedItem.title}</h3>
            {selectedItem.description && (
              <p style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: 16 }}>{selectedItem.description}</p>
            )}
            {selectedItem.meta && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 16 }}>
                {Object.entries(selectedItem.meta).map(([key, value]) => (
                  <div key={key}>
                    <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 2, textTransform: 'capitalize' }}>{key}</div>
                    <div style={{ fontSize: 14, color: 'var(--text-primary)' }}>{value}</div>
                  </div>
                ))}
              </div>
            )}
            {selectedItem.preview}
            <div style={{ display: 'flex', gap: 8, marginTop: 20 }}>
              <button
                onClick={() => onApprove(selectedItem)}
                style={{ flex: 1, padding: '10px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-green)', color: '#fff', fontSize: 13, fontWeight: 500, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}
              >
                <Check size={14} /> Approve & Promote
              </button>
              <button
                onClick={() => onReject(selectedItem)}
                style={{ flex: 1, padding: '10px', borderRadius: 'var(--radius-md)', border: '1px solid var(--accent-red)', background: 'transparent', color: 'var(--accent-red)', fontSize: 13, fontWeight: 500, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 6 }}
              >
                <X size={14} /> Reject
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
