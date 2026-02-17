'use client';

import { useState } from 'react';
import ChatFeed, { type ChatMessage, type ChatSuggestion } from '@/components/boilerplates/ChatFeed';

// ============================================================
// DEMO: AI Concierge (CMD_B)
// Shows the ChatFeed boilerplate with sample conversation
// ============================================================

const INITIAL_MESSAGES: ChatMessage[] = [
  {
    id: '1',
    role: 'system',
    content: 'Session started — Chief of Staff agent activated',
    timestamp: '14:32',
  },
  {
    id: '2',
    role: 'assistant',
    content: 'Good afternoon, John. I\'ve reviewed your current goals. Property Connect London is at 15% with the Feb 28 deadline approaching. LeadEngine Platform hasn\'t started yet but has a Feb 24 target. Would you like me to prioritise today\'s tasks based on these deadlines?',
    timestamp: '14:32',
    agent: 'Chief of Staff',
  },
  {
    id: '3',
    role: 'user',
    content: 'Yes, what should I focus on today? I have about 4 hours.',
    timestamp: '14:33',
  },
  {
    id: '4',
    role: 'assistant',
    content: 'Given 4 hours and your deadlines, here\'s my recommendation:\n\n1. **LeadEngine Foundation** (2 hours) — Set up the Next.js project, PostgreSQL schema, and basic API routes. This gets Day 1 of the 7-day sprint done.\n\n2. **Property Connect API** (1.5 hours) — Connect the chatbot to the property listing data source. This is the critical path item.\n\n3. **Session Log & Review** (30 min) — Document decisions and update goal health.\n\nShall I create tasks in the queue for these?',
    timestamp: '14:33',
    agent: 'Chief of Staff',
  },
  {
    id: '5',
    role: 'user',
    content: 'Do it. Also, what\'s the status on the UI component library?',
    timestamp: '14:34',
  },
  {
    id: '6',
    role: 'assistant',
    content: 'Tasks queued. For the UI Component Library:\n\n- **Progress:** 65% complete\n- **Figma exports:** 48 Brainwave screens done, batch running for remaining 37 kits\n- **Boilerplates built:** 7 of 15 (DashboardList, CardGrid, AuthSplit, DashboardAnalytics, MultiStepWizard, SearchResults, ChatFeed)\n- **Remaining:** SplitView, ApprovalQueue, DashboardForm, ReadOnlyDigest, Timeline, Canvas, TreeVis\n- **Status:** On track for March 1 target\n\nThe boilerplates cover all 48 screens across your 8 modules. Shall I pull the detailed breakdown?',
    timestamp: '14:34',
    agent: 'Chief of Staff',
  },
];

const SUGGESTIONS: ChatSuggestion[] = [
  { label: 'Daily priorities', prompt: 'What should I focus on today?' },
  { label: 'Goal status', prompt: 'Give me a status update on all active goals' },
  { label: 'Knowledge search', prompt: 'Search for brand voice guidelines' },
  { label: 'Sprint plan', prompt: 'Create a sprint plan for this week' },
];

export default function AIConcierge() {
  const [messages, setMessages] = useState<ChatMessage[]>(INITIAL_MESSAGES);
  const [loading, setLoading] = useState(false);

  const handleSend = (content: string) => {
    const userMsg: ChatMessage = {
      id: `user-${Date.now()}`,
      role: 'user',
      content,
      timestamp: new Date().toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }),
    };
    setMessages((prev) => [...prev, userMsg]);
    setLoading(true);

    // Simulate response
    setTimeout(() => {
      const reply: ChatMessage = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: `I'll look into that. Processing your request: "${content}"\n\nThis is a demo — in production, this connects to the Enterprise OS knowledge base via RAG search and routes to the appropriate specialist agent.`,
        timestamp: new Date().toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' }),
        agent: 'Chief of Staff',
      };
      setMessages((prev) => [...prev, reply]);
      setLoading(false);
    }, 1500);
  };

  return (
    <ChatFeed
      agentName="Chief of Staff"
      subtitle="Strategic operations & daily prioritisation"
      messages={messages}
      onSend={handleSend}
      placeholder="Ask anything about your goals, tasks, or knowledge base..."
      suggestions={SUGGESTIONS}
      loading={loading}
      showTimestamps
      onCopy={(content) => navigator.clipboard.writeText(content)}
      sidebar={
        <div style={{ padding: '16px' }}>
          <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginBottom: 16 }}>Active Agents</div>
          {[
            { name: 'Chief of Staff', status: 'Active', color: 'var(--accent-green)' },
            { name: 'SEO Lead', status: 'Idle', color: 'var(--text-tertiary)' },
            { name: 'Copy Chief', status: 'Idle', color: 'var(--text-tertiary)' },
            { name: 'Data Engineer', status: 'Idle', color: 'var(--text-tertiary)' },
          ].map((agent) => (
            <div
              key={agent.name}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                padding: '8px 0',
                borderBottom: '1px solid var(--border-subtle)',
              }}
            >
              <div style={{ width: 8, height: 8, borderRadius: '50%', background: agent.color }} />
              <div>
                <div style={{ fontSize: 13, color: 'var(--text-primary)' }}>{agent.name}</div>
                <div style={{ fontSize: 11, color: 'var(--text-tertiary)' }}>{agent.status}</div>
              </div>
            </div>
          ))}

          <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-primary)', marginTop: 24, marginBottom: 12 }}>Quick Actions</div>
          {['New Goal', 'Search Knowledge', 'View Tasks', 'Export Session'].map((action) => (
            <button
              key={action}
              style={{
                display: 'block',
                width: '100%',
                padding: '8px 12px',
                marginBottom: 6,
                borderRadius: 'var(--radius-md)',
                border: '1px solid var(--border-default)',
                background: 'var(--bg-card)',
                color: 'var(--text-secondary)',
                fontSize: 13,
                cursor: 'pointer',
                textAlign: 'left',
              }}
            >
              {action}
            </button>
          ))}
        </div>
      }
    />
  );
}
