'use client';

import { useState } from 'react';
import { Target, Layers, Calendar, CheckCircle } from 'lucide-react';
import MultiStepWizard, { type WizardStep } from '@/components/boilerplates/MultiStepWizard';

// ============================================================
// DEMO: Goal Intake Wizard (NAV_A)
// Shows the MultiStepWizard boilerplate for creating a new goal
// ============================================================

function FieldGroup({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ marginBottom: 20 }}>
      <label style={{ display: 'block', fontSize: 13, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 6 }}>{label}</label>
      {children}
    </div>
  );
}

function TextInput({ placeholder }: { placeholder?: string }) {
  return (
    <input
      type="text"
      placeholder={placeholder}
      style={{
        width: '100%',
        padding: '10px 12px',
        border: '1px solid var(--border-default)',
        borderRadius: 'var(--radius-md)',
        fontSize: 14,
        color: 'var(--text-primary)',
        background: 'var(--bg-card)',
        outline: 'none',
        boxSizing: 'border-box',
      }}
    />
  );
}

function TextArea({ placeholder, rows = 3 }: { placeholder?: string; rows?: number }) {
  return (
    <textarea
      placeholder={placeholder}
      rows={rows}
      style={{
        width: '100%',
        padding: '10px 12px',
        border: '1px solid var(--border-default)',
        borderRadius: 'var(--radius-md)',
        fontSize: 14,
        color: 'var(--text-primary)',
        background: 'var(--bg-card)',
        outline: 'none',
        resize: 'vertical',
        fontFamily: 'inherit',
        boxSizing: 'border-box',
      }}
    />
  );
}

function SelectInput({ options, placeholder }: { options: string[]; placeholder?: string }) {
  return (
    <select
      style={{
        width: '100%',
        padding: '10px 12px',
        border: '1px solid var(--border-default)',
        borderRadius: 'var(--radius-md)',
        fontSize: 14,
        color: 'var(--text-primary)',
        background: 'var(--bg-card)',
        outline: 'none',
      }}
    >
      <option value="">{placeholder || 'Select...'}</option>
      {options.map((opt) => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  );
}

function PillarCheckboxes() {
  const pillars = [
    'Enterprise OS', 'Property', 'Fitness', 'LeadEngine',
    'UI Library', 'Knowledge Ingestion', 'Branding', 'Copy',
    'Marketing', 'Content', 'Development', 'Operations',
  ];
  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8 }}>
      {pillars.map((p) => (
        <label
          key={p}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 8,
            padding: '8px 12px',
            border: '1px solid var(--border-default)',
            borderRadius: 'var(--radius-md)',
            cursor: 'pointer',
            fontSize: 13,
            color: 'var(--text-secondary)',
            background: 'var(--bg-card)',
          }}
        >
          <input type="checkbox" style={{ accentColor: 'var(--accent-purple)' }} />
          {p}
        </label>
      ))}
    </div>
  );
}

export default function GoalIntakePage() {
  const steps: WizardStep[] = [
    {
      key: 'define',
      title: 'Define',
      icon: <Target size={16} />,
      description: 'What do you want to achieve?',
      content: (
        <div>
          <FieldGroup label="Goal Title">
            <TextInput placeholder="e.g. Launch Property Connect London MVP" />
          </FieldGroup>
          <FieldGroup label="Description">
            <TextArea placeholder="Describe the goal, its purpose, and expected outcomes..." rows={4} />
          </FieldGroup>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
            <FieldGroup label="Priority">
              <SelectInput options={['P1 — Critical', 'P2 — High', 'P3 — Medium', 'P4 — Low']} placeholder="Select priority" />
            </FieldGroup>
            <FieldGroup label="Category">
              <SelectInput options={['Revenue', 'Infrastructure', 'Product', 'Content', 'Operations']} placeholder="Select category" />
            </FieldGroup>
          </div>
        </div>
      ),
    },
    {
      key: 'scope',
      title: 'Scope',
      icon: <Layers size={16} />,
      description: 'Which pillars and resources are involved?',
      content: (
        <div>
          <FieldGroup label="Related Pillars">
            <PillarCheckboxes />
          </FieldGroup>
          <FieldGroup label="Key Dependencies">
            <TextArea placeholder="List any dependencies, blockers, or prerequisites..." rows={3} />
          </FieldGroup>
          <FieldGroup label="Success Metrics">
            <TextArea placeholder="How will you measure success? e.g. 'MVP live with 10 test users by Feb 28'" rows={3} />
          </FieldGroup>
        </div>
      ),
    },
    {
      key: 'timeline',
      title: 'Timeline',
      icon: <Calendar size={16} />,
      description: 'When should this be completed?',
      content: (
        <div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
            <FieldGroup label="Start Date">
              <input
                type="date"
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-md)',
                  fontSize: 14,
                  color: 'var(--text-primary)',
                  background: 'var(--bg-card)',
                  outline: 'none',
                  boxSizing: 'border-box',
                }}
              />
            </FieldGroup>
            <FieldGroup label="Target Date">
              <input
                type="date"
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-md)',
                  fontSize: 14,
                  color: 'var(--text-primary)',
                  background: 'var(--bg-card)',
                  outline: 'none',
                  boxSizing: 'border-box',
                }}
              />
            </FieldGroup>
          </div>
          <FieldGroup label="Milestones">
            <TextArea placeholder="Break down into milestones, one per line:&#10;Week 1: Schema + API foundation&#10;Week 2: Core UI + integrations&#10;Week 3: Testing + launch" rows={5} />
          </FieldGroup>
          <FieldGroup label="Time Commitment">
            <SelectInput options={['Full time (8h/day)', 'Part time (4h/day)', '2-hour blocks', 'Ad hoc']} placeholder="Select commitment level" />
          </FieldGroup>
        </div>
      ),
    },
    {
      key: 'confirm',
      title: 'Confirm',
      icon: <CheckCircle size={16} />,
      description: 'Review and create your goal.',
      content: (
        <div
          style={{
            background: 'var(--bg-card)',
            border: '1px solid var(--border-default)',
            borderRadius: 'var(--radius-lg)',
            padding: '24px',
          }}
        >
          <div style={{ fontSize: 14, color: 'var(--text-tertiary)', marginBottom: 16 }}>
            Review your goal details and click &ldquo;Create Goal&rdquo; to add it to your active goals.
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            <div style={{ padding: '12px 16px', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-md)' }}>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>Goal Title</div>
              <div style={{ fontSize: 14, fontWeight: 500, color: 'var(--text-primary)' }}>Will be populated from Step 1</div>
            </div>
            <div style={{ padding: '12px 16px', background: 'var(--bg-tertiary)', borderRadius: 'var(--radius-md)' }}>
              <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 4 }}>This goal will be tracked in the Goal Health dashboard</div>
              <div style={{ fontSize: 14, fontWeight: 500, color: 'var(--accent-green)' }}>Ready to create</div>
            </div>
          </div>
        </div>
      ),
    },
  ];

  return (
    <MultiStepWizard
      title="New Goal"
      subtitle="Create a new tracked goal with milestones and success metrics"
      steps={steps}
      onComplete={() => console.log('Goal created!')}
      onCancel={() => console.log('Cancelled')}
      completeLabel="Create Goal"
    />
  );
}
