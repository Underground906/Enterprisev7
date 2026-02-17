'use client';

import { useState } from 'react';

// ============================================================
// AUTH SPLIT — Pixel-matched to Brainwave 2.0 sign_in.png
//
// LEFT:  White bg, centered form (~360px), "Sign in to [App]"
//        Google SSO button (outlined), email/password fields,
//        dark pill "Sign in" button, "Need an account?" link
//
// RIGHT: Full-bleed hero image with optional floating chat input
//        at bottom. Speaker icon top-left of image area.
// ============================================================

interface AuthField {
  key: string;
  label: string;
  type: 'text' | 'email' | 'password';
  placeholder?: string;
  required?: boolean;
  rightLink?: { label: string; href: string };
}

interface AuthSplitProps {
  title: string;
  fields: AuthField[];
  submitLabel: string;
  onSubmit: (values: Record<string, string>) => void;
  loading?: boolean;
  error?: string;
  footerLink?: { label: string; href: string };
  ssoProviders?: { name: string; icon?: React.ReactNode; onClick: () => void }[];
  ssoSeparator?: string;
  heroImage?: string;
  heroAlt?: string;
  chatInput?: {
    placeholder?: string;
    brandLabel?: string;
  };
  promoText?: string;
}

export default function AuthSplit({
  title,
  fields,
  submitLabel,
  onSubmit,
  loading,
  error,
  footerLink,
  ssoProviders,
  ssoSeparator = 'Or sign in with email',
  heroImage = '/figma-exports/6hCuwRI0GsBmIOJelAVpND/screens/canvas_images_canvas_full_screen_01.png',
  chatInput,
  promoText,
}: AuthSplitProps) {
  const [values, setValues] = useState<Record<string, string>>({});

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(values);
  };

  return (
    <div style={{ display: 'flex', minHeight: '100vh', background: '#fff' }}>
      {/* ---- LEFT: Form ---- */}
      <div
        style={{
          flex: 1,
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '40px',
        }}
      >
        <div style={{ width: '100%', maxWidth: 360 }}>
          {/* Title — Brainwave uses ~32px, weight 400, tight spacing */}
          <h1
            style={{
              fontSize: 32,
              fontWeight: 400,
              color: 'var(--shade-9)',
              letterSpacing: '-0.03em',
              lineHeight: 1.2,
              margin: '0 0 32px',
            }}
          >
            {title}
          </h1>

          {/* Error */}
          {error && (
            <div
              style={{
                padding: '10px 14px',
                borderRadius: 10,
                background: 'var(--accent-red-light)',
                color: 'var(--accent-red)',
                fontSize: 13,
                marginBottom: 20,
              }}
            >
              {error}
            </div>
          )}

          {/* SSO Providers — Brainwave: outlined button, 1px border, rounded 10px */}
          {ssoProviders && ssoProviders.length > 0 && (
            <>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginBottom: 24 }}>
                {ssoProviders.map((provider, i) => (
                  <button
                    key={i}
                    onClick={provider.onClick}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: 10,
                      padding: '12px 16px',
                      border: '1px solid var(--shade-4)',
                      borderRadius: 10,
                      background: '#fff',
                      fontSize: 14,
                      fontWeight: 500,
                      color: 'var(--shade-7)',
                      cursor: 'pointer',
                      letterSpacing: '-0.01em',
                      transition: 'background 0.15s',
                    }}
                    onMouseEnter={(e) => { e.currentTarget.style.background = 'var(--shade-2)'; }}
                    onMouseLeave={(e) => { e.currentTarget.style.background = '#fff'; }}
                  >
                    {provider.icon}
                    Sign in with {provider.name}
                  </button>
                ))}
              </div>
              {/* Separator — Brainwave: plain centered text, no lines */}
              <div
                style={{
                  textAlign: 'center',
                  fontSize: 13,
                  color: 'var(--shade-6)',
                  marginBottom: 24,
                  letterSpacing: '-0.01em',
                }}
              >
                {ssoSeparator}
              </div>
            </>
          )}

          {/* Form Fields */}
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
            {fields.map((field) => (
              <div key={field.key}>
                {/* Label row — label left, optional right link */}
                <div
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'baseline',
                    marginBottom: 8,
                  }}
                >
                  <label
                    style={{
                      fontSize: 13,
                      fontWeight: 500,
                      color: 'var(--shade-9)',
                      letterSpacing: '-0.01em',
                    }}
                  >
                    {field.label}
                  </label>
                  {field.rightLink && (
                    <a
                      href={field.rightLink.href}
                      style={{
                        fontSize: 13,
                        color: 'var(--shade-6)',
                        textDecoration: 'none',
                        letterSpacing: '-0.01em',
                      }}
                    >
                      {field.rightLink.label}
                    </a>
                  )}
                </div>
                {/* Input — Brainwave: 1px border #ECECEC, rounded 10px, 46px height */}
                <input
                  type={field.type}
                  placeholder={field.placeholder}
                  required={field.required}
                  value={values[field.key] || ''}
                  onChange={(e) => setValues((v) => ({ ...v, [field.key]: e.target.value }))}
                  style={{
                    width: '100%',
                    padding: '12px 16px',
                    border: '1px solid var(--shade-4)',
                    borderRadius: 10,
                    fontSize: 14,
                    color: 'var(--shade-9)',
                    background: '#fff',
                    outline: 'none',
                    boxSizing: 'border-box',
                    letterSpacing: '-0.01em',
                    transition: 'border-color 0.15s',
                  }}
                  onFocus={(e) => { e.currentTarget.style.borderColor = 'var(--shade-6)'; }}
                  onBlur={(e) => { e.currentTarget.style.borderColor = 'var(--shade-4)'; }}
                />
              </div>
            ))}

            {/* Submit — Brainwave: dark bg #222, white text, fully rounded pill */}
            <button
              type="submit"
              disabled={loading}
              style={{
                padding: '14px 20px',
                borderRadius: 9999,
                border: 'none',
                background: loading ? 'var(--shade-6)' : 'var(--shade-8)',
                color: '#fff',
                fontSize: 14,
                fontWeight: 500,
                cursor: loading ? 'not-allowed' : 'pointer',
                marginTop: 4,
                letterSpacing: '-0.01em',
                transition: 'background 0.15s',
              }}
            >
              {loading ? 'Please wait...' : submitLabel}
            </button>
          </form>

          {/* Footer Link — Brainwave: centered, gray text */}
          {footerLink && (
            <div style={{ textAlign: 'center', marginTop: 20 }}>
              <a
                href={footerLink.href}
                style={{
                  fontSize: 13,
                  color: 'var(--shade-6)',
                  textDecoration: 'none',
                  letterSpacing: '-0.01em',
                }}
              >
                {footerLink.label}
              </a>
            </div>
          )}
        </div>
      </div>

      {/* ---- RIGHT: Hero Image ---- */}
      <div
        style={{
          flex: 1,
          position: 'relative',
          overflow: 'hidden',
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        {/* Full-bleed image — Brainwave uses rounded top-left on the image container */}
        <div
          style={{
            flex: 1,
            position: 'relative',
            borderRadius: '20px 0 0 0',
            overflow: 'hidden',
            background: 'var(--shade-3)',
          }}
        >
          <img
            src={heroImage}
            alt="Hero"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'cover',
              display: 'block',
            }}
          />

          {/* Sound icon — top-left of image area (Brainwave detail) */}
          <button
            style={{
              position: 'absolute',
              top: 16,
              left: 16,
              width: 36,
              height: 36,
              borderRadius: '50%',
              border: 'none',
              background: 'rgba(255,255,255,0.9)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              cursor: 'pointer',
              fontSize: 16,
              color: 'var(--shade-7)',
            }}
          >
            &#x1F50A;
          </button>
        </div>

        {/* Floating chat input — Brainwave sign-in has this at bottom */}
        {chatInput && (
          <div
            style={{
              position: 'absolute',
              bottom: 40,
              left: '50%',
              transform: 'translateX(-50%)',
              width: '85%',
              maxWidth: 520,
            }}
          >
            <div
              style={{
                background: '#fff',
                borderRadius: 16,
                padding: '16px 16px 12px',
                boxShadow: '0 4px 24px rgba(0,0,0,0.12)',
              }}
            >
              {/* Prompt text area */}
              <div
                style={{
                  fontSize: 14,
                  color: 'var(--shade-6)',
                  lineHeight: 1.5,
                  marginBottom: 12,
                  letterSpacing: '-0.01em',
                }}
              >
                {chatInput.placeholder || 'Describe what you want to create...'}
              </div>
              {/* Toolbar row */}
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                {/* + button */}
                <button
                  style={{
                    width: 32,
                    height: 32,
                    borderRadius: '50%',
                    border: '1px solid var(--shade-4)',
                    background: '#fff',
                    cursor: 'pointer',
                    fontSize: 16,
                    color: 'var(--shade-7)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  +
                </button>
                {/* Inspiration pill */}
                <button
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                    padding: '6px 12px',
                    borderRadius: 9999,
                    border: '1px solid var(--shade-4)',
                    background: '#fff',
                    fontSize: 13,
                    color: 'var(--shade-7)',
                    cursor: 'pointer',
                    fontWeight: 400,
                    letterSpacing: '-0.01em',
                  }}
                >
                  <span style={{ color: 'var(--bw-green)' }}>&#x2728;</span>
                  Inspiration
                  <span style={{ fontSize: 10, color: 'var(--shade-6)' }}>&#x25BE;</span>
                </button>
                {/* Brand pill */}
                <button
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                    padding: '6px 12px',
                    borderRadius: 9999,
                    border: '1px solid var(--shade-4)',
                    background: '#fff',
                    fontSize: 13,
                    color: 'var(--shade-7)',
                    cursor: 'pointer',
                    fontWeight: 400,
                    letterSpacing: '-0.01em',
                  }}
                >
                  {chatInput.brandLabel || 'Enterprise OS'}
                  <span style={{ fontSize: 10, color: 'var(--shade-6)' }}>&#x25BE;</span>
                </button>
                <div style={{ flex: 1 }} />
                {/* Mic icon */}
                <button
                  style={{
                    width: 32,
                    height: 32,
                    borderRadius: '50%',
                    border: 'none',
                    background: 'transparent',
                    cursor: 'pointer',
                    fontSize: 16,
                    color: 'var(--shade-6)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  &#x1F3A4;
                </button>
                {/* Send button — dark circle with up arrow */}
                <button
                  style={{
                    width: 36,
                    height: 36,
                    borderRadius: '50%',
                    border: 'none',
                    background: 'var(--shade-8)',
                    cursor: 'pointer',
                    color: '#fff',
                    fontSize: 16,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                  }}
                >
                  &#x2191;
                </button>
              </div>
            </div>
            {/* Promo text below chat */}
            {promoText && (
              <div
                style={{
                  textAlign: 'center',
                  fontSize: 12,
                  color: 'rgba(255,255,255,0.7)',
                  marginTop: 12,
                  letterSpacing: '-0.01em',
                }}
              >
                {promoText}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
