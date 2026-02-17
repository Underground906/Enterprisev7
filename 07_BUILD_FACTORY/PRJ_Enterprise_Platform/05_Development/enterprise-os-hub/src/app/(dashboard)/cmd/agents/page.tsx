'use client';

import { useState } from 'react';
import { Brain, Code, Megaphone, Palette, Shield, Target, FileText, BarChart3 } from 'lucide-react';
import CardGrid, { type CardItem } from '@/components/boilerplates/CardGrid';

// ============================================================
// DEMO: Agent Registry (CMD_D)
// Shows the CardGrid boilerplate with sample agent data
// ============================================================

const AGENTS: CardItem[] = [
  {
    id: 'seo-lead',
    title: 'SEO Lead',
    description: 'Technical SEO specialist. Analyses keyword strategies, site architecture, and search performance.',
    category: 'Knowledge',
    icon: <Target size={20} style={{ color: 'var(--accent-purple)' }} />,
    badges: [
      { label: 'Keywords', color: 'var(--accent-blue)' },
      { label: 'Site Architecture', color: 'var(--accent-green)' },
    ],
    meta: 'Used 47 times',
    starred: true,
  },
  {
    id: 'copy-chief',
    title: 'Copy Chief',
    description: 'Conversion copywriter. Writes headlines, landing pages, and email sequences using proven formulas.',
    category: 'Creation',
    icon: <FileText size={20} style={{ color: 'var(--accent-amber)' }} />,
    badges: [
      { label: 'Headlines', color: 'var(--accent-amber)' },
      { label: 'Landing Pages', color: 'var(--accent-red)' },
    ],
    meta: 'Used 82 times',
    starred: true,
  },
  {
    id: 'data-engineer',
    title: 'Data Engineer',
    description: 'Database architecture and pipeline specialist. Designs schemas, optimises queries, builds ETL flows.',
    category: 'Knowledge',
    icon: <Code size={20} style={{ color: 'var(--accent-blue)' }} />,
    badges: [
      { label: 'PostgreSQL', color: 'var(--accent-blue)' },
      { label: 'Pipelines', color: 'var(--accent-purple)' },
    ],
    meta: 'Used 31 times',
  },
  {
    id: 'brand-strategist',
    title: 'Brand Strategist',
    description: 'Develops brand positioning, voice guidelines, and unique mechanism frameworks.',
    category: 'Creation',
    icon: <Palette size={20} style={{ color: '#EC4899' }} />,
    badges: [
      { label: 'Positioning', color: '#EC4899' },
      { label: 'Voice', color: 'var(--accent-purple)' },
    ],
    meta: 'Used 19 times',
  },
  {
    id: 'chief-of-staff',
    title: 'Chief of Staff',
    description: 'Strategic operations. Aligns activities to goals, manages cross-team dependencies, flags risks.',
    category: 'System',
    icon: <Shield size={20} style={{ color: 'var(--accent-green)' }} />,
    badges: [
      { label: 'Strategy', color: 'var(--accent-green)' },
      { label: 'Operations', color: 'var(--accent-amber)' },
    ],
    meta: 'Used 56 times',
    starred: true,
  },
  {
    id: 'market-analyst',
    title: 'Market Analyst',
    description: 'Competitor research, TAM/SAM/SOM analysis, market validation, and trend identification.',
    category: 'Knowledge',
    icon: <BarChart3 size={20} style={{ color: '#06B6D4' }} />,
    badges: [
      { label: 'Research', color: '#06B6D4' },
      { label: 'Competitors', color: 'var(--accent-red)' },
    ],
    meta: 'Used 23 times',
  },
  {
    id: 'growth-marketer',
    title: 'Growth Marketer',
    description: 'GTM strategy, funnel design, campaign planning, and conversion optimisation.',
    category: 'Creation',
    icon: <Megaphone size={20} style={{ color: 'var(--accent-red)' }} />,
    badges: [
      { label: 'GTM', color: 'var(--accent-red)' },
      { label: 'Funnels', color: 'var(--accent-amber)' },
    ],
    meta: 'Used 15 times',
  },
  {
    id: 'ux-architect',
    title: 'UX Architect',
    description: 'Information architecture, user flows, wireframing, and component specifications.',
    category: 'Creation',
    icon: <Brain size={20} style={{ color: 'var(--color-navigation)' }} />,
    badges: [
      { label: 'Wireframes', color: 'var(--color-navigation)' },
      { label: 'User Flows', color: 'var(--accent-blue)' },
    ],
    meta: 'Used 28 times',
  },
  {
    id: 'devops-eng',
    title: 'DevOps Engineer',
    description: 'CI/CD pipelines, Docker, Kubernetes, infrastructure as code, monitoring.',
    category: 'System',
    icon: <Code size={20} style={{ color: '#06B6D4' }} />,
    badges: [
      { label: 'Docker', color: '#06B6D4' },
      { label: 'CI/CD', color: 'var(--accent-green)' },
    ],
    meta: 'Used 12 times',
  },
];

export default function AgentRegistryPage() {
  const [activeTab, setActiveTab] = useState('all');
  const [selected, setSelected] = useState<CardItem | null>(null);

  const filteredItems = activeTab === 'all'
    ? AGENTS
    : AGENTS.filter((a) => a.category?.toLowerCase() === activeTab);

  return (
    <CardGrid
      title="Agent Registry"
      description="80+ role-based expert profiles to activate per session"
      items={filteredItems}
      tabs={[
        { key: 'all', label: 'All', count: AGENTS.length },
        { key: 'knowledge', label: 'Knowledge', count: AGENTS.filter((a) => a.category === 'Knowledge').length },
        { key: 'creation', label: 'Creation', count: AGENTS.filter((a) => a.category === 'Creation').length },
        { key: 'system', label: 'System', count: AGENTS.filter((a) => a.category === 'System').length },
      ]}
      activeTab={activeTab}
      onTabChange={setActiveTab}
      onItemClick={setSelected}
      onStar={(item) => console.log('Star:', item.id)}
      selectedItem={selected}
      columns={3}
      featuredSection={{
        title: 'Most Used',
        items: AGENTS.filter((a) => a.starred).slice(0, 5),
      }}
      detailPanel={(item) => (
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 16 }}>
            {item.icon && (
              <div style={{ width: 48, height: 48, borderRadius: 'var(--radius-lg)', background: 'var(--bg-tertiary)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                {item.icon}
              </div>
            )}
            <div>
              <h3 style={{ fontSize: 16, fontWeight: 600, margin: 0 }}>{item.title}</h3>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>{item.category}</div>
            </div>
          </div>
          <p style={{ fontSize: 13, color: 'var(--text-secondary)', lineHeight: 1.6, marginBottom: 16 }}>
            {item.description}
          </p>
          {item.badges && (
            <div style={{ marginBottom: 16 }}>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 8 }}>Expertise</div>
              <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap' }}>
                {item.badges.map((b, i) => (
                  <span key={i} style={{ fontSize: 12, padding: '3px 10px', borderRadius: 'var(--radius-sm)', background: b.color ? `${b.color}18` : 'var(--bg-tertiary)', color: b.color }}>
                    {b.label}
                  </span>
                ))}
              </div>
            </div>
          )}
          <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 16 }}>{item.meta}</div>
          <button style={{ width: '100%', padding: '10px', borderRadius: 'var(--radius-md)', border: 'none', background: 'var(--accent-purple)', color: '#fff', fontSize: 13, fontWeight: 500, cursor: 'pointer' }}>
            Activate for Session
          </button>
        </div>
      )}
      actions={[
        { label: '+ Custom Agent', onClick: () => {}, variant: 'primary' },
      ]}
      emptyState={{
        title: 'No agents found',
        description: 'Try a different search or category',
      }}
    />
  );
}
