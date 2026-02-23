#!/usr/bin/env python3
"""
Enterprise OS V7 — Content Extraction Engine

Runs structured extraction passes on any content using LLM APIs.
Four extraction modes:
  domains  — 27-domain classification pass (any content)
  thread   — EKX-1 20-section extraction (AI chat threads)
  copy     — Copy/sales extraction (benefits, USPs, hooks, etc.)
  book     — Book extraction (proofs, arguments, rhetorical devices, etc.)

Usage:
    python v7_extract.py domains <file>                    # Single file, 27-domain pass
    python v7_extract.py thread <file>                     # Single file, EKX-1 extraction
    python v7_extract.py copy <file>                       # Single file, copy/sales extraction
    python v7_extract.py book <file>                       # Single file, book extraction
    python v7_extract.py batch <folder> --mode domains     # Batch mode
    python v7_extract.py batch <folder> --mode copy        # Batch on folder
    python v7_extract.py batch <folder> --mode thread --ext .md   # Batch, filter by extension

Options:
    --api deepseek|claude       API to use (default: deepseek)
    --output <folder>           Override output location (default: alongside source file)
    --dry-run                   Show what would be processed without calling API
    --resume                    Resume from checkpoint (skip already-processed files)

Output:
    For each input file, creates:
      <filename>.extract_<mode>.json    — Structured extraction data
      <filename>.extract_<mode>.md      — Human-readable extraction summary

Database: enterprise_os (PostgreSQL, localhost) — logs extractions to v7_changes
"""

import os
import sys
import json
import time
import hashlib
import argparse
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' not installed. Run: pip install requests")
    sys.exit(1)


# ============================================================
# Configuration
# ============================================================

V7_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-37c6535a8de54acdac169dc6b0045ac9")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"

CLAUDE_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"

# Max chars to send in one API call. If content exceeds this, split into chunks.
MAX_CONTENT_CHARS = 28000  # ~7000 tokens, safe for both APIs

CHECKPOINT_DIR = V7_ROOT / "03_CORE_ENGINE" / "CONFIG" / "extraction_checkpoints"
LOG_DIR = V7_ROOT / "03_CORE_ENGINE" / "ROUTING_ENGINE" / "extraction_logs"
CENTRAL_STORE = V7_ROOT / "04_KNOWLEDGE_LIBRARY" / "EXTRACTIONS"
EXTRACTION_INDEX = CENTRAL_STORE / "EXTRACTION_INDEX.json"

VALID_EXTENSIONS = {".md", ".txt", ".json", ".py", ".sql", ".yaml", ".yml", ".html", ".csv"}


# ============================================================
# Extraction Prompts
# ============================================================

PROMPT_27_DOMAINS = """You are a knowledge extraction specialist. Analyse the following content and classify it across the 27 extraction domains listed below. For each domain that has relevant content, extract the key items.

THE 27 EXTRACTION DOMAINS:
1. Product & Platform Definition — Features, capabilities, modules, boundaries
2. Benefits & Outcomes — User benefits, business benefits, operational leverage
3. Hooks, Messaging & Positioning — Marketing angles, narrative power, attention hooks
4. Unique Mechanisms & Differentiation — Why-this-works, moats, proprietary methods
5. Processes, SOPs & Workflows — Repeatability, sequencing, guardrails
6. Performance, Learning & Feedback — What worked, what failed, enforcement results
7. Navigation, Goals & Decision Systems — Intent, goals, priorities, routing
8. Project & Delivery Management — PRDs, phases, milestones, ownership
9. Roles, Responsibilities & Virtual Workforce — Human + agent roles, handoffs
10. Automation Opportunities — Manual processes that could be automated
11. Enforcement & Quality Control — Naming, routing, validation, anti-entropy
12. Knowledge Architecture & RAG — Chunking, indexing, retrieval, knowledge structure
13. Templates & Reusable Scaffolds — Context docs, SOPs, prompts, agents
14. Data Models & Databases — Schemas, entities, relationships
15. Libraries (UI / Copy / Media / Assets) — Component libraries, copy blocks, media
16. UI / UX & Interface Implications — Dashboards, forms, controls, user flows
17. Engineering & Infrastructure — APIs, pipelines, repos, auth, hosting
18. Operations & Post-Launch — Monitoring, iteration, scaling, support
19. Commercialisation & Monetisation — Packaging, pricing, licensing, revenue
20. Governance & Evolution — Canon vs observed, migration, system drift
21. Meta-Systems — Extraction quality, blind-spot detection, self-improvement
22. Scripts, Code & Pipelines — Specific code, commands, automation scripts
23. Books, Writing & Long-Form IP — Book content, chapters, intellectual property
24. Courses, Webinars & Educational Products — Teaching content, curriculum
25. Training & Onboarding Systems — How people/agents learn the system
26. External Intelligence Ingestion — Content from outside sources
27. Intelligence Routing & Dissemination — How knowledge gets distributed

INSTRUCTIONS:
- Only include domains where the content has REAL, SUBSTANTIVE items to extract
- Skip domains with nothing relevant (don't force it)
- For each included domain, list the specific extracted items as bullet points
- Be precise and specific — extract actual content, not vague summaries
- Preserve important details, names, numbers, and specifics

Respond with valid JSON in this exact format:
{
  "source_file": "<filename>",
  "extraction_date": "<ISO date>",
  "extraction_mode": "27_domains",
  "domains_found": <number of domains with content>,
  "domains": {
    "<domain_number>": {
      "name": "<domain name>",
      "relevance": "high|medium|low",
      "items": ["<extracted item 1>", "<extracted item 2>", ...]
    }
  },
  "primary_domains": [<top 3 domain numbers by relevance>],
  "summary": "<2-3 sentence summary of what this content is about>"
}

CONTENT TO ANALYSE:
"""

PROMPT_EKX1_THREAD = """You are an AI thread extraction specialist using the EKX-1 methodology. Extract a structured 20-section summary from this AI chat thread.

THE 20 EKX-1 SECTIONS:
1. Narrative & Context — What was this thread about? Brief story of what happened.
2. Objectives (Explicit) — What were we trying to achieve?
3. Success Criteria — How would we know it worked?
4. Decisions & Rules — What was decided? Any rules established?
5. SOPs / Workflows — What processes or standard procedures were defined?
6. Scripts / Commands — What code, commands, or scripts were produced?
7. Inputs & Outputs — What went in? What came out?
8. Missteps / Errors / Risks — What went wrong? What risks were identified?
9. Blockers — What stopped or slowed progress?
10. Status — Where did the work end up? Complete? In progress? Blocked?
11. Progress Markers — What milestones or checkpoints were hit?
12. Refinements — What was iterated on or improved during the thread?
13. Dependencies — What does this work depend on? What depends on it?
14. Entity Maps — Key concepts, systems, names, and their relationships
15. Glossary — Terms defined or used with specific meaning
16. Future — What's planned next?
17. Pending — What's started but unfinished?
18. Open Questions — What's still unresolved?
19. Meta-Observations — Patterns, insights about the process itself
20. Reusable Assets — Frameworks, templates, prompts, code worth keeping

INSTRUCTIONS:
- Extract REAL content for each section — not vague summaries
- If a section has nothing relevant, include it with an empty items array
- Preserve specifics: file paths, counts, names, decisions, exact commands
- Do NOT truncate or summarise away important details
- If the thread covers multiple topics, capture ALL of them

Respond with valid JSON in this exact format:
{
  "source_file": "<filename>",
  "extraction_date": "<ISO date>",
  "extraction_mode": "ekx1_thread",
  "thread_title": "<descriptive title for this thread>",
  "sections": {
    "1_narrative": {"title": "Narrative & Context", "items": ["..."]},
    "2_objectives": {"title": "Objectives", "items": ["..."]},
    "3_success_criteria": {"title": "Success Criteria", "items": ["..."]},
    "4_decisions": {"title": "Decisions & Rules", "items": ["..."]},
    "5_sops": {"title": "SOPs / Workflows", "items": ["..."]},
    "6_scripts": {"title": "Scripts / Commands", "items": ["..."]},
    "7_inputs_outputs": {"title": "Inputs & Outputs", "items": ["..."]},
    "8_missteps": {"title": "Missteps / Errors / Risks", "items": ["..."]},
    "9_blockers": {"title": "Blockers", "items": ["..."]},
    "10_status": {"title": "Status", "items": ["..."]},
    "11_progress": {"title": "Progress Markers", "items": ["..."]},
    "12_refinements": {"title": "Refinements", "items": ["..."]},
    "13_dependencies": {"title": "Dependencies", "items": ["..."]},
    "14_entities": {"title": "Entity Maps", "items": ["..."]},
    "15_glossary": {"title": "Glossary", "items": ["..."]},
    "16_future": {"title": "Future", "items": ["..."]},
    "17_pending": {"title": "Pending", "items": ["..."]},
    "18_questions": {"title": "Open Questions", "items": ["..."]},
    "19_meta": {"title": "Meta-Observations", "items": ["..."]},
    "20_assets": {"title": "Reusable Assets", "items": ["..."]}
  },
  "summary": "<2-3 sentence summary>"
}

THREAD CONTENT TO EXTRACT:
"""

PROMPT_COPY_SALES = """You are a direct response copywriting and sales intelligence extraction specialist. Extract all commercial intelligence from this content that could be used for marketing, sales copy, landing pages, ads, emails, or any customer-facing communication.

EXTRACT THESE CATEGORIES:

BENEFITS — What the user/customer gains. Split into:
  - User benefits (personal outcomes)
  - Business benefits (revenue, efficiency, growth)
  - Operational benefits (saves time, reduces errors, simplifies)

FEATURES — Specific capabilities, functions, modules, tools described.

PROBLEMS — Pain points, frustrations, challenges the target audience faces.

PROBLEMS SOLVED — How this product/service/system specifically addresses each problem.

USPs — What makes this unique compared to alternatives or competitors.

UNIQUE MECHANISMS — Proprietary systems, methods, frameworks, or named processes that explain HOW it works. These are the "why this works" elements.

HOOKS — Attention-grabbing angles that could open a headline, ad, email, or content piece. Think: curiosity, fear, desire, urgency, novelty.

SALES ARGUMENTS — Logical and emotional reasons someone should buy, use, or engage with this.

OBJECTIONS — What the target audience might push back on. Reasons they'd say no.

PROOF POINTS — Evidence that this works: data, case studies, demonstrations, testimonials, before/after, results.

CTAs — Calls to action implied or stated. What should the reader do next?

INSTRUCTIONS:
- Be SPECIFIC — extract actual benefits, not "it has many benefits"
- Include the exact language and phrasing from the content where powerful
- If something could be a headline or hook, flag it
- Capture unique terminology and named frameworks — these are marketing gold
- Don't invent — only extract what's actually in the content

Respond with valid JSON in this exact format:
{
  "source_file": "<filename>",
  "extraction_date": "<ISO date>",
  "extraction_mode": "copy_sales",
  "project_or_product": "<what product/project/IP this relates to, if identifiable>",
  "categories": {
    "benefits_user": ["..."],
    "benefits_business": ["..."],
    "benefits_operational": ["..."],
    "features": ["..."],
    "problems": ["..."],
    "problems_solved": ["..."],
    "usps": ["..."],
    "unique_mechanisms": ["..."],
    "hooks": ["..."],
    "sales_arguments": ["..."],
    "objections": ["..."],
    "proof_points": ["..."],
    "ctas": ["..."]
  },
  "top_hooks": ["<best 3-5 hooks/angles from the content>"],
  "summary": "<2-3 sentence summary of the commercial intelligence found>"
}

CONTENT TO EXTRACT FROM:
"""

PROMPT_BOOK = """You are a book content and intellectual property extraction specialist. Extract all material from this content that could be used in a book, long-form writing, speeches, courses, or thought leadership content.

EXTRACT THESE CATEGORIES:

PROOFS — Evidence, data, case studies, demonstrations, results that PROVE a point.

ARGUMENTS — Core logical arguments and reasoning chains. The "because X, therefore Y" structures.

FACTS — Verifiable facts, statistics, research findings, numbers.

HOOKS — Opening angles for chapters, sections, speeches, or content. Things that grab attention and make someone want to keep reading.

RHETORICAL DEVICES — Metaphors, analogies, stories, thought experiments, frameworks, or vivid comparisons that make ideas stick and become memorable.

OBJECTIONS & MYTHS — Common beliefs, assumptions, or myths that the audience holds which are WRONG or incomplete. Things you can challenge and disprove.

BELIEFS TO CHALLENGE — Deeper assumptions the reader has that need reframing. The "you think X, but actually Y" moments.

SOLUTIONS — What you offer in place of the wrong beliefs. The better way, the new framework, the replacement worldview.

KEY CONCEPTS — Core ideas, named frameworks, terminology, or mental models that form the intellectual backbone.

QUOTABLE LINES — Sentences or phrases that are punchy enough to be pulled out as quotes, tweets, or highlights.

INSTRUCTIONS:
- Extract ACTUAL content, not summaries of content
- Preserve the original language where it's powerful
- If something is a strong rhetorical device or metaphor, flag it specifically
- Capture the LOGIC of arguments, not just the conclusions
- Named frameworks and systems are high-value — always capture these
- Look for contrarian or counterintuitive insights — these are book gold

Respond with valid JSON in this exact format:
{
  "source_file": "<filename>",
  "extraction_date": "<ISO date>",
  "extraction_mode": "book",
  "subject_area": "<what topic/domain this content relates to>",
  "categories": {
    "proofs": ["..."],
    "arguments": ["..."],
    "facts": ["..."],
    "hooks": ["..."],
    "rhetorical_devices": ["..."],
    "objections_and_myths": ["..."],
    "beliefs_to_challenge": ["..."],
    "solutions": ["..."],
    "key_concepts": ["..."],
    "quotable_lines": ["..."]
  },
  "strongest_material": ["<best 3-5 items across all categories>"],
  "summary": "<2-3 sentence summary of the intellectual content found>"
}

CONTENT TO EXTRACT FROM:
"""


# ============================================================
# API Callers
# ============================================================

def call_deepseek(system_prompt: str, user_content: str) -> dict:
    """Call DeepSeek API and return parsed JSON response."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    }
    payload = {
        "model": DEEPSEEK_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.2,
        "max_tokens": 8192,
        "stream": False,
    }

    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=300)

    if response.status_code != 200:
        raise RuntimeError(f"DeepSeek API error {response.status_code}: {response.text[:500]}")

    result = response.json()
    usage = result.get("usage", {})
    content = result["choices"][0]["message"]["content"]

    return {
        "content": content,
        "prompt_tokens": usage.get("prompt_tokens", 0),
        "completion_tokens": usage.get("completion_tokens", 0),
    }


def call_claude(system_prompt: str, user_content: str) -> dict:
    """Call Claude API and return parsed JSON response."""
    if not CLAUDE_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY not set. Set it as an environment variable.")

    headers = {
        "Content-Type": "application/json",
        "x-api-key": CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01",
    }
    payload = {
        "model": CLAUDE_MODEL,
        "max_tokens": 8192,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": user_content},
        ],
        "temperature": 0.2,
    }

    response = requests.post(CLAUDE_API_URL, headers=headers, json=payload, timeout=300)

    if response.status_code != 200:
        raise RuntimeError(f"Claude API error {response.status_code}: {response.text[:500]}")

    result = response.json()
    usage = result.get("usage", {})
    content = result["content"][0]["text"]

    return {
        "content": content,
        "prompt_tokens": usage.get("input_tokens", 0),
        "completion_tokens": usage.get("output_tokens", 0),
    }


def call_api(api: str, system_prompt: str, user_content: str) -> dict:
    """Route to the correct API."""
    if api == "deepseek":
        return call_deepseek(system_prompt, user_content)
    elif api == "claude":
        return call_claude(system_prompt, user_content)
    else:
        raise ValueError(f"Unknown API: {api}. Use 'deepseek' or 'claude'.")


# ============================================================
# Content handling
# ============================================================

def read_file_full(file_path: Path) -> str:
    """Read entire file content. Never truncate."""
    try:
        return file_path.read_text(encoding="utf-8", errors="replace")
    except (PermissionError, OSError) as e:
        raise RuntimeError(f"Cannot read {file_path}: {e}")


def chunk_content(content: str, max_chars: int = MAX_CONTENT_CHARS) -> list:
    """Split content into chunks by headings, respecting max size.
    Never truncates — every character is in a chunk."""
    if len(content) <= max_chars:
        return [content]

    lines = content.split("\n")
    chunks = []
    current = []
    current_len = 0

    for line in lines:
        if line.startswith("#") and current_len > 0 and current_len + len(line) > max_chars:
            chunks.append("\n".join(current))
            current = [line]
            current_len = len(line)
        elif current_len + len(line) + 1 > max_chars and current:
            chunks.append("\n".join(current))
            current = [line]
            current_len = len(line)
        else:
            current.append(line)
            current_len += len(line) + 1

    if current:
        chunks.append("\n".join(current))

    return chunks


def parse_json_response(raw: str) -> dict:
    """Parse JSON from API response, handling markdown code blocks."""
    text = raw.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"JSON parse error: {e}\nRaw response (first 500 chars): {text[:500]}")


def merge_domain_extractions(results: list) -> dict:
    """Merge multiple chunk extractions into one for 27-domain pass."""
    if len(results) == 1:
        return results[0]

    merged = results[0].copy()
    merged_domains = {}

    for result in results:
        for domain_num, domain_data in result.get("domains", {}).items():
            if domain_num in merged_domains:
                existing = merged_domains[domain_num]["items"]
                new_items = [i for i in domain_data.get("items", []) if i not in existing]
                merged_domains[domain_num]["items"].extend(new_items)
            else:
                merged_domains[domain_num] = domain_data.copy()

    merged["domains"] = merged_domains
    merged["domains_found"] = len(merged_domains)
    primary = sorted(merged_domains.keys(), key=lambda k: len(merged_domains[k].get("items", [])), reverse=True)
    merged["primary_domains"] = [int(p) for p in primary[:3]]
    return merged


def merge_generic_extractions(results: list, mode: str) -> dict:
    """Merge multiple chunk extractions for copy/book modes."""
    if len(results) == 1:
        return results[0]

    merged = results[0].copy()
    categories_key = "categories" if "categories" in merged else "sections"

    for result in results[1:]:
        for cat_key, items in result.get(categories_key, {}).items():
            if cat_key in merged.get(categories_key, {}):
                if isinstance(items, list):
                    existing = merged[categories_key][cat_key]
                    new_items = [i for i in items if i not in existing]
                    merged[categories_key][cat_key].extend(new_items)
                elif isinstance(items, dict) and "items" in items:
                    existing = merged[categories_key][cat_key].get("items", [])
                    new_items = [i for i in items.get("items", []) if i not in existing]
                    merged[categories_key][cat_key]["items"].extend(new_items)
            else:
                merged[categories_key][cat_key] = items

    return merged


# ============================================================
# Output writers
# ============================================================

def write_json_output(data: dict, output_path: Path):
    """Write extraction JSON to file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def write_markdown_output(data: dict, mode: str, output_path: Path):
    """Write human-readable markdown summary of extraction."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(f"# Extraction: {mode.upper()}")
    lines.append(f"")
    lines.append(f"**Source:** {data.get('source_file', 'unknown')}")
    lines.append(f"**Date:** {data.get('extraction_date', 'unknown')}")
    lines.append(f"**Mode:** {mode}")
    if data.get("summary"):
        lines.append(f"")
        lines.append(f"**Summary:** {data['summary']}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    if mode == "27_domains":
        for num, domain in sorted(data.get("domains", {}).items(), key=lambda x: x[0]):
            name = domain.get("name", f"Domain {num}")
            relevance = domain.get("relevance", "")
            items = domain.get("items", [])
            if items:
                lines.append(f"## {num}. {name} [{relevance}]")
                lines.append(f"")
                for item in items:
                    lines.append(f"- {item}")
                lines.append(f"")

    elif mode == "ekx1_thread":
        if data.get("thread_title"):
            lines.append(f"## Thread: {data['thread_title']}")
            lines.append(f"")
        for key, section in data.get("sections", {}).items():
            title = section.get("title", key)
            items = section.get("items", [])
            if items:
                lines.append(f"## {title}")
                lines.append(f"")
                for item in items:
                    lines.append(f"- {item}")
                lines.append(f"")

    elif mode in ("copy_sales", "book"):
        for cat_key, items in data.get("categories", {}).items():
            if items:
                cat_name = cat_key.replace("_", " ").title()
                lines.append(f"## {cat_name}")
                lines.append(f"")
                for item in items:
                    lines.append(f"- {item}")
                lines.append(f"")

        top_key = "top_hooks" if mode == "copy_sales" else "strongest_material"
        if data.get(top_key):
            lines.append(f"## {'Top Hooks' if mode == 'copy_sales' else 'Strongest Material'}")
            lines.append(f"")
            for item in data[top_key]:
                lines.append(f"- **{item}**")
            lines.append(f"")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ============================================================
# Checkpoint system
# ============================================================

def get_checkpoint_path(batch_id: str) -> Path:
    """Get the checkpoint file path for a batch run."""
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    return CHECKPOINT_DIR / f"checkpoint_{batch_id}.json"


def load_checkpoint(batch_id: str) -> dict:
    """Load checkpoint data for a batch run."""
    cp_path = get_checkpoint_path(batch_id)
    if cp_path.exists():
        with open(cp_path) as f:
            return json.load(f)
    return {"completed": [], "errors": [], "started_at": datetime.now(timezone.utc).isoformat()}


def save_checkpoint(batch_id: str, data: dict):
    """Save checkpoint after every single item."""
    cp_path = get_checkpoint_path(batch_id)
    data["last_saved"] = datetime.now(timezone.utc).isoformat()
    with open(cp_path, "w") as f:
        json.dump(data, f, indent=2)


# ============================================================
# Extraction logging
# ============================================================

def log_extraction(file_path: str, mode: str, success: bool, details: str = ""):
    """Log an extraction event."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = LOG_DIR / f"{today}_extractions.md"

    now = datetime.now().strftime("%H:%M:%S")
    status = "OK" if success else "FAIL"
    entry = f"- [{now}] [{status}] [{mode}] {file_path}"
    if details:
        entry += f" — {details}"
    entry += "\n"

    with open(log_file, "a", encoding="utf-8") as f:
        if log_file.stat().st_size == 0:
            f.write(f"# Extraction Log — {today}\n\n")
        f.write(entry)


# ============================================================
# Central extraction store
# ============================================================

def get_week_number(dt=None):
    """Get week number within the month (W1-W5)."""
    if dt is None:
        dt = datetime.now()
    return f"W{(dt.day - 1) // 7 + 1}"


def identify_pillar_from_path(rel_path: str) -> str:
    """Extract pillar name from a relative path."""
    for part in rel_path.replace("\\", "/").split("/"):
        if part.startswith("PIL_"):
            return part
    return "UNKNOWN"


def identify_project_from_path(rel_path: str) -> str:
    """Extract project name from a relative path."""
    for part in rel_path.replace("\\", "/").split("/"):
        if part.startswith("PRJ_"):
            return part
    return ""


def write_to_central_store(data: dict, mode: str, source_path: str):
    """Write extraction output to the central store (Copy 2).
    Organised by mode and date with weekly subfolders."""
    now = datetime.now()
    month = now.strftime("%Y-%m")
    week = get_week_number(now)

    # Build central path: EXTRACTIONS/by_mode/<mode>/YYYY-MM/WN/
    mode_dir = CENTRAL_STORE / "by_mode" / mode / month / week
    mode_dir.mkdir(parents=True, exist_ok=True)

    # Build filename: original_name__PILLAR.extract_mode.json
    source_name = Path(source_path).stem
    pillar = identify_pillar_from_path(source_path)
    safe_name = f"{source_name}__{pillar}"

    json_path = mode_dir / f"{safe_name}.extract_{mode}.json"
    md_path = mode_dir / f"{safe_name}.extract_{mode}.md"

    write_json_output(data, json_path)
    write_markdown_output(data, mode, md_path)

    print(f"  Central: {json_path.relative_to(V7_ROOT)}")
    return str(json_path.relative_to(V7_ROOT))


def update_extraction_index(data: dict, mode: str, source_path: str, central_path: str):
    """Append this extraction to the master EXTRACTION_INDEX.json."""
    CENTRAL_STORE.mkdir(parents=True, exist_ok=True)

    # Load existing index
    if EXTRACTION_INDEX.exists():
        with open(EXTRACTION_INDEX, "r", encoding="utf-8") as f:
            index = json.load(f)
    else:
        index = {"extractions": [], "last_updated": ""}

    # Count items extracted
    item_count = 0
    categories_found = []
    if mode in ("copy", "copy_sales"):
        for cat, items in data.get("categories", {}).items():
            if items:
                categories_found.append(cat)
                item_count += len(items)
    elif mode == "book":
        for cat, items in data.get("categories", {}).items():
            if items:
                categories_found.append(cat)
                item_count += len(items)
    elif mode in ("domains", "27_domains"):
        for num, domain in data.get("domains", {}).items():
            if domain.get("items"):
                categories_found.append(f"domain_{num}")
                item_count += len(domain["items"])
    elif mode in ("thread", "ekx1_thread"):
        for key, section in data.get("sections", {}).items():
            if section.get("items"):
                categories_found.append(key)
                item_count += len(section["items"])

    # Build index entry
    entry = {
        "source_file": source_path,
        "mode": mode,
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "pillar": identify_pillar_from_path(source_path),
        "project": identify_project_from_path(source_path),
        "output_central": central_path,
        "output_alongside": source_path + f".extract_{mode}.json",
        "categories_found": categories_found,
        "item_count": item_count,
        "api_used": data.get("api_used", ""),
        "summary": data.get("summary", ""),
    }

    index["extractions"].append(entry)
    index["last_updated"] = datetime.now(timezone.utc).isoformat()
    index["total_extractions"] = len(index["extractions"])

    with open(EXTRACTION_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)


def update_category_aggregates(data: dict, mode: str, source_path: str):
    """Append extracted items to the by_category aggregation files.
    Each category gets a JSON file that collects ALL items of that type
    across every extraction ever run."""
    cat_dir = CENTRAL_STORE / "by_category"
    cat_dir.mkdir(parents=True, exist_ok=True)

    pillar = identify_pillar_from_path(source_path)
    project = identify_project_from_path(source_path)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Determine which categories to aggregate
    categories = {}
    if mode in ("copy", "copy_sales"):
        categories = data.get("categories", {})
    elif mode == "book":
        categories = data.get("categories", {})
    elif mode in ("domains", "27_domains"):
        # For domains, aggregate by domain name
        for num, domain in data.get("domains", {}).items():
            domain_name = domain.get("name", f"domain_{num}").lower().replace(" ", "_").replace("&", "and")
            domain_name = "".join(c for c in domain_name if c.isalnum() or c == "_")
            categories[f"domain_{num}_{domain_name}"] = domain.get("items", [])
    elif mode in ("thread", "ekx1_thread"):
        for key, section in data.get("sections", {}).items():
            categories[key] = section.get("items", [])

    for cat_key, items in categories.items():
        if not items:
            continue

        cat_file = cat_dir / f"{cat_key}.json"

        # Load existing
        if cat_file.exists():
            with open(cat_file, "r", encoding="utf-8") as f:
                cat_data = json.load(f)
        else:
            cat_data = {"category": cat_key, "items": [], "last_updated": ""}

        # Append new items with provenance
        for item in items:
            cat_data["items"].append({
                "text": item if isinstance(item, str) else str(item),
                "source": source_path,
                "pillar": pillar,
                "project": project,
                "date": date,
                "mode": mode,
            })

        cat_data["last_updated"] = datetime.now(timezone.utc).isoformat()
        cat_data["total_items"] = len(cat_data["items"])

        with open(cat_file, "w", encoding="utf-8") as f:
            json.dump(cat_data, f, indent=2, ensure_ascii=False)


# ============================================================
# PostgreSQL logging
# ============================================================

def log_extraction_to_db(data: dict, mode: str, source_path: str, central_path: str):
    """Log extraction to PostgreSQL v7_extractions table."""
    try:
        import psycopg2
        from psycopg2.extras import RealDictCursor
    except ImportError:
        return  # psycopg2 not installed, skip DB logging

    conn = psycopg2.connect(dbname="enterprise_os", user="postgres", host="localhost")
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Count items and categories
    item_count = 0
    categories_found = []
    if mode in ("copy", "copy_sales"):
        for cat, items in data.get("categories", {}).items():
            if items:
                categories_found.append(cat)
                item_count += len(items)
    elif mode == "book":
        for cat, items in data.get("categories", {}).items():
            if items:
                categories_found.append(cat)
                item_count += len(items)
    elif mode in ("domains", "27_domains"):
        for num, domain in data.get("domains", {}).items():
            if domain.get("items"):
                categories_found.append(f"domain_{num}")
                item_count += len(domain["items"])
    elif mode in ("thread", "ekx1_thread"):
        for key, section in data.get("sections", {}).items():
            if section.get("items"):
                categories_found.append(key)
                item_count += len(section["items"])

    # Get active session
    cur.execute("SELECT id FROM v7_sessions WHERE status = 'active' ORDER BY id DESC LIMIT 1")
    session_row = cur.fetchone()
    session_id = session_row["id"] if session_row else None

    cur.execute("""
        INSERT INTO v7_extractions
            (source_file, mode, api_used, pillar, project, item_count,
             categories_found, summary, extraction_data,
             output_alongside, output_central,
             prompt_tokens, completion_tokens, session_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        source_path,
        mode,
        data.get("api_used", "deepseek"),
        identify_pillar_from_path(source_path),
        identify_project_from_path(source_path),
        item_count,
        categories_found,
        data.get("summary", ""),
        json.dumps(data),
        source_path + f".extract_{mode}.json",
        central_path,
        data.get("tokens", {}).get("prompt", 0),
        data.get("tokens", {}).get("completion", 0),
        session_id,
    ))

    conn.commit()
    conn.close()


# ============================================================
# Core extraction function
# ============================================================

def extract_file(file_path: Path, mode: str, api: str = "deepseek",
                 output_dir: Path = None) -> dict:
    """Run extraction on a single file. Returns the extraction result."""

    # Select prompt
    prompts = {
        "domains": PROMPT_27_DOMAINS,
        "thread": PROMPT_EKX1_THREAD,
        "copy": PROMPT_COPY_SALES,
        "book": PROMPT_BOOK,
    }
    if mode not in prompts:
        raise ValueError(f"Unknown mode: {mode}. Use: {', '.join(prompts.keys())}")

    prompt = prompts[mode]
    system_msg = "You are a precise extraction specialist. Always respond with valid JSON only. No markdown wrapping, no explanation, just the JSON object."

    # Read content
    content = read_file_full(file_path)
    if not content.strip():
        raise RuntimeError(f"File is empty: {file_path}")

    print(f"  Reading: {file_path.name} ({len(content):,} chars)")

    # Chunk if necessary
    chunks = chunk_content(content)
    print(f"  Chunks: {len(chunks)}")

    # Process each chunk
    results = []
    total_prompt_tokens = 0
    total_completion_tokens = 0

    for i, chunk in enumerate(chunks):
        if len(chunks) > 1:
            chunk_header = f"\n[CHUNK {i+1} of {len(chunks)}]\n"
        else:
            chunk_header = ""

        user_content = prompt + chunk_header + chunk
        print(f"  Sending chunk {i+1}/{len(chunks)} to {api}...")

        start = time.time()
        response = call_api(api, system_msg, user_content)
        elapsed = time.time() - start

        total_prompt_tokens += response["prompt_tokens"]
        total_completion_tokens += response["completion_tokens"]
        print(f"  Received ({elapsed:.1f}s, {response['completion_tokens']} tokens out)")

        # Parse JSON
        parsed = parse_json_response(response["content"])
        results.append(parsed)

    # Merge chunks if needed
    if mode == "domains":
        final = merge_domain_extractions(results)
    else:
        final = merge_generic_extractions(results, mode)

    # Ensure metadata
    rel_path = str(file_path.relative_to(V7_ROOT)) if file_path.is_relative_to(V7_ROOT) else str(file_path)
    final["source_file"] = rel_path
    final["extraction_date"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    final["extraction_mode"] = mode
    final["api_used"] = api
    final["tokens"] = {
        "prompt": total_prompt_tokens,
        "completion": total_completion_tokens,
        "total": total_prompt_tokens + total_completion_tokens,
    }

    # Determine output paths
    if output_dir:
        out_base = output_dir / file_path.name
    else:
        out_base = file_path

    json_path = Path(str(out_base) + f".extract_{mode}.json")
    md_path = Path(str(out_base) + f".extract_{mode}.md")

    # Write alongside outputs (Copy 1)
    write_json_output(final, json_path)
    write_markdown_output(final, mode, md_path)
    print(f"  Alongside: {json_path.name}")
    print(f"  Alongside: {md_path.name}")

    # Write to central store (Copy 2)
    central_path = write_to_central_store(final, mode, rel_path)

    # Update master index
    update_extraction_index(final, mode, rel_path, central_path)
    print(f"  Index: EXTRACTION_INDEX.json updated")

    # Update category aggregates
    update_category_aggregates(final, mode, rel_path)
    print(f"  Categories: by_category/ updated")

    # Log to PostgreSQL
    try:
        log_extraction_to_db(final, mode, rel_path, central_path)
        print(f"  Database: v7_extractions row added")
    except Exception as e:
        print(f"  Database: SKIP (PostgreSQL not available: {e})")

    return final


# ============================================================
# Batch processing
# ============================================================

def extract_batch(folder: Path, mode: str, api: str = "deepseek",
                  output_dir: Path = None, ext_filter: str = None,
                  resume: bool = False, dry_run: bool = False):
    """Run extraction on all files in a folder."""

    if not folder.exists():
        print(f"ERROR: Folder not found: {folder}")
        sys.exit(1)

    # Collect files
    files = []
    for f in sorted(folder.rglob("*")):
        if not f.is_file():
            continue
        if f.suffix.lower() not in VALID_EXTENSIONS:
            continue
        if ext_filter and f.suffix.lower() != ext_filter:
            continue
        # Skip extraction output files
        if ".extract_" in f.name:
            continue
        files.append(f)

    print(f"Found {len(files)} files to process in {folder}")

    if dry_run:
        print("\nDRY RUN — would process:")
        for f in files:
            size = f.stat().st_size
            print(f"  {f.relative_to(V7_ROOT) if f.is_relative_to(V7_ROOT) else f} ({size:,} bytes)")
        print(f"\nTotal: {len(files)} files")
        return

    # Checkpoint setup
    batch_id = f"{mode}_{folder.name}_{datetime.now().strftime('%Y%m%d_%H%M')}"
    checkpoint = load_checkpoint(batch_id) if resume else {
        "completed": [], "errors": [], "started_at": datetime.now(timezone.utc).isoformat()
    }

    completed_files = set(checkpoint.get("completed", []))
    total = len(files)
    success = 0
    errors = 0

    print(f"Batch ID: {batch_id}")
    if resume and completed_files:
        print(f"Resuming: {len(completed_files)} already done, {total - len(completed_files)} remaining")
    print(f"Mode: {mode} | API: {api}")
    print(f"{'='*60}")

    for idx, file_path in enumerate(files, 1):
        rel = str(file_path.relative_to(V7_ROOT)) if file_path.is_relative_to(V7_ROOT) else str(file_path)

        if rel in completed_files:
            print(f"[{idx}/{total}] SKIP (already done): {file_path.name}")
            continue

        print(f"\n[{idx}/{total}] Processing: {file_path.name}")

        try:
            extract_file(file_path, mode, api, output_dir)
            success += 1
            checkpoint["completed"].append(rel)
            log_extraction(rel, mode, True)
        except Exception as e:
            errors += 1
            error_msg = str(e)[:200]
            print(f"  ERROR: {error_msg}")
            checkpoint["errors"].append({"file": rel, "error": error_msg})
            log_extraction(rel, mode, False, error_msg)

        # CHECKPOINT AFTER EVERY ITEM
        save_checkpoint(batch_id, checkpoint)

        # Brief pause to avoid rate limits
        if idx < total:
            time.sleep(1)

    print(f"\n{'='*60}")
    print(f"BATCH COMPLETE")
    print(f"  Total:     {total}")
    print(f"  Success:   {success}")
    print(f"  Errors:    {errors}")
    print(f"  Skipped:   {len(completed_files)}")
    print(f"  Checkpoint: {get_checkpoint_path(batch_id)}")
    print(f"{'='*60}")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enterprise OS V7 — Content Extraction Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  domains    27-domain classification pass (any content)
  thread     EKX-1 20-section extraction (AI chat threads)
  copy       Copy/sales extraction (benefits, USPs, hooks, etc.)
  book       Book extraction (proofs, arguments, rhetorical devices, etc.)
  batch      Process an entire folder

Examples:
  python v7_extract.py domains myfile.md
  python v7_extract.py copy 06_DOMAIN_PILLARS/PIL_19_PROPERTY/01_INPUT/research.md
  python v7_extract.py batch 06_DOMAIN_PILLARS/PIL_03_COPY/01_INPUT --mode copy
  python v7_extract.py batch some_folder --mode domains --resume
        """,
    )
    parser.add_argument("command", help="Extraction mode or 'batch'")
    parser.add_argument("target", help="File path or folder (for batch)")
    parser.add_argument("--mode", default="domains", help="Extraction mode for batch (default: domains)")
    parser.add_argument("--api", default="deepseek", choices=["deepseek", "claude"],
                        help="API to use (default: deepseek)")
    parser.add_argument("--output", default=None, help="Override output folder")
    parser.add_argument("--ext", default=None, help="Filter by extension in batch mode (e.g. .md)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without calling API")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")

    args = parser.parse_args()

    # Resolve paths
    target = Path(args.target)
    if not target.is_absolute():
        target = V7_ROOT / target
    output_dir = Path(args.output) if args.output else None

    if args.command == "batch":
        extract_batch(target, args.mode, args.api, output_dir, args.ext, args.resume, args.dry_run)
    elif args.command in ("domains", "thread", "copy", "book"):
        if not target.exists():
            print(f"ERROR: File not found: {target}")
            sys.exit(1)
        if args.dry_run:
            size = target.stat().st_size
            print(f"DRY RUN — would process: {target} ({size:,} bytes) with mode={args.command}")
            return
        try:
            result = extract_file(target, args.command, args.api, output_dir)
            log_extraction(str(target), args.command, True)
            print(f"\nExtraction complete.")
        except Exception as e:
            log_extraction(str(target), args.command, False, str(e)[:200])
            print(f"\nERROR: {e}")
            sys.exit(1)
    else:
        print(f"Unknown command: {args.command}")
        print("Use: domains, thread, copy, book, or batch")
        sys.exit(1)


if __name__ == "__main__":
    main()
