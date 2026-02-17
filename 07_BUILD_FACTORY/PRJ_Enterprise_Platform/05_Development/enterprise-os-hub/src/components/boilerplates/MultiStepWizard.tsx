'use client';

import { useState } from 'react';
import { Check, ChevronLeft, ChevronRight } from 'lucide-react';

// ============================================================
// MULTI-STEP WIZARD BOILERPLATE
// Used by: Goal Intake (NAV_A), Document Generator (TPL_B),
//          Register (AUTH_B), Project Setup, Onboarding flows
// Layout: Step indicator + Form content + Navigation buttons
// ============================================================

export interface WizardStep {
  key: string;
  title: string;
  description?: string;
  icon?: React.ReactNode;
  content: React.ReactNode;
  validate?: () => boolean;
}

interface MultiStepWizardProps {
  title?: string;
  subtitle?: string;
  steps: WizardStep[];
  onComplete: (data: Record<string, unknown>) => void;
  onCancel?: () => void;
  completeLabel?: string;
  showSummary?: boolean;
  summary?: React.ReactNode;
  maxWidth?: number;
}

export default function MultiStepWizard({
  title,
  subtitle,
  steps,
  onComplete,
  onCancel,
  completeLabel = 'Complete',
  showSummary,
  summary,
  maxWidth = 720,
}: MultiStepWizardProps) {
  const [currentStep, setCurrentStep] = useState(0);
  const [completedSteps, setCompletedSteps] = useState<Set<number>>(new Set());
  const [isCompleting, setIsCompleting] = useState(false);

  const isLast = currentStep === steps.length - 1;
  const isSummaryStep = showSummary && currentStep === steps.length;

  const goNext = () => {
    const step = steps[currentStep];
    if (step.validate && !step.validate()) return;

    setCompletedSteps((prev) => new Set(prev).add(currentStep));

    if (isLast && showSummary) {
      setCurrentStep(steps.length);
    } else if (isLast) {
      onComplete({});
    } else {
      setCurrentStep((s) => s + 1);
    }
  };

  const goBack = () => {
    if (currentStep > 0) setCurrentStep((s) => s - 1);
  };

  const goToStep = (index: number) => {
    if (index <= currentStep || completedSteps.has(index)) {
      setCurrentStep(index);
    }
  };

  const handleComplete = () => {
    setIsCompleting(true);
    onComplete({});
  };

  return (
    <div
      style={{
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
        background: 'var(--bg-primary)',
      }}
    >
      {/* Header */}
      {(title || onCancel) && (
        <div
          style={{
            padding: '20px 24px',
            borderBottom: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}
        >
          <div>
            {title && <h2 style={{ fontSize: 18, fontWeight: 600, color: 'var(--text-primary)', margin: 0 }}>{title}</h2>}
            {subtitle && <p style={{ fontSize: 13, color: 'var(--text-tertiary)', margin: '4px 0 0' }}>{subtitle}</p>}
          </div>
          {onCancel && (
            <button
              onClick={onCancel}
              style={{
                padding: '8px 16px',
                borderRadius: 'var(--radius-md)',
                border: '1px solid var(--border-default)',
                background: 'var(--bg-secondary)',
                color: 'var(--text-secondary)',
                fontSize: 13,
                cursor: 'pointer',
              }}
            >
              Cancel
            </button>
          )}
        </div>
      )}

      {/* Step Indicator */}
      <div style={{ padding: '24px 24px 0', display: 'flex', justifyContent: 'center' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 0, maxWidth }}>
          {steps.map((step, i) => {
            const isActive = i === currentStep;
            const isComplete = completedSteps.has(i);
            const isClickable = i <= currentStep || isComplete;

            return (
              <div key={step.key} style={{ display: 'flex', alignItems: 'center' }}>
                {/* Step circle + label */}
                <div
                  onClick={() => isClickable && goToStep(i)}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: 8,
                    cursor: isClickable ? 'pointer' : 'default',
                    opacity: isActive || isComplete ? 1 : 0.4,
                    minWidth: 80,
                  }}
                >
                  <div
                    style={{
                      width: 36,
                      height: 36,
                      borderRadius: '50%',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      background: isComplete
                        ? 'var(--accent-green)'
                        : isActive
                        ? 'var(--accent-purple)'
                        : 'var(--bg-tertiary)',
                      color: isComplete || isActive ? '#fff' : 'var(--text-tertiary)',
                      fontSize: 14,
                      fontWeight: 600,
                      transition: 'all 0.2s',
                      border: isActive ? '2px solid var(--accent-purple)' : '2px solid transparent',
                      boxShadow: isActive ? '0 0 0 4px var(--accent-purple-light)' : 'none',
                    }}
                  >
                    {isComplete ? <Check size={16} /> : step.icon || i + 1}
                  </div>
                  <div style={{ fontSize: 12, fontWeight: isActive ? 600 : 400, color: isActive ? 'var(--text-primary)' : 'var(--text-tertiary)', textAlign: 'center', whiteSpace: 'nowrap' }}>
                    {step.title}
                  </div>
                </div>

                {/* Connector line */}
                {i < steps.length - 1 && (
                  <div
                    style={{
                      width: 60,
                      height: 2,
                      background: isComplete ? 'var(--accent-green)' : 'var(--border-default)',
                      marginBottom: 24,
                      transition: 'background 0.2s',
                    }}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Step Content */}
      <div style={{ flex: 1, overflow: 'auto', display: 'flex', justifyContent: 'center', padding: '32px 24px' }}>
        <div style={{ width: '100%', maxWidth }}>
          {isSummaryStep ? (
            <div>
              <h3 style={{ fontSize: 16, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 8 }}>Review & Confirm</h3>
              <p style={{ fontSize: 13, color: 'var(--text-tertiary)', marginBottom: 24 }}>Review your selections before completing.</p>
              {summary}
            </div>
          ) : (
            <>
              {steps[currentStep]?.description && (
                <p style={{ fontSize: 13, color: 'var(--text-tertiary)', marginBottom: 24 }}>
                  {steps[currentStep].description}
                </p>
              )}
              {steps[currentStep]?.content}
            </>
          )}
        </div>
      </div>

      {/* Navigation Footer */}
      <div
        style={{
          padding: '16px 24px',
          borderTop: '1px solid var(--border-default)',
          background: 'var(--bg-secondary)',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
        }}
      >
        <button
          onClick={goBack}
          disabled={currentStep === 0}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            padding: '10px 20px',
            borderRadius: 'var(--radius-md)',
            border: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            color: currentStep === 0 ? 'var(--text-tertiary)' : 'var(--text-primary)',
            fontSize: 13,
            fontWeight: 500,
            cursor: currentStep === 0 ? 'not-allowed' : 'pointer',
            opacity: currentStep === 0 ? 0.5 : 1,
          }}
        >
          <ChevronLeft size={14} /> Back
        </button>

        <div style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>
          Step {Math.min(currentStep + 1, steps.length)} of {steps.length}
        </div>

        <button
          onClick={isSummaryStep ? handleComplete : goNext}
          disabled={isCompleting}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            padding: '10px 24px',
            borderRadius: 'var(--radius-md)',
            border: 'none',
            background: (isSummaryStep || isLast) ? 'var(--accent-green)' : 'var(--accent-purple)',
            color: '#fff',
            fontSize: 13,
            fontWeight: 500,
            cursor: isCompleting ? 'not-allowed' : 'pointer',
          }}
        >
          {isSummaryStep ? completeLabel : isLast && !showSummary ? completeLabel : 'Next'}
          {!isSummaryStep && !isLast && <ChevronRight size={14} />}
        </button>
      </div>
    </div>
  );
}
