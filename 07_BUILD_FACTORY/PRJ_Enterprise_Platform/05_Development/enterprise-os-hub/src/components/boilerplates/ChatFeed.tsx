'use client';

import { useState, useRef, useEffect } from 'react';
import { Send, Paperclip, Bot, User, MoreHorizontal, Copy, ThumbsUp, ThumbsDown, Sparkles } from 'lucide-react';

// ============================================================
// CHAT/FEED BOILERPLATE
// Used by: AI Concierge (CMD_B), Thread Viewer, Session Chat,
//          any screen with message history + input
// Layout: Message list + Input bar (+ optional sidebar)
// ============================================================

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp?: string;
  agent?: string;
  attachments?: { name: string; type: string }[];
  reactions?: { thumbsUp?: boolean; thumbsDown?: boolean };
}

export interface ChatSuggestion {
  label: string;
  prompt: string;
}

interface ChatFeedProps {
  title?: string;
  subtitle?: string;
  messages: ChatMessage[];
  onSend: (message: string, attachments?: File[]) => void;
  placeholder?: string;
  suggestions?: ChatSuggestion[];
  loading?: boolean;
  agentName?: string;
  agentAvatar?: React.ReactNode;
  showTimestamps?: boolean;
  onReaction?: (messageId: string, reaction: 'thumbsUp' | 'thumbsDown') => void;
  onCopy?: (content: string) => void;
  sidebar?: React.ReactNode;
  maxWidth?: number;
}

function MessageBubble({
  message,
  showTimestamps,
  onReaction,
  onCopy,
}: {
  message: ChatMessage;
  showTimestamps?: boolean;
  onReaction?: (messageId: string, reaction: 'thumbsUp' | 'thumbsDown') => void;
  onCopy?: (content: string) => void;
}) {
  const isUser = message.role === 'user';
  const isSystem = message.role === 'system';
  const [showActions, setShowActions] = useState(false);

  if (isSystem) {
    return (
      <div style={{ display: 'flex', justifyContent: 'center', padding: '8px 0' }}>
        <span style={{ fontSize: 12, color: 'var(--text-tertiary)', background: 'var(--bg-tertiary)', padding: '4px 12px', borderRadius: 12 }}>
          {message.content}
        </span>
      </div>
    );
  }

  return (
    <div
      style={{
        display: 'flex',
        gap: 12,
        flexDirection: isUser ? 'row-reverse' : 'row',
        alignItems: 'flex-start',
        padding: '4px 0',
      }}
      onMouseEnter={() => setShowActions(true)}
      onMouseLeave={() => setShowActions(false)}
    >
      {/* Avatar */}
      <div
        style={{
          width: 32,
          height: 32,
          borderRadius: '50%',
          background: isUser ? 'var(--accent-purple)' : 'var(--accent-green)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#fff',
          flexShrink: 0,
        }}
      >
        {isUser ? <User size={14} /> : <Bot size={14} />}
      </div>

      {/* Message body */}
      <div style={{ maxWidth: '70%', display: 'flex', flexDirection: 'column', gap: 4 }}>
        {/* Agent label */}
        {!isUser && message.agent && (
          <span style={{ fontSize: 11, fontWeight: 500, color: 'var(--accent-green)' }}>{message.agent}</span>
        )}

        {/* Content */}
        <div
          style={{
            padding: '10px 14px',
            borderRadius: isUser ? '12px 12px 4px 12px' : '12px 12px 12px 4px',
            background: isUser ? 'var(--accent-purple)' : 'var(--bg-card)',
            color: isUser ? '#fff' : 'var(--text-primary)',
            fontSize: 14,
            lineHeight: 1.6,
            border: isUser ? 'none' : '1px solid var(--border-default)',
            boxShadow: 'var(--shadow-sm)',
          }}
        >
          {message.content}
        </div>

        {/* Attachments */}
        {message.attachments && message.attachments.length > 0 && (
          <div style={{ display: 'flex', gap: 6, flexWrap: 'wrap', marginTop: 4 }}>
            {message.attachments.map((att, i) => (
              <span
                key={i}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 4,
                  padding: '4px 10px',
                  borderRadius: 'var(--radius-sm)',
                  background: 'var(--bg-tertiary)',
                  border: '1px solid var(--border-default)',
                  fontSize: 12,
                  color: 'var(--text-secondary)',
                }}
              >
                <Paperclip size={10} /> {att.name}
              </span>
            ))}
          </div>
        )}

        {/* Meta + Actions */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          {showTimestamps && message.timestamp && (
            <span style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>{message.timestamp}</span>
          )}
          {showActions && !isUser && (
            <div style={{ display: 'flex', gap: 4 }}>
              <button
                onClick={() => onCopy?.(message.content)}
                style={{ border: 'none', background: 'transparent', cursor: 'pointer', color: 'var(--text-tertiary)', padding: 2 }}
                title="Copy"
              >
                <Copy size={12} />
              </button>
              <button
                onClick={() => onReaction?.(message.id, 'thumbsUp')}
                style={{
                  border: 'none',
                  background: 'transparent',
                  cursor: 'pointer',
                  color: message.reactions?.thumbsUp ? 'var(--accent-green)' : 'var(--text-tertiary)',
                  padding: 2,
                }}
              >
                <ThumbsUp size={12} />
              </button>
              <button
                onClick={() => onReaction?.(message.id, 'thumbsDown')}
                style={{
                  border: 'none',
                  background: 'transparent',
                  cursor: 'pointer',
                  color: message.reactions?.thumbsDown ? 'var(--accent-red)' : 'var(--text-tertiary)',
                  padding: 2,
                }}
              >
                <ThumbsDown size={12} />
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function TypingIndicator() {
  return (
    <div style={{ display: 'flex', gap: 12, alignItems: 'flex-start', padding: '4px 0' }}>
      <div
        style={{
          width: 32,
          height: 32,
          borderRadius: '50%',
          background: 'var(--accent-green)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#fff',
          flexShrink: 0,
        }}
      >
        <Bot size={14} />
      </div>
      <div
        style={{
          padding: '12px 16px',
          borderRadius: '12px 12px 12px 4px',
          background: 'var(--bg-card)',
          border: '1px solid var(--border-default)',
          display: 'flex',
          gap: 4,
        }}
      >
        {[0, 1, 2].map((i) => (
          <div
            key={i}
            style={{
              width: 6,
              height: 6,
              borderRadius: '50%',
              background: 'var(--text-tertiary)',
              animation: `pulse 1.4s ease-in-out ${i * 0.2}s infinite`,
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default function ChatFeed({
  title,
  subtitle,
  messages,
  onSend,
  placeholder = 'Type a message...',
  suggestions,
  loading,
  agentName,
  showTimestamps = true,
  onReaction,
  onCopy,
  sidebar,
  maxWidth,
}: ChatFeedProps) {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input.trim());
    setInput('');
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const isEmpty = messages.length === 0;

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      {/* Main Chat */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
        {/* Header */}
        {(title || agentName) && (
          <div
            style={{
              padding: '14px 24px',
              borderBottom: '1px solid var(--border-default)',
              background: 'var(--bg-secondary)',
              display: 'flex',
              alignItems: 'center',
              gap: 12,
            }}
          >
            {agentName && (
              <div
                style={{
                  width: 36,
                  height: 36,
                  borderRadius: '50%',
                  background: 'var(--accent-green)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  color: '#fff',
                }}
              >
                <Sparkles size={16} />
              </div>
            )}
            <div>
              <div style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-primary)' }}>
                {title || agentName}
              </div>
              {subtitle && (
                <div style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>{subtitle}</div>
              )}
            </div>
          </div>
        )}

        {/* Messages */}
        <div
          style={{
            flex: 1,
            overflow: 'auto',
            padding: '24px',
            display: 'flex',
            flexDirection: 'column',
            gap: 16,
          }}
        >
          <div style={{ maxWidth: maxWidth || 800, width: '100%', margin: '0 auto', flex: 1, display: 'flex', flexDirection: 'column', gap: 16 }}>
            {isEmpty && suggestions && (
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 24 }}>
                <div style={{ textAlign: 'center' }}>
                  <div
                    style={{
                      width: 56,
                      height: 56,
                      borderRadius: '50%',
                      background: 'var(--accent-green)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      color: '#fff',
                      margin: '0 auto 16px',
                    }}
                  >
                    <Sparkles size={24} />
                  </div>
                  <div style={{ fontSize: 16, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 4 }}>
                    {agentName || 'AI Assistant'}
                  </div>
                  <div style={{ fontSize: 13, color: 'var(--text-tertiary)' }}>
                    Ask me anything about your Enterprise OS knowledge base
                  </div>
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10, maxWidth: 480, width: '100%' }}>
                  {suggestions.map((s) => (
                    <button
                      key={s.label}
                      onClick={() => {
                        setInput(s.prompt);
                        onSend(s.prompt);
                      }}
                      style={{
                        padding: '12px 16px',
                        borderRadius: 'var(--radius-md)',
                        border: '1px solid var(--border-default)',
                        background: 'var(--bg-card)',
                        cursor: 'pointer',
                        textAlign: 'left',
                        transition: 'border-color 0.15s, box-shadow 0.15s',
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.borderColor = 'var(--border-accent)';
                        e.currentTarget.style.boxShadow = 'var(--shadow-sm)';
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.borderColor = 'var(--border-default)';
                        e.currentTarget.style.boxShadow = 'none';
                      }}
                    >
                      <div style={{ fontSize: 13, fontWeight: 500, color: 'var(--text-primary)', marginBottom: 4 }}>
                        {s.label}
                      </div>
                      <div style={{ fontSize: 12, color: 'var(--text-tertiary)' }}>
                        {s.prompt}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {messages.map((msg) => (
              <MessageBubble
                key={msg.id}
                message={msg}
                showTimestamps={showTimestamps}
                onReaction={onReaction}
                onCopy={onCopy}
              />
            ))}

            {loading && <TypingIndicator />}
            <div ref={messagesEndRef} />
          </div>
        </div>

        {/* Input */}
        <div style={{ padding: '16px 24px', borderTop: '1px solid var(--border-default)', background: 'var(--bg-secondary)' }}>
          <div style={{ maxWidth: maxWidth || 800, margin: '0 auto' }}>
            <div
              style={{
                display: 'flex',
                alignItems: 'flex-end',
                gap: 10,
                padding: '10px 14px',
                border: '1px solid var(--border-default)',
                borderRadius: 'var(--radius-lg)',
                background: 'var(--bg-card)',
                boxShadow: 'var(--shadow-sm)',
              }}
            >
              <button
                style={{
                  border: 'none',
                  background: 'transparent',
                  cursor: 'pointer',
                  color: 'var(--text-tertiary)',
                  padding: 4,
                  flexShrink: 0,
                }}
                title="Attach file"
              >
                <Paperclip size={16} />
              </button>
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={placeholder}
                rows={1}
                style={{
                  border: 'none',
                  outline: 'none',
                  background: 'transparent',
                  fontSize: 14,
                  color: 'var(--text-primary)',
                  width: '100%',
                  resize: 'none',
                  fontFamily: 'inherit',
                  lineHeight: 1.5,
                  maxHeight: 120,
                  overflow: 'auto',
                }}
              />
              <button
                onClick={handleSend}
                disabled={!input.trim()}
                style={{
                  width: 32,
                  height: 32,
                  borderRadius: '50%',
                  border: 'none',
                  background: input.trim() ? 'var(--accent-purple)' : 'var(--bg-tertiary)',
                  color: input.trim() ? '#fff' : 'var(--text-tertiary)',
                  cursor: input.trim() ? 'pointer' : 'not-allowed',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flexShrink: 0,
                  transition: 'background 0.15s',
                }}
              >
                <Send size={14} />
              </button>
            </div>
            <div style={{ fontSize: 11, color: 'var(--text-tertiary)', textAlign: 'center', marginTop: 8 }}>
              Press Enter to send, Shift+Enter for new line
            </div>
          </div>
        </div>
      </div>

      {/* Optional Sidebar */}
      {sidebar && (
        <div
          style={{
            width: 300,
            minWidth: 300,
            borderLeft: '1px solid var(--border-default)',
            background: 'var(--bg-secondary)',
            overflow: 'auto',
          }}
        >
          {sidebar}
        </div>
      )}
    </div>
  );
}
