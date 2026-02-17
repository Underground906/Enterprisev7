'use client';

import { useState } from 'react';
import { TrendingUp, TrendingDown, Minus, ChevronDown } from 'lucide-react';

// ============================================================
// DASHBOARD ANALYTICS BOILERPLATE
// Used by: Goal Health (NAV_D), RAG Quality (ENG_C),
//          Pipeline Health (LIB_E), System Health (OPS_A),
//          any screen with stat cards + charts + tables
// Layout: Stat row + Chart area + Breakdown table
// ============================================================

export interface StatItem {
  label: string;
  value: string | number;
  change?: number; // percentage, positive or negative
  color?: string;
  icon?: React.ReactNode;
}

export interface ChartConfig {
  title: string;
  type: 'bar' | 'line' | 'area' | 'donut';
  data: { label: string; value: number; color?: string }[];
  height?: number;
}

export interface BreakdownRow {
  id: string;
  cells: Record<string, React.ReactNode>;
}

export interface BreakdownColumn {
  key: string;
  label: string;
  width?: string;
}

interface DashboardAnalyticsProps {
  title?: string;
  description?: string;
  stats: StatItem[];
  charts?: ChartConfig[];
  breakdownTitle?: string;
  breakdownColumns?: BreakdownColumn[];
  breakdownData?: BreakdownRow[];
  periodOptions?: string[];
  activePeriod?: string;
  onPeriodChange?: (period: string) => void;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' }[];
  alerts?: { message: string; severity: 'info' | 'warning' | 'error' | 'success' }[];
}

function TrendBadge({ change }: { change?: number }) {
  if (change === undefined || change === 0) {
    return (
      <span style={{ display: 'inline-flex', alignItems: 'center', gap: 4, fontSize: 12, color: 'var(--text-tertiary)' }}>
        <Minus size={12} /> 0%
      </span>
    );
  }
  const isUp = change > 0;
  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: 4,
        fontSize: 12,
        fontWeight: 500,
        color: isUp ? 'var(--accent-green)' : 'var(--accent-red)',
      }}
    >
      {isUp ? <TrendingUp size={12} /> : <TrendingDown size={12} />}
      {isUp ? '+' : ''}{change}%
    </span>
  );
}

function MiniBarChart({ data, height = 200 }: { data: ChartConfig['data']; height?: number }) {
  const maxValue = Math.max(...data.map((d) => d.value), 1);

  return (
    <div style={{ display: 'flex', alignItems: 'flex-end', gap: 8, height, padding: '0 4px' }}>
      {data.map((item, i) => {
        const barHeight = (item.value / maxValue) * (height - 32);
        return (
          <div key={i} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6 }}>
            <div
              style={{
                width: '100%',
                maxWidth: 48,
                height: barHeight,
                background: item.color || 'var(--accent-purple)',
                borderRadius: '4px 4px 0 0',
                transition: 'height 0.3s ease',
                minHeight: 4,
              }}
              title={`${item.label}: ${item.value}`}
            />
            <div style={{ fontSize: 10, color: 'var(--text-tertiary)', textAlign: 'center', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: 48 }}>
              {item.label}
            </div>
          </div>
        );
      })}
    </div>
  );
}

function MiniDonutChart({ data, height = 200 }: { data: ChartConfig['data']; height?: number }) {
  const total = data.reduce((sum, d) => sum + d.value, 0);
  const size = Math.min(height, 180);
  const cx = size / 2;
  const cy = size / 2;
  const radius = size / 2 - 8;
  const innerRadius = radius * 0.6;

  let currentAngle = -90;

  const arcs = data.map((item) => {
    const percentage = total > 0 ? item.value / total : 0;
    const angle = percentage * 360;
    const startAngle = currentAngle;
    const endAngle = currentAngle + angle;
    currentAngle = endAngle;

    const startRad = (startAngle * Math.PI) / 180;
    const endRad = (endAngle * Math.PI) / 180;
    const largeArc = angle > 180 ? 1 : 0;

    const outerX1 = cx + radius * Math.cos(startRad);
    const outerY1 = cy + radius * Math.sin(startRad);
    const outerX2 = cx + radius * Math.cos(endRad);
    const outerY2 = cy + radius * Math.sin(endRad);
    const innerX1 = cx + innerRadius * Math.cos(endRad);
    const innerY1 = cy + innerRadius * Math.sin(endRad);
    const innerX2 = cx + innerRadius * Math.cos(startRad);
    const innerY2 = cy + innerRadius * Math.sin(startRad);

    const d = [
      `M ${outerX1} ${outerY1}`,
      `A ${radius} ${radius} 0 ${largeArc} 1 ${outerX2} ${outerY2}`,
      `L ${innerX1} ${innerY1}`,
      `A ${innerRadius} ${innerRadius} 0 ${largeArc} 0 ${innerX2} ${innerY2}`,
      'Z',
    ].join(' ');

    return { ...item, d, percentage };
  });

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 24 }}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        {arcs.map((arc, i) => (
          <path key={i} d={arc.d} fill={arc.color || `hsl(${i * 60}, 60%, 55%)`} />
        ))}
        <text x={cx} y={cy - 6} textAnchor="middle" style={{ fontSize: 20, fontWeight: 600, fill: 'var(--text-primary)' }}>
          {total.toLocaleString()}
        </text>
        <text x={cx} y={cy + 12} textAnchor="middle" style={{ fontSize: 11, fill: 'var(--text-tertiary)' }}>
          Total
        </text>
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
        {arcs.map((arc, i) => (
          <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13 }}>
            <div style={{ width: 10, height: 10, borderRadius: 2, background: arc.color || `hsl(${i * 60}, 60%, 55%)`, flexShrink: 0 }} />
            <span style={{ color: 'var(--text-secondary)' }}>{arc.label}</span>
            <span style={{ color: 'var(--text-tertiary)', marginLeft: 'auto' }}>{Math.round(arc.percentage * 100)}%</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function AlertBanner({ message, severity }: { message: string; severity: string }) {
  const colorMap: Record<string, { bg: string; border: string; text: string }> = {
    info: { bg: 'var(--accent-blue-light)', border: 'var(--accent-blue)', text: 'var(--accent-blue)' },
    warning: { bg: 'var(--accent-amber-light)', border: 'var(--accent-amber)', text: '#92400E' },
    error: { bg: 'var(--accent-red-light)', border: 'var(--accent-red)', text: 'var(--accent-red)' },
    success: { bg: 'var(--accent-green-light)', border: 'var(--accent-green)', text: 'var(--accent-green)' },
  };
  const c = colorMap[severity] || colorMap.info;
  return (
    <div style={{ padding: '10px 14px', borderRadius: 'var(--radius-md)', background: c.bg, border: `1px solid ${c.border}`, color: c.text, fontSize: 13 }}>
      {message}
    </div>
  );
}

export default function DashboardAnalytics({
  title,
  description,
  stats,
  charts,
  breakdownTitle,
  breakdownColumns,
  breakdownData,
  periodOptions,
  activePeriod,
  onPeriodChange,
  actions,
  alerts,
}: DashboardAnalyticsProps) {
  const [selectedPeriod, setSelectedPeriod] = useState(activePeriod || periodOptions?.[0] || '');

  const handlePeriodChange = (period: string) => {
    setSelectedPeriod(period);
    onPeriodChange?.(period);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'auto' }}>
      <div style={{ padding: '20px 24px' }}>
        {/* Header */}
        {(title || actions) && (
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
            <div>
              {title && <h2 style={{ fontSize: 18, fontWeight: 600, color: 'var(--text-primary)', margin: 0 }}>{title}</h2>}
              {description && <p style={{ fontSize: 13, color: 'var(--text-tertiary)', margin: '4px 0 0' }}>{description}</p>}
            </div>
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              {periodOptions && (
                <select
                  value={selectedPeriod}
                  onChange={(e) => handlePeriodChange(e.target.value)}
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
                  {periodOptions.map((p) => (
                    <option key={p} value={p}>{p}</option>
                  ))}
                </select>
              )}
              {actions?.map((action, i) => (
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
          </div>
        )}

        {/* Alerts */}
        {alerts && alerts.length > 0 && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 16 }}>
            {alerts.map((alert, i) => (
              <AlertBanner key={i} {...alert} />
            ))}
          </div>
        )}

        {/* Stats Row */}
        <div style={{ display: 'grid', gridTemplateColumns: `repeat(${Math.min(stats.length, 5)}, 1fr)`, gap: 12, marginBottom: 24 }}>
          {stats.map((stat, i) => (
            <div
              key={i}
              style={{
                background: 'var(--bg-card)',
                border: '1px solid var(--border-default)',
                borderRadius: 'var(--radius-lg)',
                padding: '16px 20px',
                boxShadow: 'var(--shadow-sm)',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 8 }}>
                <span style={{ fontSize: 12, color: 'var(--text-tertiary)', fontWeight: 500, textTransform: 'uppercase', letterSpacing: '0.03em' }}>
                  {stat.label}
                </span>
                {stat.icon && <span style={{ color: 'var(--text-tertiary)' }}>{stat.icon}</span>}
              </div>
              <div style={{ fontSize: 24, fontWeight: 600, color: stat.color || 'var(--text-primary)', marginBottom: 4 }}>
                {stat.value}
              </div>
              <TrendBadge change={stat.change} />
            </div>
          ))}
        </div>

        {/* Charts */}
        {charts && charts.length > 0 && (
          <div style={{ display: 'grid', gridTemplateColumns: charts.length === 1 ? '1fr' : '1fr 1fr', gap: 16, marginBottom: 24 }}>
            {charts.map((chart, i) => (
              <div
                key={i}
                style={{
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-lg)',
                  padding: '20px',
                  boxShadow: 'var(--shadow-sm)',
                }}
              >
                <h3 style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)', margin: '0 0 16px' }}>
                  {chart.title}
                </h3>
                {chart.type === 'donut' ? (
                  <MiniDonutChart data={chart.data} height={chart.height} />
                ) : (
                  <MiniBarChart data={chart.data} height={chart.height} />
                )}
              </div>
            ))}
          </div>
        )}

        {/* Breakdown Table */}
        {breakdownColumns && breakdownData && (
          <div
            style={{
              background: 'var(--bg-card)',
              border: '1px solid var(--border-default)',
              borderRadius: 'var(--radius-lg)',
              overflow: 'hidden',
              boxShadow: 'var(--shadow-sm)',
            }}
          >
            {breakdownTitle && (
              <div style={{ padding: '14px 20px', borderBottom: '1px solid var(--border-default)' }}>
                <h3 style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)', margin: 0 }}>{breakdownTitle}</h3>
              </div>
            )}
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr>
                  {breakdownColumns.map((col) => (
                    <th
                      key={col.key}
                      style={{
                        textAlign: 'left',
                        padding: '10px 16px',
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
                {breakdownData.map((row) => (
                  <tr
                    key={row.id}
                    onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--bg-card-hover)'; }}
                    onMouseLeave={(e) => { e.currentTarget.style.background = 'transparent'; }}
                  >
                    {breakdownColumns.map((col) => (
                      <td
                        key={col.key}
                        style={{
                          padding: '10px 16px',
                          fontSize: 13,
                          color: 'var(--text-secondary)',
                          borderBottom: '1px solid var(--border-subtle)',
                        }}
                      >
                        {row.cells[col.key]}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export { TrendBadge, AlertBanner };
