// Enterprise OS V7 — Module definitions and constants
// This is the single source of truth for module metadata in the app

export const V7_ROOT = process.env.V7_ROOT || 'C:\\Users\\under\\Downloads\\ENTERPRISE_OS_V7';

export interface Module {
  id: string;
  number: string;
  name: string;
  organ: string;
  description: string;
  folder: string;
  color: string;
  icon: string; // lucide icon name
}

export const MODULES: Module[] = [
  {
    id: 'system-root',
    number: '00',
    name: 'System Root',
    organ: 'Spine & Skeleton',
    description: 'Governance, master context, naming rules',
    folder: '00_SYSTEM_ROOT',
    color: '#6366F1',
    icon: 'Shield',
  },
  {
    id: 'navigation',
    number: '01',
    name: 'Navigation Centre',
    organ: 'Brain',
    description: 'Goals, state snapshots, priorities',
    folder: '01_NAVIGATION_CENTRE',
    color: '#8B5CF6',
    icon: 'Brain',
  },
  {
    id: 'command-deck',
    number: '02',
    name: 'Command Deck',
    organ: 'Hands',
    description: 'Sessions, agent workspaces, task queue',
    folder: '02_COMMAND_DECK',
    color: '#EC4899',
    icon: 'Terminal',
  },
  {
    id: 'core-engine',
    number: '03',
    name: 'Core Engine',
    organ: 'Nervous System',
    description: 'Scripts, indices, routing engine',
    folder: '03_CORE_ENGINE',
    color: '#06B6D4',
    icon: 'Cpu',
  },
  {
    id: 'knowledge-library',
    number: '04',
    name: 'Knowledge Library',
    organ: 'Stomach',
    description: 'Intake, extraction pipeline, RAG bundles',
    folder: '04_KNOWLEDGE_LIBRARY',
    color: '#F59E0B',
    icon: 'BookOpen',
  },
  {
    id: 'template-hub',
    number: '05',
    name: 'Template Hub',
    organ: 'DNA',
    description: 'Reusable templates for agents, docs, prompts',
    folder: '05_TEMPLATE_HUB',
    color: '#10B981',
    icon: 'Dna',
  },
  {
    id: 'domain-pillars',
    number: '06',
    name: 'Domain Pillars',
    organ: 'Organs',
    description: '23 specialist knowledge domains',
    folder: '06_DOMAIN_PILLARS',
    color: '#3B82F6',
    icon: 'Layers',
  },
  {
    id: 'build-factory',
    number: '07',
    name: 'Build Factory',
    organ: 'Kinetic Limbs',
    description: 'Active platform builds',
    folder: '07_BUILD_FACTORY',
    color: '#EF4444',
    icon: 'Hammer',
  },
  {
    id: 'operations',
    number: '08',
    name: 'Operations',
    organ: 'Immune System',
    description: 'Post-launch: marketing, metrics, legal',
    folder: '08_OPERATIONS',
    color: '#0B8C00',
    icon: 'Activity',
  },
];

export function getModuleByFolder(folder: string): Module | undefined {
  return MODULES.find(m => m.folder === folder);
}

export function getModuleById(id: string): Module | undefined {
  return MODULES.find(m => m.id === id);
}
