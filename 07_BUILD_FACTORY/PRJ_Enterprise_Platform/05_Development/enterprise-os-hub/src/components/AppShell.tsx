'use client';

import { useState } from 'react';
import {
  Search, ChevronLeft, ChevronRight, ChevronDown,
  Compass, FolderOpen, Heart, Zap, Grid3X3,
  Brain, Terminal, Cpu, BookOpen, Dna,
  Layers, Hammer, Activity
} from 'lucide-react';

// ============================================================
// APP SHELL — Matched to Brainwave 2.0 sidebar + topbar
// From: pre_made_templates_my_scenes.png, topbar_topbar.png
//
// Sidebar: white bg, logo top-left, search bar with ⌘K,
//   tree nav with icons, section labels, expand/collapse,
//   count badges. ~200px wide.
// Topbar: back/forward arrows, search, utility icons, avatar.
//   Merges with sidebar header row.
// ============================================================

interface NavItem {
  id: string;
  label: string;
  icon: React.ReactNode;
  href: string;
  children?: { id: string; label: string; href: string }[];
  count?: number;
}

interface NavSection {
  label?: string;
  items: NavItem[];
}

const NAV_SECTIONS: NavSection[] = [
  {
    items: [
      {
        id: 'explore',
        label: 'Explore',
        icon: <Compass size={18} />,
        href: '/',
        children: [
          { id: 'nav-goals', label: 'Goals', href: '/nav/health' },
          { id: 'nav-intake', label: 'Goal Intake', href: '/nav/intake' },
        ],
      },
    ],
  },
  {
    items: [
      { id: 'engine', label: 'Engine', icon: <Cpu size={18} />, href: '/engine/index', count: 2847 },
      { id: 'library', label: 'Library', icon: <BookOpen size={18} />, href: '/lib/search' },
    ],
  },
  {
    label: 'Command Deck',
    items: [
      { id: 'concierge', label: 'AI Concierge', icon: <Zap size={18} />, href: '/cmd/chat' },
      { id: 'agents', label: 'Agents', icon: <Brain size={18} />, href: '/cmd/agents' },
      { id: 'sessions', label: 'Sessions', icon: <Terminal size={18} />, href: '/cmd/sessions' },
    ],
  },
  {
    label: 'System',
    items: [
      { id: 'staging', label: 'Staging Review', icon: <Layers size={18} />, href: '/engine/staging' },
      { id: 'threads', label: 'Threads', icon: <FolderOpen size={18} />, href: '/lib/threads' },
      { id: 'settings', label: 'Settings', icon: <Grid3X3 size={18} />, href: '/sys/settings' },
    ],
  },
];

function SidebarItem({
  item,
  collapsed,
  expandedIds,
  onToggle,
}: {
  item: NavItem;
  collapsed: boolean;
  expandedIds: Set<string>;
  onToggle: (id: string) => void;
}) {
  const isExpanded = expandedIds.has(item.id);
  const hasChildren = item.children && item.children.length > 0;

  return (
    <>
      <a
        href={item.href}
        onClick={(e) => {
          if (hasChildren) {
            e.preventDefault();
            onToggle(item.id);
          }
        }}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          padding: collapsed ? '7px 0' : '7px 12px',
          borderRadius: 10,
          color: 'var(--text-secondary)',
          textDecoration: 'none',
          fontSize: 14,
          fontWeight: 400,
          letterSpacing: '-0.01em',
          justifyContent: collapsed ? 'center' : 'flex-start',
          cursor: 'pointer',
          transition: 'background 0.1s',
        }}
        onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--shade-3)'; }}
        onMouseLeave={(e) => { e.currentTarget.style.background = 'transparent'; }}
      >
        <span style={{ color: 'var(--shade-6)', flexShrink: 0, display: 'flex' }}>{item.icon}</span>
        {!collapsed && (
          <>
            <span style={{ flex: 1 }}>{item.label}</span>
            {item.count !== undefined && (
              <span style={{
                fontSize: 11,
                fontWeight: 500,
                color: 'var(--shade-6)',
                background: 'var(--shade-3)',
                padding: '1px 8px',
                borderRadius: 10,
              }}>
                {item.count > 999 ? `${(item.count / 1000).toFixed(0)}k` : item.count}
              </span>
            )}
            {hasChildren && (
              <ChevronDown
                size={14}
                style={{
                  color: 'var(--shade-6)',
                  transform: isExpanded ? 'rotate(0deg)' : 'rotate(-90deg)',
                  transition: 'transform 0.15s',
                }}
              />
            )}
          </>
        )}
      </a>
      {/* Children */}
      {hasChildren && isExpanded && !collapsed && (
        <div style={{ paddingLeft: 28, display: 'flex', flexDirection: 'column', gap: 1 }}>
          {item.children!.map((child) => (
            <a
              key={child.id}
              href={child.href}
              style={{
                display: 'block',
                padding: '5px 12px',
                borderRadius: 8,
                color: 'var(--shade-6)',
                textDecoration: 'none',
                fontSize: 13,
                letterSpacing: '-0.01em',
                transition: 'background 0.1s, color 0.1s',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.background = 'var(--shade-3)';
                e.currentTarget.style.color = 'var(--shade-7)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.background = 'transparent';
                e.currentTarget.style.color = 'var(--shade-6)';
              }}
            >
              {child.label}
            </a>
          ))}
        </div>
      )}
    </>
  );
}

export default function AppShell({
  children,
}: {
  children: React.ReactNode;
}) {
  const [collapsed, setCollapsed] = useState(false);
  const [expandedIds, setExpandedIds] = useState<Set<string>>(new Set(['explore']));

  const toggleExpand = (id: string) => {
    setExpandedIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  return (
    <div style={{ display: 'flex', height: '100vh', overflow: 'hidden' }}>
      {/* Sidebar — Brainwave style */}
      <aside
        style={{
          width: collapsed ? 56 : 'var(--sidebar-width)',
          minWidth: collapsed ? 56 : 'var(--sidebar-width)',
          background: 'var(--bg-sidebar)',
          borderRight: '1px solid var(--border-subtle)',
          display: 'flex',
          flexDirection: 'column',
          transition: 'width 0.2s, min-width 0.2s',
          overflow: 'hidden',
        }}
      >
        {/* Logo row — matches Brainwave: green icon + "Enterprise OS" */}
        <div
          style={{
            padding: collapsed ? '16px 12px' : '16px 16px',
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            justifyContent: collapsed ? 'center' : 'flex-start',
          }}
        >
          {/* Green swirl icon placeholder — using "E" for now */}
          <div
            style={{
              width: 28,
              height: 28,
              borderRadius: 8,
              background: 'var(--accent-green-bw)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#fff',
              fontWeight: 700,
              fontSize: 14,
              flexShrink: 0,
            }}
          >
            E
          </div>
          {!collapsed && (
            <span style={{ fontWeight: 600, fontSize: 15, color: 'var(--text-primary)', letterSpacing: '-0.02em' }}>
              Enterprise OS
            </span>
          )}
        </div>

        {/* Search bar — Brainwave style: gray bg, ⌘K badge */}
        {!collapsed && (
          <div style={{ padding: '0 12px 12px' }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 8,
                padding: '7px 10px',
                borderRadius: 8,
                background: 'var(--shade-2)',
                border: '1px solid var(--shade-4)',
                cursor: 'pointer',
              }}
            >
              <Search size={14} style={{ color: 'var(--shade-6)' }} />
              <span style={{ flex: 1, fontSize: 13, color: 'var(--shade-6)', letterSpacing: '-0.01em' }}>Search files...</span>
              <span style={{
                fontSize: 11,
                color: 'var(--shade-6)',
                background: 'var(--shade-3)',
                padding: '1px 5px',
                borderRadius: 4,
                fontWeight: 500,
              }}>
                ⌘K
              </span>
            </div>
          </div>
        )}

        {/* Navigation — Brainwave tree style */}
        <nav style={{ flex: 1, overflow: 'auto', padding: collapsed ? '4px 8px' : '4px 8px' }}>
          {NAV_SECTIONS.map((section, si) => (
            <div key={si} style={{ marginBottom: 8 }}>
              {/* Section label */}
              {section.label && !collapsed && (
                <div style={{
                  padding: '8px 12px 4px',
                  fontSize: 11,
                  fontWeight: 500,
                  color: 'var(--shade-6)',
                  letterSpacing: '-0.01em',
                  textTransform: 'none',
                }}>
                  {section.label}
                </div>
              )}
              {section.items.map((item) => (
                <SidebarItem
                  key={item.id}
                  item={item}
                  collapsed={collapsed}
                  expandedIds={expandedIds}
                  onToggle={toggleExpand}
                />
              ))}
            </div>
          ))}
        </nav>

        {/* Collapse toggle */}
        <button
          onClick={() => setCollapsed(!collapsed)}
          style={{
            padding: '10px',
            border: 'none',
            borderTop: '1px solid var(--border-subtle)',
            background: 'transparent',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: 'var(--shade-6)',
          }}
        >
          {collapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
        </button>
      </aside>

      {/* Main area */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* Topbar — Brainwave style: back/forward, sparse, avatar right */}
        <header
          style={{
            height: 'var(--topbar-height)',
            borderBottom: '1px solid var(--border-subtle)',
            background: 'var(--bg-primary)',
            display: 'flex',
            alignItems: 'center',
            padding: '0 20px',
            gap: 8,
            flexShrink: 0,
          }}
        >
          {/* Back/Forward — Brainwave style */}
          <button style={{ padding: 6, border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--shade-6)', display: 'flex' }}>
            <ChevronLeft size={18} />
          </button>
          <button style={{ padding: 6, border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--shade-6)', display: 'flex' }}>
            <ChevronRight size={18} />
          </button>

          <div style={{ flex: 1 }} />

          {/* Sparkle/lightning icon — Brainwave top-right utility */}
          <button style={{ padding: 6, border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--shade-7)', display: 'flex' }}>
            <Zap size={18} />
          </button>

          {/* Create button — Brainwave dark button */}
          <button
            style={{
              padding: '7px 20px',
              borderRadius: 'var(--radius-full)',
              border: '1px solid var(--shade-5)',
              background: 'var(--bg-primary)',
              color: 'var(--text-primary)',
              fontSize: 13,
              fontWeight: 500,
              cursor: 'pointer',
              letterSpacing: '-0.01em',
            }}
          >
            Create
          </button>

          {/* User Avatar — Brainwave circular with image/color */}
          <div
            style={{
              width: 34,
              height: 34,
              borderRadius: '50%',
              background: 'var(--bw-orange)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#fff',
              fontSize: 14,
              fontWeight: 600,
              cursor: 'pointer',
            }}
          >
            J
          </div>
        </header>

        {/* Page content */}
        <main style={{ flex: 1, overflow: 'auto', background: 'var(--bg-primary)' }}>
          {children}
        </main>
      </div>
    </div>
  );
}
