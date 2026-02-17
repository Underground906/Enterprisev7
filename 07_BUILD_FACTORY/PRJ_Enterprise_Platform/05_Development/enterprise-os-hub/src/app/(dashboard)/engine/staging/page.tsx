'use client';

import { useState } from 'react';
import ApprovalQueue, { type QueueItem } from '@/components/boilerplates/ApprovalQueue';

// ============================================================
// DEMO: Staging Review (ENG_B)
// Shows the ApprovalQueue boilerplate for S→C promotion
// ============================================================

const QUEUE_ITEMS: QueueItem[] = [
  {
    id: '1',
    title: 'competitor_analysis_q1.md',
    description: 'Competitive analysis of 14 property tech companies. Imported from AI thread — needs validation against actual market data.',
    source: 'AI Thread',
    type: 'Market Intel',
    priority: 'high',
    status: 'pending',
    submittedAt: '2h ago',
    meta: { 'Pillar': 'Market Research', 'Word Count': '2,847', 'Source Thread': 'Session 2026-02-14 #03', 'Confidence': '78%' },
  },
  {
    id: '2',
    title: 'keyword_lattice_property.json',
    description: '847 keywords across 12 topic clusters for Property Connect London. Generated via DeepSeek — spot-check needed.',
    source: 'API Pipeline',
    type: 'Schema',
    priority: 'critical',
    status: 'pending',
    submittedAt: '4h ago',
    meta: { 'Pillar': 'Property', 'Keywords': '847', 'Clusters': '12', 'Coverage Score': '92%' },
  },
  {
    id: '3',
    title: 'session_2026-02-15_01.md',
    description: 'UI kit selection decisions and pipeline architecture. Contains 14 key decisions that need canonical status.',
    source: 'Session Log',
    type: 'Decision',
    priority: 'medium',
    status: 'pending',
    submittedAt: '1d ago',
    meta: { 'Pillar': 'Navigation', 'Decisions': '14', 'Duration': '4h 20m' },
  },
  {
    id: '4',
    title: 'fitness_db_schema.sql',
    description: 'PostgreSQL schema for the fitness platform. 23 tables, 8 views. Needs review against the latest PRD.',
    source: 'AI Thread',
    type: 'Schema',
    priority: 'low',
    status: 'pending',
    submittedAt: '3d ago',
    meta: { 'Pillar': 'Fitness', 'Tables': '23', 'Views': '8' },
  },
  {
    id: '5',
    title: 'avatar_icp_premium_agent.md',
    description: 'Ideal Customer Profile for premium estate agents. Based on 6 interview transcripts + market data.',
    source: 'Extraction',
    type: 'Framework',
    priority: 'high',
    status: 'reviewing',
    submittedAt: '5h ago',
    meta: { 'Pillar': 'Avatars', 'Sources': '6 interviews', 'Confidence': '85%' },
  },
  {
    id: '6',
    title: 'headline_formulas_update.json',
    description: '18 new headline formulas to add to the canonical collection. Need deduplication against existing 142.',
    source: 'Manual',
    type: 'Canonical Ref',
    priority: 'medium',
    status: 'pending',
    submittedAt: '2d ago',
    meta: { 'Pillar': 'Copy', 'New Formulas': '18', 'Existing': '142' },
  },
  {
    id: '7',
    title: 'ingestion_error_patterns.md',
    description: 'Analysis of common ingestion pipeline failures. 7 error patterns identified with fixes.',
    source: 'System',
    type: 'SOP',
    priority: 'medium',
    status: 'pending',
    submittedAt: '6h ago',
    meta: { 'Pillar': 'Core Engine', 'Patterns': '7', 'Fix Coverage': '100%' },
  },
];

export default function StagingReviewPage() {
  const [items, setItems] = useState(QUEUE_ITEMS);

  const handleApprove = (item: QueueItem) => {
    setItems((prev) => prev.map((i) => i.id === item.id ? { ...i, status: 'approved' as const } : i));
  };

  const handleReject = (item: QueueItem) => {
    setItems((prev) => prev.map((i) => i.id === item.id ? { ...i, status: 'rejected' as const } : i));
  };

  return (
    <ApprovalQueue
      title="Staging Review"
      description="Review and promote content from Staging to Canonical"
      items={items}
      onApprove={handleApprove}
      onReject={handleReject}
      onBulkApprove={(selected) => {
        const ids = new Set(selected.map((i) => i.id));
        setItems((prev) => prev.map((i) => ids.has(i.id) ? { ...i, status: 'approved' as const } : i));
      }}
      onBulkReject={(selected) => {
        const ids = new Set(selected.map((i) => i.id));
        setItems((prev) => prev.map((i) => ids.has(i.id) ? { ...i, status: 'rejected' as const } : i));
      }}
      stats={{
        pending: items.filter((i) => i.status === 'pending').length,
        reviewing: items.filter((i) => i.status === 'reviewing').length,
        approved: items.filter((i) => i.status === 'approved').length,
        rejected: items.filter((i) => i.status === 'rejected').length,
      }}
      actions={[
        { label: '+ Manual Upload', onClick: () => {}, variant: 'primary' },
      ]}
    />
  );
}
