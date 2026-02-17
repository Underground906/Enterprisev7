'use client';

import { MessageSquare, Zap, Target, Code, FileText, AlertCircle } from 'lucide-react';
import Timeline, { type TimelineEvent } from '@/components/boilerplates/Timeline';

// ============================================================
// DEMO: Session History (CMD_C)
// Shows the Timeline boilerplate with session/activity events
// ============================================================

const EVENTS: TimelineEvent[] = [
  {
    id: '1',
    title: 'Boilerplate Build Sprint Started',
    description: 'Built 11 of 15 boilerplate templates: DashboardList, CardGrid, AuthSplit, DashboardAnalytics, MultiStepWizard, SearchResults, ChatFeed, SplitView, ApprovalQueue, DashboardForm, Timeline.',
    timestamp: '2026-02-16T14:30',
    type: 'build',
    icon: <Code size={14} style={{ color: 'var(--accent-blue)' }} />,
    color: 'var(--accent-blue)',
    user: 'John + Claude',
    tags: ['UI Library', 'boilerplates'],
    detail: (
      <div>
        <h4 style={{ fontSize: 14, fontWeight: 600, marginBottom: 12 }}>Build Summary</h4>
        <div style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.7 }}>
          <p>Created 11 React boilerplate components that cover all 48 Enterprise OS screens:</p>
          <ul style={{ paddingLeft: 20, marginTop: 8 }}>
            <li>DashboardList — tables, filters, search</li>
            <li>CardGrid — card-based catalogues</li>
            <li>AuthSplit — login/register flows</li>
            <li>DashboardAnalytics — charts + stats</li>
            <li>MultiStepWizard — step-by-step forms</li>
            <li>SearchResults — search + filter + preview</li>
            <li>ChatFeed — AI conversation interface</li>
            <li>SplitView — list + content viewer</li>
            <li>ApprovalQueue — review + approve/reject</li>
            <li>DashboardForm — settings + configuration</li>
            <li>Timeline — activity/session history</li>
          </ul>
        </div>
      </div>
    ),
  },
  {
    id: '2',
    title: 'PRD Granular Screens Completed',
    description: '48 screens, 188 states, 29 modals documented. Every page drilled down to component level.',
    timestamp: '2026-02-16T12:15',
    type: 'document',
    icon: <FileText size={14} style={{ color: 'var(--accent-green)' }} />,
    color: 'var(--accent-green)',
    user: 'John + Claude',
    tags: ['PRD', 'product'],
  },
  {
    id: '3',
    title: 'PRD-to-Inventory Matching Complete',
    description: 'All 41 PRD screens matched to Brainwave template components. 100% coverage achieved.',
    timestamp: '2026-02-16T11:30',
    type: 'milestone',
    icon: <Target size={14} style={{ color: 'var(--accent-purple)' }} />,
    color: 'var(--accent-purple)',
    user: 'Claude',
    tags: ['matching', 'pipeline'],
  },
  {
    id: '4',
    title: 'Gemini Free Tier Exhausted',
    description: 'Switched to DeepSeek/Groq for remaining kit identification. Brainwave complete (48 screens).',
    timestamp: '2026-02-16T10:45',
    type: 'alert',
    icon: <AlertCircle size={14} style={{ color: 'var(--accent-amber)' }} />,
    color: 'var(--accent-amber)',
    user: 'System',
    tags: ['API', 'cost'],
  },
  {
    id: '5',
    title: 'Batch Kit Export Running',
    description: 'batch-export-all-kits.js started for 37 remaining kits. Running in background terminal.',
    timestamp: '2026-02-16T10:00',
    type: 'build',
    icon: <Zap size={14} style={{ color: 'var(--accent-blue)' }} />,
    color: 'var(--accent-blue)',
    user: 'John',
    tags: ['Figma', 'export'],
  },
  {
    id: '6',
    title: 'UI Assembly Pipeline Spec Written',
    description: 'Formal 6-stage pipeline documentation: Export → Identify → Structure → Match → Extract → Assemble.',
    timestamp: '2026-02-16T09:30',
    type: 'document',
    icon: <FileText size={14} style={{ color: 'var(--accent-green)' }} />,
    color: 'var(--accent-green)',
    user: 'Claude',
    tags: ['pipeline', 'spec'],
  },
  {
    id: '7',
    title: 'LeadEngine Build Spec Completed',
    description: '£5,000/month AI-powered conversion platform. 42 app screens, 18 marketing screens, 38 content pieces.',
    timestamp: '2026-02-15T18:00',
    type: 'milestone',
    icon: <Target size={14} style={{ color: 'var(--accent-purple)' }} />,
    color: 'var(--accent-purple)',
    user: 'John + Claude',
    tags: ['LeadEngine', 'PRD'],
  },
  {
    id: '8',
    title: 'UI Kit Selection Finalised',
    description: 'Tier 1: Brainwave, Untitled UI Pro, Fleet, Source Fusion AI, Chroma, Square Dashboard, Tripie, Briefberry.',
    timestamp: '2026-02-15T14:20',
    type: 'decision',
    icon: <MessageSquare size={14} style={{ color: 'var(--color-command)' }} />,
    color: 'var(--color-command)',
    user: 'John',
    tags: ['UI kits', 'design'],
  },
  {
    id: '9',
    title: 'Brainwave Screen Export Complete',
    description: '48 template screens exported as PNGs from Figma via API. All identified with AI vision.',
    timestamp: '2026-02-15T11:00',
    type: 'build',
    icon: <Code size={14} style={{ color: 'var(--accent-blue)' }} />,
    color: 'var(--accent-blue)',
    user: 'Claude',
    tags: ['Figma', 'Brainwave'],
  },
];

export default function SessionHistoryPage() {
  return (
    <Timeline
      title="Session History"
      description="Chronological log of all sessions, decisions, and milestones"
      events={EVENTS}
      groupBy="day"
      typeFilters={[
        { key: 'build', label: 'Builds', color: 'var(--accent-blue)' },
        { key: 'document', label: 'Documents', color: 'var(--accent-green)' },
        { key: 'milestone', label: 'Milestones', color: 'var(--accent-purple)' },
        { key: 'decision', label: 'Decisions', color: 'var(--color-command)' },
        { key: 'alert', label: 'Alerts', color: 'var(--accent-amber)' },
      ]}
      actions={[
        { label: 'Export Log', onClick: () => {} },
        { label: '+ Log Entry', onClick: () => {}, variant: 'primary' },
      ]}
      emptyState={{
        title: 'No events found',
        description: 'Try adjusting your filters',
      }}
    />
  );
}
