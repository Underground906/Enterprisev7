'use client';

import { Activity, Target, Users, Zap } from 'lucide-react';
import DashboardAnalytics from '@/components/boilerplates/DashboardAnalytics';

// ============================================================
// DEMO: Goal Health Dashboard (NAV_D)
// Shows the DashboardAnalytics boilerplate with goal metrics
// ============================================================

export default function GoalHealthPage() {
  return (
    <DashboardAnalytics
      title="Goal Health"
      description="Track progress across all active goals and objectives"
      periodOptions={['Last 7 days', 'Last 30 days', 'This quarter', 'This year']}
      activePeriod="Last 30 days"
      alerts={[
        { message: 'Property Connect London is behind schedule — 15% complete, target Feb 28', severity: 'warning' },
      ]}
      stats={[
        { label: 'Active Goals', value: 8, change: 12, icon: <Target size={16} /> },
        { label: 'Completion Rate', value: '34%', change: -5, color: 'var(--accent-amber)', icon: <Activity size={16} /> },
        { label: 'Tasks This Week', value: 47, change: 23, icon: <Zap size={16} /> },
        { label: 'Active Contributors', value: 3, change: 0, icon: <Users size={16} /> },
      ]}
      charts={[
        {
          title: 'Goal Progress by Priority',
          type: 'bar',
          data: [
            { label: 'P1 Property', value: 15, color: 'var(--accent-red)' },
            { label: 'P2 Chatbot', value: 5, color: 'var(--accent-amber)' },
            { label: 'P3 Scripts', value: 40, color: 'var(--accent-green)' },
            { label: 'P4 UI Lib', value: 65, color: 'var(--accent-blue)' },
            { label: 'P5 Fitness', value: 10, color: 'var(--accent-purple)' },
          ],
          height: 180,
        },
        {
          title: 'Task Distribution',
          type: 'donut',
          data: [
            { label: 'Completed', value: 34, color: 'var(--accent-green)' },
            { label: 'In Progress', value: 18, color: 'var(--accent-blue)' },
            { label: 'Blocked', value: 7, color: 'var(--accent-red)' },
            { label: 'Pending', value: 41, color: 'var(--bg-tertiary)' },
          ],
          height: 180,
        },
      ]}
      breakdownTitle="Goals Breakdown"
      breakdownColumns={[
        { key: 'goal', label: 'Goal' },
        { key: 'priority', label: 'Priority', width: '80px' },
        { key: 'progress', label: 'Progress', width: '100px' },
        { key: 'target', label: 'Target Date', width: '120px' },
        { key: 'status', label: 'Status', width: '100px' },
      ]}
      breakdownData={[
        {
          id: '1',
          cells: {
            goal: <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>Property Connect London MVP</span>,
            priority: <span style={{ color: 'var(--accent-red)', fontWeight: 500 }}>P1</span>,
            progress: (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
                  <div style={{ width: '15%', height: '100%', borderRadius: 2, background: 'var(--accent-red)' }} />
                </div>
                <span style={{ fontSize: 12 }}>15%</span>
              </div>
            ),
            target: '2026-02-28',
            status: <span style={{ padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-red-light)', color: 'var(--accent-red)', fontSize: 12, fontWeight: 500 }}>At Risk</span>,
          },
        },
        {
          id: '2',
          cells: {
            goal: <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>AI Chatbot Revenue Product</span>,
            priority: <span style={{ color: 'var(--accent-amber)', fontWeight: 500 }}>P2</span>,
            progress: (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
                  <div style={{ width: '5%', height: '100%', borderRadius: 2, background: 'var(--accent-amber)' }} />
                </div>
                <span style={{ fontSize: 12 }}>5%</span>
              </div>
            ),
            target: '2026-03-15',
            status: <span style={{ padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-amber-light)', color: '#92400E', fontSize: 12, fontWeight: 500 }}>Behind</span>,
          },
        },
        {
          id: '3',
          cells: {
            goal: <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>Enterprise OS Core Scripts</span>,
            priority: <span style={{ color: 'var(--accent-green)', fontWeight: 500 }}>P3</span>,
            progress: (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
                  <div style={{ width: '40%', height: '100%', borderRadius: 2, background: 'var(--accent-green)' }} />
                </div>
                <span style={{ fontSize: 12 }}>40%</span>
              </div>
            ),
            target: '2026-02-10',
            status: <span style={{ padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-amber-light)', color: '#92400E', fontSize: 12, fontWeight: 500 }}>Late</span>,
          },
        },
        {
          id: '4',
          cells: {
            goal: <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>UI Component Library</span>,
            priority: <span style={{ color: 'var(--accent-blue)', fontWeight: 500 }}>P4</span>,
            progress: (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
                  <div style={{ width: '65%', height: '100%', borderRadius: 2, background: 'var(--accent-blue)' }} />
                </div>
                <span style={{ fontSize: 12 }}>65%</span>
              </div>
            ),
            target: '2026-03-01',
            status: <span style={{ padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-green-light)', color: 'var(--accent-green)', fontSize: 12, fontWeight: 500 }}>On Track</span>,
          },
        },
        {
          id: '5',
          cells: {
            goal: <span style={{ fontWeight: 500, color: 'var(--text-primary)' }}>LeadEngine Platform</span>,
            priority: <span style={{ color: 'var(--accent-red)', fontWeight: 500 }}>P1</span>,
            progress: (
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <div style={{ width: 60, height: 4, borderRadius: 2, background: 'var(--bg-tertiary)' }}>
                  <div style={{ width: '0%', height: '100%', borderRadius: 2, background: 'var(--accent-purple)' }} />
                </div>
                <span style={{ fontSize: 12 }}>0%</span>
              </div>
            ),
            target: '2026-02-24',
            status: <span style={{ padding: '2px 8px', borderRadius: 'var(--radius-sm)', background: 'var(--accent-blue-light)', color: 'var(--accent-blue)', fontSize: 12, fontWeight: 500 }}>Starting</span>,
          },
        },
      ]}
      actions={[
        { label: 'Export Report', onClick: () => {} },
        { label: '+ New Goal', onClick: () => {}, variant: 'primary' },
      ]}
    />
  );
}
