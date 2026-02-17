/**
 * PRD-to-Inventory Matching Engine
 *
 * Cross-references Enterprise OS PRD screens against the Brainwave component inventory.
 * For each PRD screen, finds the best matching Brainwave templates based on:
 *   - Layout type match
 *   - Component requirements overlap
 *   - Screen type fit
 *   - Functional similarity
 *
 * Usage: node scripts/match-prd-to-inventory.js
 * Output: public/figma-exports/prd_component_mapping.json
 */

const fs = require('fs');
const path = require('path');

const INVENTORY_PATH = path.join(__dirname, '..', 'public', 'figma-exports', '6hCuwRI0GsBmIOJelAVpND', 'component_inventory.json');
const OUTPUT_PATH = path.join(__dirname, '..', 'public', 'figma-exports', 'prd_component_mapping.json');

// ============================================================
// PRD Screen Definitions — extracted from PRD_Enterprise_OS_V7_MASTER.md
// Each screen has: required layout, needed components, purpose keywords
// ============================================================

const PRD_SCREENS = [
  // MODULE 1: Navigation Centre (The Brain)
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_A",
    name: "Goal Intake Wizard",
    description: "Stream-of-consciousness portal; AI asks refinement questions and auto-generates Alignment-to-Assets plan",
    preferred_layout: ["centered", "split"],
    needed_components: ["form", "input", "textarea", "button", "card", "progress", "tabs"],
    keywords: ["wizard", "form", "intake", "steps", "ai chat", "generation"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_B",
    name: "Role-Informed Perspective Panel",
    description: "Multi-role Think Tank view; system generates perspectives from different roles to flag risks",
    preferred_layout: ["sidebar_content", "split"],
    needed_components: ["sidebar", "card", "avatar", "tabs", "badge", "button"],
    keywords: ["roles", "perspectives", "panel", "multi-view", "avatar"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_C",
    name: "6:00 AM Morning Brief",
    description: "Daily newspaper summarizing yesterday's wins and today's top 3 priorities",
    preferred_layout: ["centered", "sidebar_content"],
    needed_components: ["card", "badge", "button", "divider", "text"],
    keywords: ["digest", "summary", "notification", "brief", "daily", "update"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_D",
    name: "Goal Health Dashboard",
    description: "Visual heatmap of active objectives with Health Scores (1-10)",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "badge", "progress", "chart", "grid", "topbar"],
    keywords: ["dashboard", "health", "heatmap", "scores", "metrics", "status"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_E",
    name: "Decision & Iteration Log",
    description: "Version History for strategy; every pivot logged with rationale",
    preferred_layout: ["sidebar_content", "split"],
    needed_components: ["sidebar", "table", "card", "badge", "button", "divider", "text"],
    keywords: ["log", "history", "timeline", "version", "decisions", "list"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Navigation Centre",
    module_id: 1,
    screen_id: "NAV_F",
    name: "AI Challenge Console",
    description: "Proactive sidebar challenging stale tasks and suggesting actions",
    preferred_layout: ["sidebar_content", "split"],
    needed_components: ["sidebar", "card", "button", "badge", "notification", "text"],
    keywords: ["ai", "chat", "challenge", "sidebar", "proactive", "console"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 2: Command Deck (The Hands)
  {
    module: "Command Deck",
    module_id: 2,
    screen_id: "CMD_A",
    name: "Active Cockpit",
    description: "Running log (left), AI chat (middle), Outputs Pane (right)",
    preferred_layout: ["split", "sidebar_content"],
    needed_components: ["sidebar", "card", "button", "input", "textarea", "text", "divider"],
    keywords: ["cockpit", "chat", "log", "split", "three-panel", "ai", "real-time"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Command Deck",
    module_id: 2,
    screen_id: "CMD_B",
    name: "Role-Appropriate Dashboard",
    description: "Progressive disclosure: freelancer sees 3 panels, CEO sees whole-org velocity",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "topbar", "badge", "chart", "grid", "avatar"],
    keywords: ["dashboard", "role", "metrics", "velocity", "overview", "panels"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Command Deck",
    module_id: 2,
    screen_id: "CMD_C",
    name: "Auto-Digest Generation",
    description: "Split-screen: messy session log transforms into polished manager-ready summary",
    preferred_layout: ["split"],
    needed_components: ["card", "button", "text", "divider", "textarea", "badge"],
    keywords: ["split", "transform", "digest", "summary", "before-after", "generation"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Command Deck",
    module_id: 2,
    screen_id: "CMD_D",
    name: "Agent Registry & Workspace",
    description: "Library of 80+ role profiles to activate per session",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "grid", "avatar", "badge", "search_bar", "button"],
    keywords: ["registry", "library", "grid", "cards", "agents", "profiles", "search"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Command Deck",
    module_id: 2,
    screen_id: "CMD_E",
    name: "Approval & Governance Queue",
    description: "Swipe to Approve interface for promoting Staging to Canonical",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "button", "badge", "table", "toggle", "divider"],
    keywords: ["queue", "approval", "review", "promote", "governance", "swipe"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 3: Core Engine (The Nervous System)
  {
    module: "Core Engine",
    module_id: 3,
    screen_id: "ENG_A",
    name: "Routing Rules Editor",
    description: "Logic-builder for keyword thresholds per pillar",
    preferred_layout: ["sidebar_content", "split"],
    needed_components: ["sidebar", "input", "button", "card", "toggle", "dropdown", "table"],
    keywords: ["editor", "rules", "logic", "builder", "settings", "configuration"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Core Engine",
    module_id: 3,
    screen_id: "ENG_B",
    name: "Universal Index & Manifests",
    description: "Filterable list of every file, thread, artifact with Epoch Counts",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "table", "search_bar", "badge", "button", "dropdown", "pagination"],
    keywords: ["index", "list", "table", "filter", "search", "manifests", "files"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Core Engine",
    module_id: 3,
    screen_id: "ENG_C",
    name: "RAG Quality Dashboard",
    description: "Chunking efficiency, token counts, embedding accuracy",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "chart", "badge", "progress", "table", "topbar"],
    keywords: ["dashboard", "quality", "metrics", "charts", "monitoring", "rag"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Core Engine",
    module_id: 3,
    screen_id: "ENG_D",
    name: "Schema & Data Model Library",
    description: "PostgreSQL/JSON schemas; new projects pull their skeleton from here",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "table", "button", "text", "badge"],
    keywords: ["schema", "library", "data model", "database", "code", "reference"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Core Engine",
    module_id: 3,
    screen_id: "ENG_E",
    name: "Error Library & Failure Log",
    description: "Diagnostic heart monitor for script and API failures",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "table", "badge", "card", "button", "notification"],
    keywords: ["errors", "log", "failures", "diagnostic", "monitoring", "alerts"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 4: Knowledge Library (The Stomach)
  {
    module: "Knowledge Library",
    module_id: 4,
    screen_id: "LIB_A",
    name: "Ingestion Inbox",
    description: "Global inbox: Pending, Processing, Routed, Unrouted + URL Sniffer",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "table", "badge", "button", "tabs", "search_bar", "card"],
    keywords: ["inbox", "queue", "pending", "processing", "status", "ingestion"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Knowledge Library",
    module_id: 4,
    screen_id: "LIB_B",
    name: "Artifact Extraction View",
    description: "Split-screen: raw source vs. 29 extracted artifact types",
    preferred_layout: ["split"],
    needed_components: ["card", "text", "badge", "tabs", "button", "divider"],
    keywords: ["split", "extraction", "artifacts", "comparison", "source", "types"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Knowledge Library",
    module_id: 4,
    screen_id: "LIB_C",
    name: "Promotion Console",
    description: "Quality Gate: review Staging, one-click promote to Canonical",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "button", "badge", "toggle", "table", "text"],
    keywords: ["promotion", "review", "quality", "gate", "approve", "staging"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Knowledge Library",
    module_id: 4,
    screen_id: "LIB_D",
    name: "Semantic Search Engine",
    description: "Lattice Filters by Project, Domain, Date",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["search_bar", "card", "badge", "dropdown", "button", "tabs", "grid"],
    keywords: ["search", "filters", "results", "semantic", "query", "lattice"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Knowledge Library",
    module_id: 4,
    screen_id: "LIB_E",
    name: "Pipeline Health Monitor",
    description: "Real-time status bars for active scrapers and fetchers",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "progress", "badge", "chart", "table"],
    keywords: ["pipeline", "health", "monitoring", "status", "real-time", "scrapers"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 5: Template Hub (The DNA)
  {
    module: "Template Hub",
    module_id: 5,
    screen_id: "TPL_A",
    name: "Template Catalogue",
    description: "Searchable grid: Agents, Prompts, SOPs, Project Scaffolds",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "grid", "search_bar", "badge", "button", "tabs"],
    keywords: ["catalogue", "grid", "cards", "search", "templates", "library"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Template Hub",
    module_id: 5,
    screen_id: "TPL_B",
    name: "Dynamic Document Generator",
    description: "Wizard: select blueprint, fill parameters, AI assembles high-fidelity doc",
    preferred_layout: ["centered", "split"],
    needed_components: ["form", "input", "button", "card", "progress", "dropdown", "textarea"],
    keywords: ["wizard", "generator", "form", "parameters", "document", "builder"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Template Hub",
    module_id: 5,
    screen_id: "TPL_C",
    name: "Scaffold Replicator",
    description: "One-click deployment of 17-stage project hierarchy",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "button", "progress", "badge", "tree", "text"],
    keywords: ["scaffold", "deploy", "hierarchy", "tree", "replication", "stages"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Template Hub",
    module_id: 5,
    screen_id: "TPL_D",
    name: "Prompt Chain Editor",
    description: "Visual flow builder chaining AI models into production sequences",
    preferred_layout: ["full_canvas", "sidebar_content"],
    needed_components: ["sidebar", "card", "button", "input", "dropdown"],
    keywords: ["flow", "editor", "canvas", "chain", "visual", "builder", "nodes"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Template Hub",
    module_id: 5,
    screen_id: "TPL_E",
    name: "Brand DNA Vault",
    description: "Irreducible backbone: vision, voice rules, unique mechanisms",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "text", "badge", "button", "divider", "image"],
    keywords: ["brand", "vault", "reference", "rules", "guidelines", "vision"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 6: Domain Pillars (The Organs)
  {
    module: "Domain Pillars",
    module_id: 6,
    screen_id: "PIL_A",
    name: "Pillar Grid",
    description: "Bird's-eye view: item counts, health status, last update",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "grid", "badge", "progress", "button", "topbar"],
    keywords: ["grid", "overview", "cards", "health", "status", "pillars"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Domain Pillars",
    module_id: 6,
    screen_id: "PIL_B",
    name: "Canon Viewer",
    description: "Authoritative reference document; AI agents primary instruction set",
    preferred_layout: ["sidebar_content", "split"],
    needed_components: ["sidebar", "text", "card", "button", "breadcrumb", "divider"],
    keywords: ["viewer", "document", "reference", "canon", "reading", "content"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Domain Pillars",
    module_id: 6,
    screen_id: "PIL_C",
    name: "Artifact Browser",
    description: "Filterable archive of high-value extracted assets",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "grid", "search_bar", "badge", "dropdown", "button"],
    keywords: ["browser", "archive", "filter", "grid", "assets", "search"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Domain Pillars",
    module_id: 6,
    screen_id: "PIL_D",
    name: "Thread Archive",
    description: "Raw AI conversation histories (full provenance)",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "text", "badge", "search_bar", "button", "pagination"],
    keywords: ["archive", "threads", "conversations", "history", "provenance", "list"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Domain Pillars",
    module_id: 6,
    screen_id: "PIL_E",
    name: "Pillar Routing Rules Editor",
    description: "Logic-builder: keywords and thresholds per organ",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "input", "button", "table", "toggle", "dropdown", "card"],
    keywords: ["editor", "rules", "routing", "keywords", "settings", "logic"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 7: Build Factory (The Kinetic Limbs)
  {
    module: "Build Factory",
    module_id: 7,
    screen_id: "BLD_A",
    name: "Project Registry",
    description: "Active builds with Maturity Grades (Speculative/Operational/Production-Ready)",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "table", "badge", "button", "dropdown"],
    keywords: ["registry", "projects", "list", "status", "grades", "builds"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Build Factory",
    module_id: 7,
    screen_id: "BLD_B",
    name: "17-Step Mission Control",
    description: "Linear production line tracking all build stages",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "progress", "card", "badge", "button", "timeline"],
    keywords: ["mission control", "pipeline", "stages", "linear", "tracking", "production"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Build Factory",
    module_id: 7,
    screen_id: "BLD_C",
    name: "Assembly Dashboard",
    description: "Drag-and-drop: snap Copy Frameworks and UI Snippets into scaffold",
    preferred_layout: ["sidebar_content", "full_canvas"],
    needed_components: ["sidebar", "card", "button", "grid", "drag_drop"],
    keywords: ["assembly", "drag-drop", "canvas", "dashboard", "builder", "snap"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Build Factory",
    module_id: 7,
    screen_id: "BLD_D",
    name: "Role-Informed PRD Editor",
    description: "Multi-role AI reviewers flag risks before coding begins",
    preferred_layout: ["split", "sidebar_content"],
    needed_components: ["sidebar", "textarea", "card", "avatar", "badge", "button", "text"],
    keywords: ["editor", "prd", "review", "roles", "document", "ai"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Build Factory",
    module_id: 7,
    screen_id: "BLD_E",
    name: "Build Story",
    description: "Chronological timeline capturing breakthroughs and anti-patterns",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "text", "badge", "button", "divider", "timeline"],
    keywords: ["story", "timeline", "chronological", "history", "breakthroughs"],
    screen_type_preference: ["full_page"]
  },

  // MODULE 8: Operations (The Immune System)
  {
    module: "Operations",
    module_id: 8,
    screen_id: "OPS_A",
    name: "System Health Dashboard",
    description: "Org heatmap: ingestion stats, routing accuracy, pillar freshness",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "chart", "badge", "progress", "grid", "topbar"],
    keywords: ["dashboard", "health", "heatmap", "stats", "monitoring", "system"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Operations",
    module_id: 8,
    screen_id: "OPS_B",
    name: "Strategic Goal Cascade",
    description: "Visual tree: individual tasks auto-update CEO-level goal percentages",
    preferred_layout: ["sidebar_content", "centered"],
    needed_components: ["card", "progress", "badge", "tree", "button", "text"],
    keywords: ["cascade", "goals", "tree", "hierarchy", "strategic", "visual"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Operations",
    module_id: 8,
    screen_id: "OPS_C",
    name: "Canonisation Queue",
    description: "Quality Gate for promoting Staging to Canonical",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "button", "badge", "table", "toggle"],
    keywords: ["queue", "approval", "promotion", "staging", "canonical", "review"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Operations",
    module_id: 8,
    screen_id: "OPS_D",
    name: "Daily Digest Viewer",
    description: "AI-synthesized morning briefing by role level",
    preferred_layout: ["centered", "sidebar_content"],
    needed_components: ["card", "text", "badge", "button", "divider", "avatar"],
    keywords: ["digest", "daily", "briefing", "summary", "viewer", "morning"],
    screen_type_preference: ["full_page"]
  },
  {
    module: "Operations",
    module_id: 8,
    screen_id: "OPS_E",
    name: "Whole-Org Pulse",
    description: "Live activity feed: who's working on what, where the bottlenecks are",
    preferred_layout: ["sidebar_content"],
    needed_components: ["sidebar", "card", "avatar", "badge", "button", "text", "notification"],
    keywords: ["pulse", "live", "feed", "activity", "real-time", "org"],
    screen_type_preference: ["full_page"]
  }
];

// ============================================================
// Matching Engine
// ============================================================

function scoreMatch(prdScreen, inventoryScreen) {
  let score = 0;
  let reasons = [];

  // 1. Layout match (0-25 points)
  if (inventoryScreen.layout?.type) {
    if (prdScreen.preferred_layout.includes(inventoryScreen.layout.type)) {
      score += 25;
      reasons.push(`layout:${inventoryScreen.layout.type}`);
    } else {
      score += 5; // partial credit for any layout
    }
  }

  // 2. Screen type match (0-15 points)
  if (prdScreen.screen_type_preference.includes(inventoryScreen.screen_type)) {
    score += 15;
    reasons.push(`type:${inventoryScreen.screen_type}`);
  } else if (inventoryScreen.screen_type === 'state_variant') {
    score -= 10; // penalise variants
  }

  // 3. Component overlap (0-40 points)
  const inventoryCompTypes = new Set(
    (inventoryScreen.components || []).map(c => c.type)
  );
  const needed = prdScreen.needed_components;
  let matched = 0;
  let matchedComps = [];
  for (const comp of needed) {
    if (inventoryCompTypes.has(comp)) {
      matched++;
      matchedComps.push(comp);
    }
  }
  const compScore = needed.length > 0 ? (matched / needed.length) * 40 : 0;
  score += compScore;
  if (matchedComps.length > 0) {
    reasons.push(`components:${matchedComps.join(',')}`);
  }

  // 4. Has sidebar when needed (0-10 points)
  const needsSidebar = prdScreen.needed_components.includes('sidebar');
  if (needsSidebar && inventoryScreen.layout?.has_sidebar) {
    score += 10;
    reasons.push('has_sidebar');
  }

  // 5. Component count richness bonus (0-10 points)
  const compCount = (inventoryScreen.components || []).length;
  if (compCount >= 20) {
    score += 10;
    reasons.push(`rich:${compCount}comps`);
  } else if (compCount >= 10) {
    score += 5;
  }

  return { score: Math.round(score), reasons, matched_components: matchedComps };
}

function findMatches(prdScreen, inventory, topN = 5) {
  const scored = inventory.screens
    .map(invScreen => ({
      screen_slug: invScreen.screen_slug,
      screen_name: invScreen.screen_name,
      screen_type: invScreen.screen_type,
      layout_type: invScreen.layout?.type,
      component_count: (invScreen.components || []).length,
      ...scoreMatch(prdScreen, invScreen)
    }))
    .filter(m => m.score > 20) // minimum threshold
    .sort((a, b) => b.score - a.score)
    .slice(0, topN);

  return scored;
}

// ============================================================
// Main
// ============================================================

function main() {
  console.log('\n=== PRD → INVENTORY MATCHING ENGINE ===\n');

  // Load inventory
  if (!fs.existsSync(INVENTORY_PATH)) {
    console.error('ERROR: component_inventory.json not found');
    process.exit(1);
  }
  const inventory = JSON.parse(fs.readFileSync(INVENTORY_PATH, 'utf8'));
  console.log(`Inventory: ${inventory.total_screens} Brainwave screens loaded`);
  console.log(`PRD: ${PRD_SCREENS.length} screens to match\n`);

  const results = {
    generated_at: new Date().toISOString(),
    inventory_kit: 'Brainwave 2.0',
    inventory_screens: inventory.total_screens,
    prd_screens: PRD_SCREENS.length,
    modules: {},
    coverage_summary: {},
    unmapped_screens: [],
    best_reuse_screens: {}
  };

  let totalMatched = 0;
  let totalUnmatched = 0;

  // Group by module
  const modules = {};
  for (const screen of PRD_SCREENS) {
    if (!modules[screen.module]) modules[screen.module] = [];
    modules[screen.module].push(screen);
  }

  for (const [moduleName, screens] of Object.entries(modules)) {
    console.log(`\n── Module ${screens[0].module_id}: ${moduleName} ──`);
    results.modules[moduleName] = { screens: [] };

    for (const prdScreen of screens) {
      const matches = findMatches(prdScreen, inventory);

      const screenResult = {
        screen_id: prdScreen.screen_id,
        name: prdScreen.name,
        description: prdScreen.description,
        preferred_layout: prdScreen.preferred_layout,
        needed_components: prdScreen.needed_components,
        match_count: matches.length,
        best_match_score: matches[0]?.score || 0,
        matches: matches
      };

      results.modules[moduleName].screens.push(screenResult);

      if (matches.length > 0) {
        totalMatched++;
        const best = matches[0];
        console.log(`  ✓ ${prdScreen.screen_id}: ${prdScreen.name}`);
        console.log(`    Best: ${best.screen_name} (${best.score}%) — ${best.reasons.join(', ')}`);
        if (matches.length > 1) {
          console.log(`    Also: ${matches.slice(1, 3).map(m => `${m.screen_name} (${m.score}%)`).join(', ')}`);
        }
      } else {
        totalUnmatched++;
        results.unmapped_screens.push({
          screen_id: prdScreen.screen_id,
          name: prdScreen.name,
          needed: prdScreen.needed_components
        });
        console.log(`  ✗ ${prdScreen.screen_id}: ${prdScreen.name} — NO MATCH (needs: ${prdScreen.needed_components.join(', ')})`);
      }
    }
  }

  // Track which inventory screens are most reused
  const reuseCount = {};
  for (const [, modData] of Object.entries(results.modules)) {
    for (const screen of modData.screens) {
      for (const match of screen.matches) {
        reuseCount[match.screen_slug] = (reuseCount[match.screen_slug] || 0) + 1;
      }
    }
  }
  results.best_reuse_screens = Object.entries(reuseCount)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 15)
    .map(([slug, count]) => ({ slug, matched_to_prd_screens: count }));

  // Coverage summary
  results.coverage_summary = {
    total_prd_screens: PRD_SCREENS.length,
    screens_with_matches: totalMatched,
    screens_without_matches: totalUnmatched,
    coverage_percentage: Math.round((totalMatched / PRD_SCREENS.length) * 100),
    note: "Brainwave alone covers these screens. Additional kits (Square Dashboard, Untitled UI, etc.) will fill gaps."
  };

  // Write output
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2));

  console.log('\n========================================');
  console.log('  MATCHING COMPLETE');
  console.log('========================================');
  console.log(`PRD screens: ${PRD_SCREENS.length}`);
  console.log(`Matched: ${totalMatched} (${results.coverage_summary.coverage_percentage}%)`);
  console.log(`Unmatched: ${totalUnmatched}`);
  console.log(`\nMost reusable Brainwave screens:`);
  results.best_reuse_screens.slice(0, 8).forEach(s =>
    console.log(`  ${s.slug}: matches ${s.matched_to_prd_screens} PRD screens`)
  );
  console.log(`\nOutput: ${OUTPUT_PATH}`);
}

main();
