#!/usr/bin/env python3
"""
Page Picker API — serves the page selection tool.
For each page across PCL, Fitness, Enterprise builds:
- Shows matching kit components with thumbnail previews
- Allows selection and saving

Run: python page_picker.py
Then open: http://localhost:8080
"""
import sys, io, json, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "dbname": "ui_library",
    "user": "postgres",
    "host": "localhost"
}

SELECTIONS_FILE = os.path.join(os.path.dirname(__file__), "page_selections.json")

# The 38 target kit file keys
TARGET_KIT_KEYS = [
    '6hCuwRI0GsBmIOJelAVpND', '88CZ1cuAGLBYxXI743aO1I', 'BeqInrAMGdwwDnD4sAhpXi',
    'hclnmuRp2VS1UPFmuYfjka', 'qdZCYxMCCybLNTbpiHhRvH', 'eQpOuv9h6qVnEwzvZ1iTDV',
    'wGr7jrSaR6Psznp6O69P1V', 'NPFFSPpbO27fWSX0cUaFJO', 'XK3d5YHdoyV60avw3cpQCo',
    'TWNCPNCVswFQwUKMq99dYI', 'ibUAqii0Lx1BiP6OvtME0l', 'U9Vy8iVwTyjDwRfYTOyPuV',
    'lakQUjeKUyotRErsMpD7Vv', '24h3Ty1OtmTV6m0ROHb7DB', '1zuA1R87EIxMLR1rYKmSVo',
    'sSCteJZwatQ7GmKv3reBHu', 'yNs5Y0aYN5SxbfL9tGw92R', 'rpAaabZ8WnW6yT4vHXhpIA',
    'gX3vYcBHFTbMdSkgJOcTaV', 'AYzFX61wgcyaxHCpg55NoD', 'FcQ8RuwXhtMfNXOJDlZYS7',
    'w8CnqCqnEHoPup4g4hmCMF', '4DjXTYs8judIaV978izwUU', 'MrAzer3g7KCoWwMO9RE4Bi',
    'S5N0Ln2ukNq8Ip4JqijOem', 'Sgp1yeAlNiDG5XIjVpZj5c', 'BaKQFtxDIp1sqyK51elWWl',
    'ynPYq67ECusq8JJQZndH3E', 'Vjl4wOACqV9Pquz6CoNb60', 'tI3hUHvXOIzWNiGDAWg30h',
    'EXhqJe4YbbyS0Hegl8OEDk', '7vWKAMm6109mpiA3K5D7Vw', 'xkTk1662YKoVNNSZt1FyRQ',
    '9nH8sfE7Yo6ZDFbY0zuKOd', 'C1nzSmYcqSF8W7qK5Q2YRr', 'xjdV652MDlXv5za86ou2wo',
    '5qqOJsUAYyWNtnKrT7Ffb6', '6vbYtA59S9MUGAPUYiyIgB', 'rPqAZVsUkjaVdtl9hNF6Ma',
]

# Page definitions with search criteria
PAGES = [
    # ===================== COMMON ANCILLARY =====================
    {"id": "common_landing", "build": "Common", "name": "Landing / Marketing Page", "phase": "MVP",
     "features": "Hero section, feature blocks, testimonials, pricing table, CTA sections, trust badges, FAQ accordion",
     "search": ["landing", "hero", "features", "pricing", "CTA"],
     "categories": ["hero", "features", "pricing", "testimonials", "content"]},

    {"id": "common_auth", "build": "Common", "name": "Auth (Sign Up / Sign In)", "phase": "MVP",
     "features": "Login form, register form, social login buttons, forgot password, email verification",
     "search": ["login", "sign in", "sign up", "register", "auth"],
     "categories": ["auth"]},

    {"id": "common_onboarding", "build": "Common", "name": "Onboarding / Wizard", "phase": "MVP",
     "features": "Multi-step form, progress indicator, preference selection, welcome screen",
     "search": ["onboarding", "wizard", "welcome", "setup", "getting started"],
     "categories": ["forms", "content"]},

    {"id": "common_settings", "build": "Common", "name": "Settings / Profile", "phase": "MVP",
     "features": "Profile form, preference toggles, notification settings, subscription management, avatar upload",
     "search": ["settings", "profile", "account", "preferences"],
     "categories": ["profile", "forms"]},

    {"id": "common_pricing", "build": "Common", "name": "Pricing / Subscription", "phase": "MVP",
     "features": "Pricing tiers, feature comparison, toggle monthly/annual, CTA buttons",
     "search": ["pricing", "subscription", "plan", "billing"],
     "categories": ["pricing"]},

    {"id": "common_404", "build": "Common", "name": "404 / Error Page", "phase": "MVP",
     "features": "Error message, illustration, back to home link",
     "search": ["404", "error", "not found", "empty"],
     "categories": ["empty"]},

    # ===================== PCL BUILD A: B2B PROMO =====================
    {"id": "pcl_presell_home", "build": "PCL", "name": "B2B Presell: Home", "phase": "MVP",
     "features": "Big Idea hero, Pre-Head, Sub Head, Lead, Unique Mechanism, Problems, Solutions, Story, Process, Who We Serve, Facts, Benefits, Services, CTAs, Nurturing, Discovery Call, FAQs, Objections, Team, Transform",
     "search": ["landing", "hero", "services", "about", "team", "FAQ", "CTA", "testimonial"],
     "categories": ["hero", "features", "testimonials", "content", "pricing"]},

    {"id": "pcl_presell_magazine", "build": "PCL", "name": "B2B Presell: Magazine", "phase": "MVP",
     "features": "Magazine concept presell, content showcase, editorial style, subscription CTA",
     "search": ["magazine", "editorial", "blog", "article", "content", "media"],
     "categories": ["content", "media", "hero"]},

    {"id": "pcl_presell_tv", "build": "PCL", "name": "B2B Presell: Connected TV", "phase": "MVP",
     "features": "Video/TV platform presell, streaming concept, channel showcase",
     "search": ["video", "streaming", "TV", "player", "media", "channel"],
     "categories": ["media", "hero", "content"]},

    {"id": "pcl_presell_platform", "build": "PCL", "name": "B2B Presell: Platform", "phase": "MVP",
     "features": "Platform overview presell, feature showcase, dashboard preview",
     "search": ["platform", "dashboard", "features", "overview", "SaaS"],
     "categories": ["hero", "features", "dashboard"]},

    {"id": "pcl_presell_podcasts", "build": "PCL", "name": "B2B Presell: Podcasts", "phase": "MVP",
     "features": "Podcast platform presell, episode showcase, host profiles",
     "search": ["podcast", "audio", "episode", "player", "media"],
     "categories": ["media", "content", "hero"]},

    {"id": "pcl_offers", "build": "PCL", "name": "B2B Offers / Funnels", "phase": "MVP",
     "features": "7 offer types: Free Property Video, Free Magazine Interview, Free Platform Membership, Sponsorship, Editorial, Video Package, Ad. Lead capture, conversion funnels",
     "search": ["offer", "lead", "funnel", "CTA", "form", "contact", "booking"],
     "categories": ["forms", "hero", "content"]},

    # ===================== PCL BUILD B: B2C MIRROR =====================
    {"id": "pcl_consumer_home", "build": "PCL", "name": "B2C Consumer: Home", "phase": "MVP",
     "features": "Consumer-facing mirror of B2B presell (without services). Community focus, content preview, platform access",
     "search": ["landing", "hero", "community", "content", "discover"],
     "categories": ["hero", "features", "content"]},

    # ===================== PCL BUILD D: PRO DASHBOARD =====================
    {"id": "pcl_pro_home", "build": "PCL", "name": "Pro Dashboard: Home", "phase": "MVP",
     "features": "Dashboard home, quick stats, recent activity, notifications, shortcuts to all 9 sections",
     "search": ["dashboard", "home", "overview", "stats", "analytics"],
     "categories": ["dashboard"]},

    {"id": "pcl_pro_content", "build": "PCL", "name": "Pro Dashboard: Content Management Hub", "phase": "MVP",
     "features": "Article editor, video upload, podcast manager, content calendar, draft/published status",
     "search": ["content", "editor", "articles", "manage", "upload", "CMS"],
     "categories": ["dashboard", "content", "forms"]},

    {"id": "pcl_pro_clients", "build": "PCL", "name": "Pro Dashboard: Client Management", "phase": "MVP",
     "features": "Client list, CRM, messaging, appointment booking, lead pipeline",
     "search": ["CRM", "client", "contacts", "leads", "pipeline", "messaging"],
     "categories": ["dashboard", "tables", "forms"]},

    {"id": "pcl_pro_analytics", "build": "PCL", "name": "Pro Dashboard: Analytics & Insights", "phase": "MVP",
     "features": "Traffic stats, engagement metrics, revenue tracking, content performance, charts and graphs",
     "search": ["analytics", "charts", "metrics", "statistics", "reports", "graph"],
     "categories": ["dashboard"]},

    {"id": "pcl_pro_profile", "build": "PCL", "name": "Pro Dashboard: Business Profile", "phase": "MVP",
     "features": "Company profile editor, portfolio showcase, team members, certifications, reviews",
     "search": ["profile", "business", "company", "portfolio", "team"],
     "categories": ["profile", "forms"]},

    {"id": "pcl_pro_marketing", "build": "PCL", "name": "Pro Dashboard: Marketing Tools", "phase": "MVP",
     "features": "Email campaigns, social media scheduler, ad manager, SEO tools",
     "search": ["marketing", "email", "campaign", "social", "ads"],
     "categories": ["dashboard", "forms"]},

    {"id": "pcl_pro_learning", "build": "PCL", "name": "Pro Dashboard: Learning Centre", "phase": "MVP",
     "features": "Course browser, video lessons, progress tracking, certifications",
     "search": ["learning", "courses", "education", "training", "lessons", "e-learning"],
     "categories": ["content", "media"]},

    {"id": "pcl_pro_community", "build": "PCL", "name": "Pro Dashboard: Community & Networking", "phase": "MVP",
     "features": "Forum, groups, events, networking, member directory",
     "search": ["community", "forum", "groups", "events", "social", "network"],
     "categories": ["content", "profile"]},

    {"id": "pcl_pro_settings", "build": "PCL", "name": "Pro Dashboard: Settings & Integrations", "phase": "MVP",
     "features": "Account settings, billing, API keys, integrations, team management",
     "search": ["settings", "integrations", "billing", "API", "team"],
     "categories": ["forms", "profile"]},

    # ===================== PCL BUILD E: CONSUMER DASHBOARD =====================
    {"id": "pcl_consumer_dash", "build": "PCL", "name": "Consumer Dashboard: Home", "phase": "MVP",
     "features": "Content feed, recommendations, saved items, activity, notifications",
     "search": ["dashboard", "feed", "home", "activity", "discover"],
     "categories": ["dashboard", "content"]},

    {"id": "pcl_consumer_social", "build": "PCL", "name": "Consumer Dashboard: Social", "phase": "MVP",
     "features": "Social feed, posts, comments, likes, shares, user interactions, following",
     "search": ["social", "feed", "posts", "comments", "community", "chat"],
     "categories": ["content", "profile"]},

    {"id": "pcl_consumer_content", "build": "PCL", "name": "Consumer Dashboard: Content Streams", "phase": "MVP",
     "features": "10 streams: Video, Article, Learning, Property, Projects, Jobs, Events, Experts, Q&A, Shop. Browse, filter, search",
     "search": ["browse", "content", "video", "article", "listing", "directory", "jobs", "events", "shop"],
     "categories": ["content", "media", "ecommerce", "cards"]},

    {"id": "pcl_consumer_property", "build": "PCL", "name": "Consumer Dashboard: Property Explorer", "phase": "MVP",
     "features": "Property search, map view, listings, filters, saved properties, agent contact",
     "search": ["property", "listing", "real estate", "map", "search", "filter"],
     "categories": ["cards", "forms", "content"]},

    {"id": "pcl_consumer_projects", "build": "PCL", "name": "Consumer Dashboard: My Projects", "phase": "MVP",
     "features": "Project tracker, timeline, budget, contractors, documents",
     "search": ["projects", "tracker", "timeline", "tasks", "kanban"],
     "categories": ["dashboard", "tables"]},

    # ===================== FITNESS MVP =====================
    {"id": "fit_ai_generator", "build": "Fitness", "name": "AI Workout Generator", "phase": "MVP",
     "features": "THE CORE. Chat interface, AI conversation, workout output cards, circumstance input (time/equipment/energy). AI learns preferences, adapts to circumstances, generates workouts from any exercise combo on the fly",
     "search": ["chat", "AI", "conversation", "message", "assistant", "bot"],
     "categories": ["other"]},

    {"id": "fit_active_workout", "build": "Fitness", "name": "Active Workout Mode", "phase": "MVP",
     "features": "Exercise-by-exercise guidance, video playback, timer, set/rep/weight logging, rest periods, form cues, previous performance, auto-advance, exercise swap",
     "search": ["workout", "exercise", "timer", "fitness", "training", "player"],
     "categories": ["media", "forms"]},

    {"id": "fit_exercise_library", "build": "Fitness", "name": "Exercise Library", "phase": "MVP",
     "features": "Browse/search 4,630 exercises, filter by muscle group, equipment, difficulty, movement pattern. Grid/list view",
     "search": ["library", "browse", "grid", "filter", "search", "cards", "list"],
     "categories": ["cards", "content", "tables"]},

    {"id": "fit_exercise_detail", "build": "Fitness", "name": "Exercise Detail", "phase": "MVP",
     "features": "Video demonstrations, muscle groups targeted, form tips, common mistakes, variations, progressions, related exercises",
     "search": ["detail", "video", "player", "info", "description"],
     "categories": ["media", "content", "profile"]},

    {"id": "fit_dashboard", "build": "Fitness", "name": "Dashboard / Home", "phase": "MVP",
     "features": "Today's AI suggestion, recent activity, streaks, quick stats, entry point. Workout history at a glance",
     "search": ["dashboard", "home", "overview", "stats", "activity"],
     "categories": ["dashboard"]},

    {"id": "fit_progress", "build": "Fitness", "name": "Progress & History", "phase": "MVP",
     "features": "Workout log, volume charts, frequency heatmap, PRs, body measurements, progress photos, trends over time",
     "search": ["progress", "analytics", "charts", "history", "statistics", "tracking"],
     "categories": ["dashboard"]},

    # ===================== FITNESS PHASE 2 =====================
    {"id": "fit_trainer_dir", "build": "Fitness", "name": "Trainer/Influencer Directory", "phase": "Phase 2",
     "features": "Marketplace directory, browse trainers and influencers, filter by specialty/location/price, ratings, connect",
     "search": ["directory", "listing", "marketplace", "browse", "filter", "profile"],
     "categories": ["cards", "content", "profile"]},

    {"id": "fit_trainer_detail", "build": "Fitness", "name": "Trainer Detail", "phase": "Phase 2",
     "features": "Individual trainer page, bio, certifications, programs offered, reviews, pricing, booking",
     "search": ["profile", "detail", "bio", "reviews", "booking"],
     "categories": ["profile", "content"]},

    {"id": "fit_programs", "build": "Fitness", "name": "Pre-built Programs", "phase": "Phase 2",
     "features": "Trainer-made programs, curated content, marketplace listings, buy/subscribe",
     "search": ["programs", "courses", "browse", "marketplace", "plans"],
     "categories": ["cards", "content", "ecommerce"]},

    {"id": "fit_social", "build": "Fitness", "name": "Social Feed", "phase": "Phase 2",
     "features": "Post routines, progress updates, journey milestones, comments, likes, community interaction",
     "search": ["social", "feed", "posts", "community", "timeline"],
     "categories": ["content", "profile"]},

    # ===================== ENTERPRISE (8 TABS) =====================
    {"id": "ent_hub", "build": "Enterprise", "name": "Hub (Home Screen)", "phase": "MVP",
     "features": "8 module tiles with health indicators, Morning Brief, Org Pulse (L5+), State Snapshot (L7). Adapts by permission level L1-L7",
     "search": ["dashboard", "home", "overview", "tiles", "grid", "cards", "stats"],
     "categories": ["dashboard"]},

    {"id": "ent_nav_goals", "build": "Enterprise", "name": "Navigation: Goal Intake Wizard", "phase": "MVP",
     "features": "Stream-of-consciousness portal, AI asks refinement questions, generates 5A plan (Alignment→Assets). Multi-step wizard",
     "search": ["wizard", "onboarding", "form", "intake", "goals", "setup"],
     "categories": ["forms", "content"]},

    {"id": "ent_nav_health", "build": "Enterprise", "name": "Navigation: Goal Health Dashboard", "phase": "MVP",
     "features": "Heatmap of active objectives, Health Scores 1-10, alignment drift, activity completion, decision velocity",
     "search": ["dashboard", "analytics", "heatmap", "health", "metrics", "charts"],
     "categories": ["dashboard"]},

    {"id": "ent_nav_brief", "build": "Enterprise", "name": "Navigation: Morning Brief", "phase": "MVP",
     "features": "Daily newspaper: yesterday's wins, today's top 3 priorities, pre-calibrated by system. Role-appropriate content",
     "search": ["brief", "digest", "daily", "summary", "notification", "report"],
     "categories": ["dashboard", "content"]},

    {"id": "ent_cmd_cockpit", "build": "Enterprise", "name": "Command Deck: Active Cockpit", "phase": "MVP",
     "features": "3-pane layout: running log (left), AI chat (middle), outputs pane (right). Start/Work/End session loop. Total Recall",
     "search": ["chat", "AI", "workspace", "editor", "console", "terminal", "split"],
     "categories": ["other", "dashboard"]},

    {"id": "ent_cmd_sessions", "build": "Enterprise", "name": "Command Deck: Session History", "phase": "MVP",
     "features": "Previous sessions with auto-generated summaries, searchable, full provenance chain",
     "search": ["history", "list", "timeline", "log", "sessions", "table"],
     "categories": ["tables", "dashboard"]},

    {"id": "ent_cmd_agents", "build": "Enterprise", "name": "Command Deck: Agent Registry", "phase": "MVP",
     "features": "Library of 80+ role profiles, activate per session, specialised lens per agent",
     "search": ["directory", "list", "cards", "profiles", "registry", "agents"],
     "categories": ["cards", "profile"]},

    {"id": "ent_lib_inbox", "build": "Enterprise", "name": "Knowledge Library: Ingestion Inbox", "phase": "MVP",
     "features": "Global inbox: Pending/Processing/Routed/Unrouted pipeline, file upload, URL sniffer, multi-source",
     "search": ["inbox", "upload", "pipeline", "queue", "notifications", "status"],
     "categories": ["dashboard", "forms"]},

    {"id": "ent_lib_search", "build": "Enterprise", "name": "Knowledge Library: Semantic Search", "phase": "MVP",
     "features": "Universal search across all pillars, lattice filters by project/domain/date, hybrid vector + keyword + metadata",
     "search": ["search", "results", "filter", "browse", "query"],
     "categories": ["content", "tables"]},

    {"id": "ent_lib_extract", "build": "Enterprise", "name": "Knowledge Library: Artifact Extraction", "phase": "MVP",
     "features": "Split-screen: raw source (left) vs 29 extracted artifact types (right). EKX-1 methodology in action",
     "search": ["editor", "split", "comparison", "viewer", "detail"],
     "categories": ["content", "other"]},

    {"id": "ent_pillars_grid", "build": "Enterprise", "name": "Domain Pillars: Pillar Grid", "phase": "MVP",
     "features": "Bird's-eye view of 23+ pillars, item counts, health status, freshness scores, Canonical vs Staging ratio",
     "search": ["grid", "cards", "overview", "tiles", "health", "status"],
     "categories": ["dashboard", "cards"]},

    {"id": "ent_factory_projects", "build": "Enterprise", "name": "Build Factory: Project Registry", "phase": "MVP",
     "features": "Active builds with maturity grades (Speculative/Operational/Production-Ready), 9-folder scaffold",
     "search": ["projects", "list", "kanban", "boards", "pipeline", "tasks"],
     "categories": ["dashboard", "tables"]},

    {"id": "ent_factory_pipeline", "build": "Enterprise", "name": "Build Factory: 17-Step Mission Control", "phase": "MVP",
     "features": "Linear production pipeline tracking 17 build stages across 4 tracks (Intelligence, Foundation, Brand, Build)",
     "search": ["pipeline", "steps", "tracker", "progress", "timeline", "workflow"],
     "categories": ["dashboard", "other"]},

    {"id": "ent_ops_health", "build": "Enterprise", "name": "Operations: System Health Dashboard", "phase": "MVP",
     "features": "Org heatmap, ingestion stats, routing accuracy, pillar freshness scores, vital signs",
     "search": ["health", "monitoring", "heatmap", "metrics", "system", "status"],
     "categories": ["dashboard"]},

    {"id": "ent_ops_cascade", "build": "Enterprise", "name": "Operations: Strategic Goal Cascade", "phase": "MVP",
     "features": "Visual tree: individual tasks auto-update dept goals auto-update CEO strategic objectives",
     "search": ["tree", "hierarchy", "goals", "cascade", "org chart", "flow"],
     "categories": ["dashboard", "other"]},
]


def get_db():
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)


@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "page_picker.html")


@app.route("/api/pages")
def list_pages():
    """Return all page definitions grouped by build."""
    builds = {}
    for p in PAGES:
        b = p["build"]
        if b not in builds:
            builds[b] = []
        builds[b].append({
            "id": p["id"],
            "name": p["name"],
            "phase": p["phase"],
            "features": p["features"],
        })
    return jsonify(builds)


@app.route("/api/page/<page_id>/components")
def page_components(page_id):
    """Get matching components for a page from the 38 target kits."""
    page = next((p for p in PAGES if p["id"] == page_id), None)
    if not page:
        return jsonify({"error": "Page not found"}), 404

    conn = get_db()
    cur = conn.cursor()

    try:
        # Build search conditions from page's search terms and categories
        search_terms = page.get("search", [])
        categories = page.get("categories", [])

        # Build query: match by category OR search text, filtered to target kits and width > 600
        placeholders_kits = ','.join(['%s'] * len(TARGET_KIT_KEYS))

        # Category matching
        cat_conditions = []
        cat_params = []
        for cat in categories:
            cat_conditions.append("llm_category = %s")
            cat_params.append(cat)

        # Search text matching
        search_conditions = []
        search_params = []
        for term in search_terms:
            search_conditions.append("search_text ILIKE %s")
            search_params.append(f"%{term}%")

        # Combine: (any category match OR any search match) AND target kits AND width > 600
        inner_conditions = []
        inner_params = []
        if cat_conditions:
            inner_conditions.append(f"({' OR '.join(cat_conditions)})")
            inner_params.extend(cat_params)
        if search_conditions:
            inner_conditions.append(f"({' OR '.join(search_conditions)})")
            inner_params.extend(search_params)

        where_inner = " OR ".join(inner_conditions) if inner_conditions else "TRUE"

        query = f"""
            SELECT id, name, component_level, width, height,
                   file_key, file_name, page_name, thumbnail_url,
                   llm_category, llm_subcategory, device_type
            FROM component_library
            WHERE file_key IN ({placeholders_kits})
              AND width > 600
              AND ({where_inner})
            ORDER BY file_name, page_name, name
            LIMIT 500
        """
        params = list(TARGET_KIT_KEYS) + inner_params

        cur.execute(query, params)
        results = cur.fetchall()

        # Group by kit
        by_kit = {}
        for r in results:
            kit = r['file_name'] or r['file_key']
            if kit not in by_kit:
                by_kit[kit] = []
            by_kit[kit].append({
                "id": r['id'],
                "name": r['name'],
                "level": r['component_level'],
                "width": r['width'],
                "height": r['height'],
                "kit": kit,
                "file_key": r['file_key'],
                "page": r['page_name'],
                "thumbnail_url": r['thumbnail_url'],
                "category": r['llm_category'],
                "subcategory": r['llm_subcategory'],
                "device": r['device_type'],
            })

        return jsonify({
            "page": {
                "id": page["id"],
                "name": page["name"],
                "build": page["build"],
                "phase": page["phase"],
                "features": page["features"],
            },
            "total": len(results),
            "by_kit": by_kit,
        })

    finally:
        cur.close()
        conn.close()


@app.route("/api/selections", methods=["GET"])
def get_selections():
    """Get saved selections."""
    try:
        with open(SELECTIONS_FILE, 'r') as f:
            return jsonify(json.load(f))
    except:
        return jsonify({})


@app.route("/api/selections", methods=["POST"])
def save_selections():
    """Save selections."""
    data = request.get_json()
    with open(SELECTIONS_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    return jsonify({"success": True})


if __name__ == "__main__":
    print("\n" + "="*60)
    print("Page Picker — Component Selection Tool")
    print("="*60)
    print("\nOpen: http://localhost:8080")
    print("="*60 + "\n")
    app.run(host="0.0.0.0", port=8080, debug=True)
