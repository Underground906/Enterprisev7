'use client';

import DashboardForm, { FormField, FormInput, FormTextArea, FormSelect, FormToggle } from '@/components/boilerplates/DashboardForm';

// ============================================================
// DEMO: System Settings (SYS_C)
// Shows the DashboardForm boilerplate for configuration
// ============================================================

export default function SettingsPage() {
  return (
    <DashboardForm
      title="Settings"
      description="System configuration"
      sections={[
        {
          key: 'profile',
          title: 'Profile',
          description: 'Your personal information and preferences',
          content: (
            <>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
                <FormField label="Full Name" required>
                  <FormInput placeholder="John" defaultValue="John" />
                </FormField>
                <FormField label="Email" required>
                  <FormInput type="email" placeholder="john@enterprise.com" defaultValue="john@enterprise.com" />
                </FormField>
              </div>
              <FormField label="Role">
                <FormSelect
                  options={[
                    { value: 'L7', label: 'L7 — CEO/Owner' },
                    { value: 'L6', label: 'L6 — Director' },
                    { value: 'L5', label: 'L5 — Manager' },
                    { value: 'L4', label: 'L4 — Lead' },
                    { value: 'L3', label: 'L3 — Specialist' },
                    { value: 'L2', label: 'L2 — Contributor' },
                    { value: 'L1', label: 'L1 — Freelancer' },
                  ]}
                  defaultValue="L7"
                />
              </FormField>
              <FormField label="Bio" description="Brief description shown in session logs">
                <FormTextArea placeholder="Tell us about yourself..." defaultValue="Building Enterprise OS and multiple platforms. Focus on knowledge architecture and AI-powered business systems." rows={3} />
              </FormField>
            </>
          ),
        },
        {
          key: 'workspace',
          title: 'Workspace',
          description: 'Configure your working environment',
          content: (
            <>
              <FormField label="Default Work Block Duration">
                <FormSelect
                  options={[
                    { value: '60', label: '1 hour' },
                    { value: '90', label: '1.5 hours' },
                    { value: '120', label: '2 hours' },
                    { value: '180', label: '3 hours' },
                  ]}
                  defaultValue="120"
                />
              </FormField>
              <FormField label="Max Decisions Per Block" description="Prevents decision fatigue in long sessions">
                <FormSelect
                  options={[
                    { value: '2', label: '2 decisions' },
                    { value: '3', label: '3 decisions' },
                    { value: '5', label: '5 decisions' },
                    { value: '10', label: 'Unlimited' },
                  ]}
                  defaultValue="3"
                />
              </FormField>
              <FormField label="Default Start Module">
                <FormSelect
                  options={[
                    { value: 'nav', label: 'Navigation Centre' },
                    { value: 'cmd', label: 'Command Deck' },
                    { value: 'engine', label: 'Core Engine' },
                    { value: 'lib', label: 'Knowledge Library' },
                  ]}
                  defaultValue="nav"
                />
              </FormField>
              <FormToggle label="Auto-start session logging" defaultChecked />
              <FormToggle label="Show module colour coding" defaultChecked />
              <FormToggle label="Enable keyboard shortcuts" defaultChecked />
            </>
          ),
        },
        {
          key: 'governance',
          title: 'Governance',
          description: 'S>C>E pipeline and promotion rules',
          content: (
            <>
              <FormToggle label="Require manual approval for S→C promotion" defaultChecked />
              <FormToggle label="Auto-promote after 72h with no objection" />
              <FormToggle label="Allow agents to self-promote staging content" />
              <FormField label="Default Staging Retention" description="How long staging content stays before auto-archive">
                <FormSelect
                  options={[
                    { value: '7', label: '7 days' },
                    { value: '14', label: '14 days' },
                    { value: '30', label: '30 days' },
                    { value: '90', label: '90 days' },
                    { value: 'never', label: 'Never auto-archive' },
                  ]}
                  defaultValue="30"
                />
              </FormField>
              <FormField label="Canonical Review Frequency">
                <FormSelect
                  options={[
                    { value: 'weekly', label: 'Weekly' },
                    { value: 'biweekly', label: 'Bi-weekly' },
                    { value: 'monthly', label: 'Monthly' },
                    { value: 'quarterly', label: 'Quarterly' },
                  ]}
                  defaultValue="monthly"
                />
              </FormField>
            </>
          ),
        },
        {
          key: 'integrations',
          title: 'Integrations',
          description: 'API keys and external service connections',
          content: (
            <>
              <FormField label="Claude API Key" description="Required for AI features">
                <FormInput type="password" placeholder="sk-ant-..." defaultValue="sk-ant-••••••••••••" />
              </FormField>
              <FormField label="Figma Token" description="Required for UI export pipeline">
                <FormInput type="password" placeholder="figd_..." defaultValue="figd_••••••••" />
              </FormField>
              <FormField label="DeepSeek API Key" description="Used for batch content identification">
                <FormInput type="password" placeholder="sk-..." />
              </FormField>
              <FormToggle label="Enable ChromaDB vector store" defaultChecked />
              <FormToggle label="Enable PostgreSQL connection" defaultChecked />
              <FormToggle label="Enable Redis cache" />
            </>
          ),
        },
        {
          key: 'appearance',
          title: 'Appearance',
          description: 'Visual customisation',
          content: (
            <>
              <FormField label="Theme">
                <FormSelect
                  options={[
                    { value: 'light', label: 'Light' },
                    { value: 'dark', label: 'Dark' },
                    { value: 'system', label: 'System' },
                  ]}
                  defaultValue="light"
                />
              </FormField>
              <FormField label="Brand Green" description="Primary brand colour used throughout the system">
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <div style={{ width: 32, height: 32, borderRadius: 'var(--radius-md)', background: '#0B8C00', border: '1px solid var(--border-default)' }} />
                  <FormInput defaultValue="#0B8C00" />
                </div>
              </FormField>
              <FormField label="Font Family">
                <FormSelect
                  options={[
                    { value: 'inter', label: 'Inter (Default)' },
                    { value: 'dm-sans', label: 'DM Sans' },
                    { value: 'system', label: 'System Default' },
                  ]}
                  defaultValue="inter"
                />
              </FormField>
              <FormToggle label="Compact sidebar" />
              <FormToggle label="Show file sizes in lists" defaultChecked />
              <FormToggle label="Animate transitions" defaultChecked />
            </>
          ),
        },
      ]}
      onSave={() => console.log('Settings saved')}
      onReset={() => console.log('Settings reset')}
      actions={[
        { label: 'Export Config', onClick: () => {} },
      ]}
    />
  );
}
