'use client';

import { useState } from 'react';

// ============================================================
// TIMELINE BOILERPLATE
// Used by: Session History (CMD_C), Activity Log, Build Log,
//          any screen showing chronological events
// Layout: Filter bar + Vertical timeline + Detail panel
// ============================================================

export interface TimelineEvent {
  id: string;
  title: string;
  description?: string;
  timestamp: string;
  type?: string;
  icon?: React.ReactNode;
  color?: string;
  user?: string;
  tags?: string[];
  detail?: React.ReactNode;
}

interface TimelineProps {
  title?: string;
  description?: string;
  events: TimelineEvent[];
  groupBy?: 'day' | 'none';
  typeFilters?: { key: string; label: string; color?: string }[];
  onEventClick?: (event: TimelineEvent) => void;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' }[];
  emptyState?: { title: string; description: string };
}

function formatDateGroup(dateStr: string): string {
  const date = new Date(dateStr);
  const today = new Date();
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);

  if (date.toDateString() === today.toDateString()) return 'Today';
  if (date.toDateString() === yesterday.toDateString()) return 'Yesterday';
  return date.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' });
}

export default function Timeline({
  title,
  description,
  events,
  groupBy = 'day',
  typeFilters,
  onEventClick,
  actions,
  emptyState,
}: TimelineProps) {
  const [activeFilter, setActiveFilter] = useState<string>('all');
  const [selectedEvent, setSelectedEvent] = useState<TimelineEvent | null>(null);

  const filteredEvents = activeFilter === 'all'
    ? events
    : events.filter((e) => e.type === activeFilter);

  // Group events by day
  const grouped = groupBy === 'day'
    ? filteredEvents.reduce<Record<string, TimelineEvent[]>>((acc, event) => {
        const dateKey = event.timestamp.split('T')[0] || event.timestamp.split(' ')[0] || 'Unknown';
        if (!acc[dateKey]) acc[dateKey] = [];
        acc[dateKey].push(event);
        return acc;
      }, {})
    : { all: filteredEvents };

  const handleEventClick = (event: TimelineEvent) => {
    setSelectedEvent(event);
    onEventClick?.(event);
  };

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Main Timeline */}
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

          {/* Type Filters */}
          {typeFilters && (
            <div style={{ display: 'flex', gap: 8, marginBottom: 16, flexWrap: 'wrap' }}>
              <button
                onClick={() => setActiveFilter('all')}
                style={{
                  padding: '6px 14px',
                  borderRadius: 20,
                  border: `1px solid ${activeFilter === 'all' ? 'var(--accent-purple)' : 'var(--border-default)'}`,
                  background: activeFilter === 'all' ? 'var(--accent-purple-light)' : 'var(--bg-card)',
                  color: activeFilter === 'all' ? 'var(--accent-purple)' : 'var(--text-secondary)',
                  fontSize: 12,
                  fontWeight: 500,
                  cursor: 'pointer',
                }}
              >
                All
              </button>
              {typeFilters.map((filter) => (
                <button
                  key={filter.key}
                  onClick={() => setActiveFilter(filter.key)}
                  style={{
                    padding: '6px 14px',
                    borderRadius: 20,
                    border: `1px solid ${activeFilter === filter.key ? (filter.color || 'var(--accent-purple)') : 'var(--border-default)'}`,
                    background: activeFilter === filter.key ? `${filter.color || 'var(--accent-purple)'}18` : 'var(--bg-card)',
                    color: activeFilter === filter.key ? (filter.color || 'var(--accent-purple)') : 'var(--text-secondary)',
                    fontSize: 12,
                    fontWeight: 500,
                    cursor: 'pointer',
                  }}
                >
                  {filter.label}
                </button>
              ))}
            </div>
          )}
        </div>

        {/* Timeline Content */}
        <div style={{ flex: 1, overflow: 'auto', padding: '0 24px 24px' }}>
          {filteredEvents.length === 0 && emptyState ? (
            <div style={{ textAlign: 'center', padding: '60px 24px' }}>
              <div style={{ fontSize: 16, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 8 }}>{emptyState.title}</div>
              <div style={{ fontSize: 13, color: 'var(--text-tertiary)' }}>{emptyState.description}</div>
            </div>
          ) : (
            Object.entries(grouped).map(([dateKey, dayEvents]) => (
              <div key={dateKey} style={{ marginBottom: 24 }}>
                {groupBy === 'day' && (
                  <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-tertiary)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: 12, paddingLeft: 28 }}>
                    {formatDateGroup(dateKey)}
                  </div>
                )}
                <div style={{ position: 'relative', paddingLeft: 28 }}>
                  {/* Vertical line */}
                  <div style={{ position: 'absolute', left: 7, top: 0, bottom: 0, width: 2, background: 'var(--border-default)' }} />

                  {dayEvents.map((event, i) => {
                    const isSelected = selectedEvent?.id === event.id;
                    return (
                      <div
                        key={event.id}
                        onClick={() => handleEventClick(event)}
                        style={{
                          position: 'relative',
                          padding: '10px 16px',
                          marginBottom: 8,
                          background: isSelected ? 'var(--bg-active)' : 'var(--bg-card)',
                          border: `1px solid ${isSelected ? 'var(--border-accent)' : 'var(--border-default)'}`,
                          borderRadius: 'var(--radius-md)',
                          cursor: 'pointer',
                          transition: 'all 0.15s',
                        }}
                        onMouseEnter={(e) => { if (!isSelected) e.currentTarget.style.borderColor = 'var(--border-accent)'; }}
                        onMouseLeave={(e) => { if (!isSelected) e.currentTarget.style.borderColor = 'var(--border-default)'; }}
                      >
                        {/* Dot */}
                        <div
                          style={{
                            position: 'absolute',
                            left: -25,
                            top: 14,
                            width: 12,
                            height: 12,
                            borderRadius: '50%',
                            background: event.color || 'var(--accent-purple)',
                            border: '2px solid var(--bg-primary)',
                            zIndex: 1,
                          }}
                        />

                        <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between' }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            {event.icon}
                            <span style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>{event.title}</span>
                          </div>
                          <span style={{ fontSize: 11, color: 'var(--text-tertiary)', flexShrink: 0 }}>
                            {event.timestamp.includes('T') ? event.timestamp.split('T')[1]?.substring(0, 5) : event.timestamp}
                          </span>
                        </div>

                        {event.description && (
                          <p style={{ fontSize: 13, color: 'var(--text-secondary)', margin: '6px 0 0', lineHeight: 1.5 }}>
                            {event.description}
                          </p>
                        )}

                        {(event.type || event.user || event.tags) && (
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 8 }}>
                            {event.type && (
                              <span style={{ fontSize: 11, padding: '1px 8px', borderRadius: 'var(--radius-sm)', background: `${event.color || 'var(--accent-purple)'}18`, color: event.color || 'var(--accent-purple)', fontWeight: 500 }}>
                                {event.type}
                              </span>
                            )}
                            {event.user && (
                              <span style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>by {event.user}</span>
                            )}
                            {event.tags?.map((tag) => (
                              <span key={tag} style={{ fontSize: 10, padding: '1px 6px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-tertiary)', color: 'var(--text-tertiary)' }}>
                                {tag}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      {/* Detail Panel */}
      {selectedEvent && selectedEvent.detail && (
        <div
          style={{
            width: 380,
            minWidth: 380,
            borderLeft: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            overflow: 'auto',
            padding: '20px',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
            <span style={{ fontSize: 14, fontWeight: 500 }}>Event Detail</span>
            <button onClick={() => setSelectedEvent(null)} style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 4, fontSize: 18 }}>
              &times;
            </button>
          </div>
          {selectedEvent.detail}
        </div>
      )}
    </div>
  );
}
