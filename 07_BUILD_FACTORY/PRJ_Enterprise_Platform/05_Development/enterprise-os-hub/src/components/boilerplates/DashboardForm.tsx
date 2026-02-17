'use client';

import { useState } from 'react';
import { Save, RotateCcw } from 'lucide-react';

// ============================================================
// DASHBOARD FORM BOILERPLATE
// Used by: Settings (SYS_C), User Profile, Project Config,
//          Permission Editor, Agent Config, any screen with
//          grouped form fields + save/cancel
// Layout: Sidebar nav + Form sections + Action bar
// ============================================================

export interface FormSection {
  key: string;
  title: string;
  description?: string;
  content: React.ReactNode;
}

interface DashboardFormProps {
  title?: string;
  description?: string;
  sections: FormSection[];
  onSave: () => void;
  onReset?: () => void;
  saveLabel?: string;
  loading?: boolean;
  dirty?: boolean;
  actions?: { label: string; onClick: () => void; variant?: 'primary' | 'default' | 'danger' }[];
}

export function FormField({ label, description, children, required }: { label: string; description?: string; children: React.ReactNode; required?: boolean }) {
  return (
    <div style={{ marginBottom: 20 }}>
      <label style={{ display: 'block', fontSize: 13, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 4 }}>
        {label}
        {required && <span style={{ color: 'var(--accent-red)', marginLeft: 2 }}>*</span>}
      </label>
      {description && (
        <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginBottom: 6 }}>{description}</div>
      )}
      {children}
    </div>
  );
}

export function FormInput({ type = 'text', placeholder, defaultValue }: { type?: string; placeholder?: string; defaultValue?: string }) {
  return (
    <input
      type={type}
      placeholder={placeholder}
      defaultValue={defaultValue}
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

export function FormTextArea({ placeholder, defaultValue, rows = 3 }: { placeholder?: string; defaultValue?: string; rows?: number }) {
  return (
    <textarea
      placeholder={placeholder}
      defaultValue={defaultValue}
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

export function FormSelect({ options, placeholder, defaultValue }: { options: { value: string; label: string }[]; placeholder?: string; defaultValue?: string }) {
  return (
    <select
      defaultValue={defaultValue || ''}
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
      {placeholder && <option value="">{placeholder}</option>}
      {options.map((opt) => (
        <option key={opt.value} value={opt.value}>{opt.label}</option>
      ))}
    </select>
  );
}

export function FormToggle({ label, defaultChecked }: { label: string; defaultChecked?: boolean }) {
  const [checked, setChecked] = useState(defaultChecked || false);
  return (
    <label style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', cursor: 'pointer', padding: '8px 0' }}>
      <span style={{ fontSize: 13, color: 'var(--text-secondary)' }}>{label}</span>
      <div
        onClick={() => setChecked(!checked)}
        style={{
          width: 40,
          height: 22,
          borderRadius: 11,
          background: checked ? 'var(--accent-green)' : 'var(--bg-tertiary)',
          position: 'relative',
          transition: 'background 0.2s',
          cursor: 'pointer',
          border: `1px solid ${checked ? 'var(--accent-green)' : 'var(--border-default)'}`,
        }}
      >
        <div
          style={{
            width: 16,
            height: 16,
            borderRadius: '50%',
            background: '#fff',
            position: 'absolute',
            top: 2,
            left: checked ? 21 : 2,
            transition: 'left 0.2s',
            boxShadow: '0 1px 3px rgba(0,0,0,0.2)',
          }}
        />
      </div>
    </label>
  );
}

export default function DashboardForm({
  title,
  description,
  sections,
  onSave,
  onReset,
  saveLabel = 'Save Changes',
  loading,
  dirty = true,
  actions,
}: DashboardFormProps) {
  const [activeSection, setActiveSection] = useState(sections[0]?.key || '');

  const scrollToSection = (key: string) => {
    setActiveSection(key);
    document.getElementById(`form-section-${key}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Section Navigation */}
      <div
        style={{
          width: 220,
          minWidth: 220,
          borderRight: '1px solid var(--border-default)',
          background: 'var(--bg-secondary)',
          padding: '20px 0',
          overflow: 'auto',
        }}
      >
        {title && (
          <div style={{ padding: '0 20px 16px', borderBottom: '1px solid var(--border-default)', marginBottom: 8 }}>
            <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>{title}</div>
            {description && <div style={{ fontSize: 12, color: 'var(--text-tertiary)', marginTop: 4 }}>{description}</div>}
          </div>
        )}
        {sections.map((section) => (
          <button
            key={section.key}
            onClick={() => scrollToSection(section.key)}
            style={{
              display: 'block',
              width: '100%',
              padding: '8px 20px',
              border: 'none',
              background: activeSection === section.key ? 'var(--bg-active)' : 'transparent',
              color: activeSection === section.key ? 'var(--accent-purple)' : 'var(--text-secondary)',
              fontSize: 13,
              fontWeight: activeSection === section.key ? 500 : 400,
              cursor: 'pointer',
              textAlign: 'left',
              borderLeft: activeSection === section.key ? '3px solid var(--accent-purple)' : '3px solid transparent',
              transition: 'all 0.15s',
            }}
          >
            {section.title}
          </button>
        ))}
      </div>

      {/* Form Content */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        <div style={{ flex: 1, overflow: 'auto', padding: '24px 32px' }}>
          {sections.map((section) => (
            <div
              key={section.key}
              id={`form-section-${section.key}`}
              style={{ marginBottom: 40 }}
            >
              <h3 style={{ fontSize: 16, fontWeight: 600, color: 'var(--text-primary)', margin: '0 0 4px' }}>
                {section.title}
              </h3>
              {section.description && (
                <p style={{ fontSize: 13, color: 'var(--text-tertiary)', margin: '0 0 20px' }}>
                  {section.description}
                </p>
              )}
              <div
                style={{
                  background: 'var(--bg-card)',
                  border: '1px solid var(--border-default)',
                  borderRadius: 'var(--radius-lg)',
                  padding: '20px 24px',
                }}
              >
                {section.content}
              </div>
            </div>
          ))}
        </div>

        {/* Action Bar */}
        <div
          style={{
            padding: '14px 32px',
            borderTop: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}
        >
          <div>
            {dirty && (
              <span style={{ fontSize: 12, color: 'var(--accent-amber)', fontWeight: 500 }}>
                Unsaved changes
              </span>
            )}
          </div>
          <div style={{ display: 'flex', gap: 8 }}>
            {onReset && (
              <button
                onClick={onReset}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 6,
                  padding: '8px 16px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--border-default)',
                  background: 'var(--bg-secondary)',
                  color: 'var(--text-secondary)',
                  fontSize: 13,
                  cursor: 'pointer',
                }}
              >
                <RotateCcw size={14} /> Reset
              </button>
            )}
            {actions?.map((action, i) => (
              <button
                key={i}
                onClick={action.onClick}
                style={{
                  padding: '8px 16px',
                  borderRadius: 'var(--radius-md)',
                  border: action.variant === 'danger' ? '1px solid var(--accent-red)' : action.variant === 'primary' ? 'none' : '1px solid var(--border-default)',
                  background: action.variant === 'primary' ? 'var(--accent-purple)' : action.variant === 'danger' ? 'transparent' : 'var(--bg-secondary)',
                  color: action.variant === 'primary' ? '#fff' : action.variant === 'danger' ? 'var(--accent-red)' : 'var(--text-primary)',
                  fontSize: 13,
                  fontWeight: 500,
                  cursor: 'pointer',
                }}
              >
                {action.label}
              </button>
            ))}
            <button
              onClick={onSave}
              disabled={loading}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 6,
                padding: '8px 20px',
                borderRadius: 'var(--radius-md)',
                border: 'none',
                background: loading ? 'var(--text-tertiary)' : 'var(--accent-green)',
                color: '#fff',
                fontSize: 13,
                fontWeight: 500,
                cursor: loading ? 'not-allowed' : 'pointer',
              }}
            >
              <Save size={14} /> {loading ? 'Saving...' : saveLabel}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
