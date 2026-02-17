'use client';

import { useState } from 'react';
import { FileText, MessageSquare, Zap, BookOpen, Code } from 'lucide-react';
import SplitView, { type SplitItem } from '@/components/boilerplates/SplitView';

// ============================================================
// DEMO: Thread Archive / Canon Reader (LIB_B)
// Shows the SplitView boilerplate with sample thread data
// ============================================================

const THREADS: SplitItem[] = [
  {
    id: '1',
    title: 'The Upward Flow of Intelligence',
    subtitle: 'Enterprise OS knowledge architecture design',
    icon: <BookOpen size={14} style={{ color: 'var(--accent-purple)' }} />,
    badge: { label: 'Canonical', color: 'var(--accent-green)' },
    meta: 'Feb 16',
    group: 'architecture',
  },
  {
    id: '2',
    title: 'Property Connect MVP Requirements',
    subtitle: 'AI chatbot spec for estate agents',
    icon: <FileText size={14} style={{ color: 'var(--accent-blue)' }} />,
    badge: { label: 'Canonical', color: 'var(--accent-green)' },
    meta: 'Feb 14',
    group: 'product',
  },
  {
    id: '3',
    title: 'UI Assembly Pipeline Design',
    subtitle: 'Figma → React component pipeline',
    icon: <Zap size={14} style={{ color: 'var(--accent-amber)' }} />,
    badge: { label: 'Canonical', color: 'var(--accent-green)' },
    meta: 'Feb 16',
    group: 'architecture',
  },
  {
    id: '4',
    title: 'LeadEngine Complete Build Spec',
    subtitle: 'AI-powered conversion platform',
    icon: <FileText size={14} style={{ color: 'var(--accent-red)' }} />,
    badge: { label: 'Staging', color: 'var(--accent-amber)' },
    meta: 'Feb 15',
    group: 'product',
  },
  {
    id: '5',
    title: 'Session 2026-02-15 #01',
    subtitle: 'UI kit selection + pipeline decisions',
    icon: <MessageSquare size={14} style={{ color: 'var(--color-command)' }} />,
    badge: { label: 'Staging', color: 'var(--accent-amber)' },
    meta: 'Feb 15',
    group: 'sessions',
  },
  {
    id: '6',
    title: 'Session 2026-02-16 #01',
    subtitle: 'Boilerplate build sprint',
    icon: <MessageSquare size={14} style={{ color: 'var(--color-command)' }} />,
    badge: { label: 'Staging', color: 'var(--accent-amber)' },
    meta: 'Feb 16',
    group: 'sessions',
  },
  {
    id: '7',
    title: 'Keyword Lattice — Property',
    subtitle: '847 keywords across 12 clusters',
    icon: <Code size={14} style={{ color: '#06B6D4' }} />,
    badge: { label: 'Canonical', color: 'var(--accent-green)' },
    meta: 'Feb 12',
    group: 'data',
  },
  {
    id: '8',
    title: 'Brand Voice Rules',
    subtitle: 'Tone, style, and language guidelines',
    icon: <BookOpen size={14} style={{ color: '#EC4899' }} />,
    badge: { label: 'Canonical', color: 'var(--accent-green)' },
    meta: 'Feb 10',
    group: 'architecture',
  },
  {
    id: '9',
    title: 'Competitor Analysis Q1',
    subtitle: '14 property tech companies reviewed',
    icon: <FileText size={14} style={{ color: 'var(--accent-amber)' }} />,
    badge: { label: 'Staging', color: 'var(--accent-amber)' },
    meta: 'Feb 14',
    group: 'data',
  },
  {
    id: '10',
    title: 'Fitness DB Schema',
    subtitle: 'PostgreSQL schema for fitness platform',
    icon: <Code size={14} style={{ color: 'var(--accent-green)' }} />,
    badge: { label: 'Staging', color: 'var(--accent-amber)' },
    meta: 'Feb 11',
    group: 'data',
  },
];

const SAMPLE_CONTENT: Record<string, string> = {
  '1': `# The Upward Flow of Intelligence

Enterprise OS is built on a fundamental principle: **knowledge flows upward through increasingly refined layers**, from raw capture to canonical truth to executable action.

## The S→C→E Pipeline

Every piece of knowledge enters the system through one of three states:

### Staging (Yellow)
Raw input. Unvalidated. Could be a chat transcript, a brainstorm, a competitor screenshot. It needs processing before it can be trusted.

### Canonical (Green)
Validated truth. Cross-referenced, deduplicated, and approved. This is the single source of truth that agents and automation can rely on.

### Execution (Blue)
Deployed and active. Templates being used, scripts running, dashboards serving data. Canonical knowledge that has been operationalised.

## The 8-Component Architecture

The system is structured as a body metaphor:
- **Brain** (Navigation) — Goals, priorities, state awareness
- **Hands** (Command Deck) — Daily operations, agent workspace
- **Nervous System** (Core Engine) — Scripts, indices, routing
- **Stomach** (Knowledge Library) — Ingestion, extraction, storage
- **DNA** (Template Hub) — Reusable patterns and scaffolds
- **Organs** (Domain Pillars) — 23 specialist knowledge domains
- **Limbs** (Build Factory) — Active project builds
- **Immune System** (Operations) — Post-launch monitoring, legal, finance`,

  '2': `# Property Connect London — MVP Requirements

## Overview
AI-powered property chatbot for estate agents in London. Provides intelligent property search, neighbourhood insights, and lead qualification.

## Core Features
1. **Conversational Search** — Natural language property queries
2. **Smart Matching** — AI-driven property recommendations based on preferences
3. **Area Intelligence** — School ratings, transport, demographics
4. **Lead Qualification** — Automated buyer/renter scoring
5. **Agent Dashboard** — Conversation history, lead pipeline, analytics

## Tech Stack
- Next.js 16 + React 19
- PostgreSQL + ChromaDB
- Claude API for conversation
- MapBox for location features
- Tailwind CSS

## Timeline
- **MVP Target:** February 28, 2026
- **Current Progress:** 15%
- **Risk Level:** HIGH — behind schedule`,
};

export default function ThreadArchivePage() {
  const [selected, setSelected] = useState<SplitItem | null>(null);

  return (
    <SplitView
      title="Thread Archive"
      description="All extracted knowledge threads"
      items={THREADS}
      selectedItem={selected}
      onItemSelect={setSelected}
      groups={[
        { key: 'architecture', label: 'Architecture' },
        { key: 'product', label: 'Product' },
        { key: 'sessions', label: 'Sessions' },
        { key: 'data', label: 'Data & Research' },
      ]}
      contentPanel={(item) => {
        const content = SAMPLE_CONTENT[item.id];
        return (
          <div className="markdown-content">
            {content ? (
              <div style={{ whiteSpace: 'pre-wrap', fontSize: 14, lineHeight: 1.7, color: 'var(--text-secondary)' }}>
                {content.split('\n').map((line, i) => {
                  if (line.startsWith('# ')) return <h1 key={i}>{line.replace('# ', '')}</h1>;
                  if (line.startsWith('## ')) return <h2 key={i}>{line.replace('## ', '')}</h2>;
                  if (line.startsWith('### ')) return <h3 key={i}>{line.replace('### ', '')}</h3>;
                  if (line.startsWith('- **')) {
                    const [bold, rest] = line.replace('- **', '').split('**');
                    return <li key={i}><strong>{bold}</strong>{rest}</li>;
                  }
                  if (line.match(/^\d+\. \*\*/)) {
                    const match = line.match(/^(\d+)\. \*\*(.+?)\*\*(.*)$/);
                    if (match) return <li key={i}><strong>{match[2]}</strong>{match[3]}</li>;
                  }
                  if (line.trim() === '') return <br key={i} />;
                  return <p key={i}>{line.replace(/\*\*(.+?)\*\*/g, '$1')}</p>;
                })}
              </div>
            ) : (
              <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-tertiary)' }}>
                <p style={{ fontSize: 14 }}>Content preview for &ldquo;{item.title}&rdquo;</p>
                <p style={{ fontSize: 13 }}>Full content would be loaded from the knowledge base.</p>
              </div>
            )}
          </div>
        );
      }}
      headerActions={(item) => (
        <div style={{ display: 'flex', gap: 8 }}>
          <button style={{ padding: '6px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-default)', background: 'var(--bg-secondary)', color: 'var(--text-secondary)', fontSize: 12, cursor: 'pointer' }}>
            Extract
          </button>
          <button style={{ padding: '6px 12px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-green)', color: '#fff', fontSize: 12, cursor: 'pointer', fontWeight: 500 }}>
            Promote to Canon
          </button>
        </div>
      )}
      actions={[
        { label: '+ Import Thread', onClick: () => {}, variant: 'primary' },
      ]}
    />
  );
}
