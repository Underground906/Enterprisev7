'use client';

import { useState } from 'react';
import DashboardList, { Badge } from '@/components/boilerplates/DashboardList';

// ============================================================
// DEMO: Universal Index (ENG_A)
// Shows the DashboardList boilerplate with sample data
// ============================================================

interface FileItem {
  id: string;
  name: string;
  type: string;
  pillar: string;
  state: 'staging' | 'canonical' | 'execution';
  size: string;
  modified: string;
  source: string;
}

const STATE_COLORS: Record<string, { label: string; color: string }> = {
  staging: { label: 'Staging', color: 'var(--accent-amber)' },
  canonical: { label: 'Canonical', color: 'var(--accent-green)' },
  execution: { label: 'Execution', color: 'var(--accent-blue)' },
};

const SAMPLE_DATA: FileItem[] = [
  { id: '1', name: 'MASTER_CONTEXT.md', type: 'Framework', pillar: 'Enterprise OS', state: 'canonical', size: '24 KB', modified: '2026-02-16', source: 'Manual' },
  { id: '2', name: 'PRD_Enterprise_OS_V7_MASTER.md', type: 'Template', pillar: 'Product Dev', state: 'canonical', size: '18 KB', modified: '2026-02-13', source: 'Session' },
  { id: '3', name: 'keyword_lattice_property.json', type: 'Schema', pillar: 'Property', state: 'staging', size: '45 KB', modified: '2026-02-15', source: 'API' },
  { id: '4', name: 'competitor_analysis_q1.md', type: 'Market Intel', pillar: 'Market Research', state: 'staging', size: '12 KB', modified: '2026-02-14', source: 'AI Thread' },
  { id: '5', name: 'brand_voice_rules.md', type: 'Canonical Ref', pillar: 'Branding', state: 'canonical', size: '8 KB', modified: '2026-02-10', source: 'Manual' },
  { id: '6', name: 'ui_component_inventory.json', type: 'Schema', pillar: 'UI Library', state: 'execution', size: '411 KB', modified: '2026-02-16', source: 'Script' },
  { id: '7', name: 'session_2026-02-15_01.md', type: 'Decision', pillar: 'Navigation', state: 'staging', size: '6 KB', modified: '2026-02-15', source: 'Session' },
  { id: '8', name: 'ROUTING_MANIFEST.md', type: 'SOP', pillar: 'Core Engine', state: 'canonical', size: '15 KB', modified: '2026-02-12', source: 'Manual' },
  { id: '9', name: 'headline_formulas.json', type: 'Canonical Ref', pillar: 'Copy', state: 'canonical', size: '32 KB', modified: '2026-02-08', source: 'Extraction' },
  { id: '10', name: 'fitness_db_schema.sql', type: 'Schema', pillar: 'Fitness', state: 'staging', size: '19 KB', modified: '2026-02-11', source: 'AI Thread' },
  { id: '11', name: 'ingestion_pipeline_errors.log', type: 'Execution', pillar: 'Core Engine', state: 'execution', size: '2 KB', modified: '2026-02-16', source: 'System' },
  { id: '12', name: 'avatar_icp_premium_agent.md', type: 'Framework', pillar: 'Avatars', state: 'canonical', size: '14 KB', modified: '2026-02-09', source: 'Extraction' },
];

export default function UniversalIndexPage() {
  const [activeTab, setActiveTab] = useState('all');
  const [selected, setSelected] = useState<FileItem | null>(null);

  const filteredData = activeTab === 'all'
    ? SAMPLE_DATA
    : SAMPLE_DATA.filter((item) => item.state === activeTab);

  return (
    <DashboardList<FileItem>
      title="Universal Index"
      description="Every file, thread, and artifact in the system"
      columns={[
        {
          key: 'name',
          label: 'Name',
          render: (item) => (
            <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>{item.name}</span>
          ),
        },
        {
          key: 'type',
          label: 'Type',
          width: '120px',
          render: (item) => <Badge>{item.type}</Badge>,
        },
        {
          key: 'pillar',
          label: 'Pillar',
          width: '140px',
        },
        {
          key: 'state',
          label: 'State',
          width: '110px',
          render: (item) => {
            const s = STATE_COLORS[item.state];
            return <Badge color={s.color}>{s.label}</Badge>;
          },
        },
        { key: 'size', label: 'Size', width: '80px' },
        { key: 'modified', label: 'Modified', width: '110px' },
        { key: 'source', label: 'Source', width: '100px' },
      ]}
      data={filteredData}
      getRowKey={(item) => item.id}
      tabs={[
        { key: 'all', label: 'All', count: SAMPLE_DATA.length },
        { key: 'staging', label: 'Staging', count: SAMPLE_DATA.filter((d) => d.state === 'staging').length },
        { key: 'canonical', label: 'Canonical', count: SAMPLE_DATA.filter((d) => d.state === 'canonical').length },
        { key: 'execution', label: 'Execution', count: SAMPLE_DATA.filter((d) => d.state === 'execution').length },
      ]}
      activeTab={activeTab}
      onTabChange={setActiveTab}
      filters={[
        {
          key: 'pillar',
          label: 'Pillar',
          options: [
            { value: 'Enterprise OS', label: 'Enterprise OS' },
            { value: 'Property', label: 'Property' },
            { value: 'Fitness', label: 'Fitness' },
            { value: 'UI Library', label: 'UI Library' },
            { value: 'Copy', label: 'Copy' },
            { value: 'Branding', label: 'Branding' },
          ],
        },
        {
          key: 'type',
          label: 'Type',
          options: [
            { value: 'Framework', label: 'Framework' },
            { value: 'Schema', label: 'Schema' },
            { value: 'Template', label: 'Template' },
            { value: 'SOP', label: 'SOP' },
            { value: 'Decision', label: 'Decision' },
            { value: 'Market Intel', label: 'Market Intel' },
          ],
        },
      ]}
      stats={[
        { label: 'Total Items', value: '2,847' },
        { label: 'Canonical', value: '1,203', color: 'var(--accent-green)' },
        { label: 'Staging', value: '1,412', color: 'var(--accent-amber)' },
        { label: 'Processed Today', value: '34', color: 'var(--accent-purple)' },
      ]}
      onRowClick={setSelected}
      selectedItem={selected}
      detailPanel={(item) => (
        <div>
          <h3 style={{ fontSize: 16, fontWeight: 600, marginBottom: 16 }}>{item.name}</h3>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Type</div>
              <Badge>{item.type}</Badge>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Pillar</div>
              <div style={{ fontSize: 14 }}>{item.pillar}</div>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>State</div>
              <Badge color={STATE_COLORS[item.state].color}>{STATE_COLORS[item.state].label}</Badge>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Source</div>
              <div style={{ fontSize: 14 }}>{item.source}</div>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Size</div>
              <div style={{ fontSize: 14 }}>{item.size}</div>
            </div>
            <div>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Last Modified</div>
              <div style={{ fontSize: 14 }}>{item.modified}</div>
            </div>
            <div style={{ marginTop: 8, display: 'flex', gap: 8 }}>
              <button style={{ flex: 1, padding: '8px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-green)', color: '#fff', fontSize: 13, cursor: 'pointer', fontWeight: 500 }}>
                Promote
              </button>
              <button style={{ flex: 1, padding: '8px', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-default)', background: 'var(--bg-secondary)', color: 'var(--text-primary)', fontSize: 13, cursor: 'pointer' }}>
                View File
              </button>
            </div>
          </div>
        </div>
      )}
      actions={[
        { label: 'Export CSV', onClick: () => {} },
        { label: '+ Ingest Content', onClick: () => {}, variant: 'primary' },
      ]}
      emptyState={{
        title: 'No items found',
        description: 'Try adjusting your filters or search query',
      }}
    />
  );
}
