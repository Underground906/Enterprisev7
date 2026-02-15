# LEADENGINE — DEPLOYMENT & HOSTING SPEC
> Created: 2026-02-15
> Two models: Hosted (you manage) and Container (their infrastructure or dedicated)

---

## DEPLOYMENT MODELS

### Model A: HOSTED (Default — £5,000/mo)
You host everything. Client installs one JS snippet. They access their dashboard via your domain.

```
Client's Website                    Your Infrastructure
┌──────────────┐                   ┌──────────────────────┐
│              │                   │   LeadEngine Cloud    │
│  <script>    │───── API ────────▶│                      │
│  1 line      │                   │  ┌────────────────┐  │
│  snippet     │◀── Widget CDN ────│  │ Multi-tenant   │  │
│              │                   │  │ API Server     │  │
└──────────────┘                   │  └────────────────┘  │
                                   │  ┌────────────────┐  │
Client's Browser                   │  │ PostgreSQL     │  │
┌──────────────┐                   │  │ (shared, data  │  │
│ Dashboard at │                   │  │  isolated by   │  │
│ app.lead     │───── HTTPS ──────▶│  │  tenant_id)    │  │
│ engine.io/   │                   │  └────────────────┘  │
│ clientname   │                   │  ┌────────────────┐  │
└──────────────┘                   │  │ Redis + Vector │  │
                                   │  └────────────────┘  │
                                   └──────────────────────┘
```

**Client does:**
1. Adds 1 JS snippet to their website `<head>`
2. Logs into dashboard at app.leadengine.io
3. Uploads knowledge base
4. Configures branding + team

**You manage:**
- All infrastructure
- Updates and patches
- Scaling
- Backups
- SSL
- Monitoring

**Pros:** Zero tech burden for client. Instant setup. Easy to manage many clients.
**Cons:** Shared infrastructure. Some clients won't trust it (data concerns).

---

### Model B: DEDICATED CONTAINER (Premium — £7,500/mo or £5k + setup fee)
Client gets their own isolated instance. Can run on YOUR servers (dedicated) or THEIR servers (self-hosted).

```
Client's Website                    Dedicated Container
┌──────────────┐                   ┌──────────────────────┐
│              │                   │  client.leadengine.io │
│  <script     │───── API ────────▶│  OR                  │
│  src="client │                   │  leads.clientsite.com │
│  .leadengine │                   │                      │
│  .io/pixel"  │◀── Widget ────────│  ┌─ Docker Compose ─┐│
│              │                   │  │ API Server       ││
└──────────────┘                   │  │ PostgreSQL       ││
                                   │  │ Redis            ││
Client's Browser                   │  │ ChromaDB         ││
┌──────────────┐                   │  │ Nginx            ││
│ Dashboard at │                   │  │ Worker           ││
│ leads.client │───── HTTPS ──────▶│  └──────────────────┘│
│ site.com     │                   └──────────────────────┘
└──────────────┘                   Runs on: Your VPS OR their AWS/Azure/GCP
```

**Client does:**
1. Provides domain/subdomain (leads.theirsite.com)
2. Points DNS to container IP
3. Same onboarding as hosted

**Deployment team does:**
1. Spin up container
2. Configure env variables
3. Set up SSL
4. Run initial setup script
5. Hand over

**Pros:** Full data isolation. Custom domain. Client owns their data. Premium positioning.
**Cons:** More infrastructure to manage per client. Higher cost.

---

## THE JS SNIPPET (What Goes On Their Website)

This is what makes it "feel like it's theirs". One script tag:

```html
<!-- LeadEngine — paste in <head> -->
<script>
  (function(w,d,s,o,f,js,fjs){
    w['LeadEngine']=o;w[o]=w[o]||function(){
    (w[o].q=w[o].q||[]).push(arguments)};
    js=d.createElement(s);fjs=d.getElementsByTagName(s)[0];
    js.id=o;js.src=f;js.async=1;fjs.parentNode.insertBefore(js,fjs);
  }(window,document,'script','le','https://cdn.leadengine.io/pixel.js'));
  le('init', 'CLIENT_ID_HERE');
</script>
```

**What this script does:**
1. Loads the tracking pixel (captures IP, user agent, pages, events, cookies)
2. Loads the concierge widget (chat bubble in corner)
3. All branding (colours, logo, fonts, greeting) pulled from config — no code changes needed
4. Runs in Shadow DOM — completely isolated from their site's CSS/JS, zero conflicts
5. ~30KB gzipped initial load, async, doesn't block their page

**The widget appears branded as THEIR company**, not yours. Their logo, their colours, their greeting message. Visitors never know it's LeadEngine unless they look at network requests.

---

## DOCKER COMPOSE ARCHITECTURE (Per-Client Container)

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    image: leadengine/api:latest
    environment:
      - DATABASE_URL=postgresql://le:${DB_PASS}@db:5432/leadengine
      - REDIS_URL=redis://redis:6379
      - CHROMA_URL=http://chromadb:8000
      - LLM_API_KEY=${CLAUDE_API_KEY}
      - IPINFO_TOKEN=${IPINFO_TOKEN}
      - CLIENT_ID=${CLIENT_ID}
      - CLIENT_DOMAIN=${CLIENT_DOMAIN}
      - BRAND_PRIMARY=${BRAND_COLOUR}
      - BRAND_LOGO=${LOGO_URL}
      - SMTP_HOST=${SMTP_HOST}
      - SMTP_USER=${SMTP_USER}
      - SMTP_PASS=${SMTP_PASS}
      - SLACK_WEBHOOK=${SLACK_WEBHOOK}
    ports:
      - "3000:3000"
    depends_on:
      - db
      - redis
      - chromadb
    restart: always

  worker:
    image: leadengine/worker:latest
    environment:
      - DATABASE_URL=postgresql://le:${DB_PASS}@db:5432/leadengine
      - REDIS_URL=redis://redis:6379
      - LLM_API_KEY=${CLAUDE_API_KEY}
    depends_on:
      - db
      - redis
    restart: always

  db:
    image: postgres:16
    environment:
      - POSTGRES_DB=leadengine
      - POSTGRES_USER=le
      - POSTGRES_PASSWORD=${DB_PASS}
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: always

  redis:
    image: redis:7-alpine
    restart: always

  chromadb:
    image: chromadb/chroma:latest
    volumes:
      - chromadata:/chroma/chroma
    restart: always

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./certs:/etc/nginx/certs
    depends_on:
      - api
    restart: always

volumes:
  pgdata:
  chromadata:
```

**Server requirements:**
- 4GB RAM minimum (8GB recommended)
- 2 CPU cores minimum
- 50GB storage
- Ubuntu 22.04+ or any Docker-capable OS
- Cost: ~$20-40/mo on DigitalOcean/Hetzner

---

## DEPLOYMENT PROCESS (Step by Step)

### For Hosted (Model A) — 15 minutes

| Step | Who | What | Time |
|:---:|-----|------|:---:|
| 1 | You/automated | Create tenant in admin panel (client name, plan, domain) | 1 min |
| 2 | You/automated | Generate client ID + JS snippet | Instant |
| 3 | Client | Add JS snippet to their website | 5 min |
| 4 | Client | Log into dashboard, upload knowledge base | 10 min |
| 5 | Client | Configure branding (colours, logo, greeting) | 5 min |
| 6 | Automated | Knowledge base vectorised, concierge ready | 2-5 min |
| **Total** | | | **~15 min** |

### For Dedicated Container (Model B) — 30 minutes

| Step | Who | What | Time |
|:---:|-----|------|:---:|
| 1 | Support | Provision VPS (DigitalOcean/Hetzner/client's cloud) | 2 min |
| 2 | Support | Run deployment script: `./deploy.sh client-name client-domain.com` | 5 min |
| 3 | Script | Pulls Docker images, starts containers, runs DB migrations | 3 min |
| 4 | Script | Auto-generates SSL via Let's Encrypt | 1 min |
| 5 | Script | Creates admin account, sends credentials | Instant |
| 6 | Client/support | Point DNS: leads.clientsite.com → container IP | 5 min |
| 7 | Client | Log in, upload knowledge base, configure branding | 10 min |
| 8 | Automated | Knowledge base vectorised, concierge ready | 2-5 min |
| **Total** | | | **~30 min** |

### The Deployment Script

```bash
#!/bin/bash
# deploy.sh — one-command client deployment
# Usage: ./deploy.sh <client-name> <domain> [email]

CLIENT=$1
DOMAIN=$2
EMAIL=${3:-"support@leadengine.io"}

echo "Deploying LeadEngine for $CLIENT at $DOMAIN..."

# Generate secrets
DB_PASS=$(openssl rand -hex 16)
ADMIN_PASS=$(openssl rand -hex 8)
CLIENT_ID=$(openssl rand -hex 12)

# Create env file
cat > .env <<EOF
CLIENT_ID=$CLIENT_ID
CLIENT_NAME=$CLIENT
CLIENT_DOMAIN=$DOMAIN
DB_PASS=$DB_PASS
CLAUDE_API_KEY=${CLAUDE_API_KEY}
IPINFO_TOKEN=${IPINFO_TOKEN}
BRAND_COLOUR=#0B8C00
SMTP_HOST=smtp.resend.com
EOF

# Pull and start
docker compose pull
docker compose up -d

# Wait for DB
sleep 10

# Run migrations + seed
docker compose exec api npm run migrate
docker compose exec api npm run seed -- --admin-email=$EMAIL --admin-pass=$ADMIN_PASS

# SSL via Certbot
docker compose exec nginx certbot --nginx -d $DOMAIN --non-interactive --agree-tos -m $EMAIL

echo "========================================="
echo "  LeadEngine deployed for $CLIENT"
echo "  URL: https://$DOMAIN"
echo "  Admin: $EMAIL / $ADMIN_PASS"
echo "  Client ID: $CLIENT_ID"
echo "  Snippet: <script src='https://$DOMAIN/pixel.js'></script>"
echo "========================================="
```

**That's it.** One command. 5 minutes. Client is live.

---

## HOW TO SIMPLIFY FURTHER

### 1. Admin Super-Panel (For You)
A master dashboard where you manage ALL clients:

| Feature | Purpose |
|---------|---------|
| Client list | See all active clients, their plan, status |
| One-click deploy | Enter client name + domain → provisions automatically |
| Health monitoring | Green/red status per client container |
| Usage metrics | API calls, visitors tracked, leads captured per client |
| Billing integration | Stripe per client, auto-invoicing |
| Update all | Push new version to all containers with one click |
| Backup/restore | Automated daily backups, one-click restore |

### 2. Self-Service Onboarding
Client signs up on your website → auto-provisioned → snippet generated → guide walks them through installation. Zero support needed for 80% of clients.

### 3. Platform Plugins
Pre-built plugins that auto-install the snippet:
- **WordPress plugin** — install from WP admin, paste client ID, done
- **Shopify app** — install from Shopify app store, auto-configures
- **Wix app** — drag-drop the widget
- **Squarespace** — code injection in settings
- **Custom** — paste the `<script>` tag (works everywhere)

### 4. Terraform/Ansible for Container Clients
For scale: infrastructure-as-code templates that provision a VPS, deploy the stack, configure DNS, and set up monitoring — fully automated.

---

## WHAT COMPETITORS OFFER (Deployment-Wise)

### Chat/Concierge Platforms

| Platform | Hosting Model | Self-Hosted? | White-Label? | Price |
|----------|:---:|:---:|:---:|:---:|
| **Intercom** | SaaS only | No | No | $39-139/seat/mo |
| **Drift** | SaaS only | No | No | Custom (expensive) |
| **Crisp** | SaaS + self-hosted | Enterprise only | Enterprise | $25-95/mo |
| **Chatwoot** | SaaS + self-hosted | Yes (open source) | Yes | Free-$19/agent/mo |
| **Tawk.to** | SaaS only | No | Yes ($19/mo) | Free |
| **Tidio** | SaaS only | No | No | $29-59/mo |

### AI Chatbot Reseller Platforms

| Platform | Hosting Model | Self-Hosted? | White-Label? | Price |
|----------|:---:|:---:|:---:|:---:|
| **Stammer.ai** | SaaS | No | Yes | $49-497/mo |
| **Botsify** | SaaS | No | Yes | $49-149/mo |
| **BotSailor** | SaaS | No | Yes | $70-719/mo |
| **Voiceflow** | SaaS | No | Enterprise | Free-custom |
| **Chatbase** | SaaS | No | Yes ($399/mo) | $19-399/mo |
| **CustomGPT** | SaaS | No | Enterprise | $99-1,399/mo |

### Visitor Identification

| Platform | Hosting Model | Self-Hosted? | White-Label? | Price |
|----------|:---:|:---:|:---:|:---:|
| **RB2B** | SaaS only | No | Agency discount | $79-199/mo |
| **Leadfeeder** | SaaS only | No | No | $99-199/mo |
| **Clearbit** | SaaS only | No | No | Custom |
| **Snitcher** | SaaS only | No | White-label option | $39-299/mo |

### Key Insight
**Almost nobody offers true per-client container deployment.** Chatwoot is the closest (open source, Docker), but it's just chat — no AI concierge, no visitor identification, no funnel analytics, no lead routing.

**Your differentiator: a complete platform that can be deployed as a dedicated, isolated, branded container.** Nobody else does this with the full stack you're building.

---

## PROPERTY CONNECT INTEGRATION

LeadEngine runs as a feature WITHIN Property Connect London:

```
propertyconnect.london
├── /               → Marketing site (Chroma design system)
├── /platform       → Agent dashboard (Brainwave shell)
│   ├── /leads      → LeadEngine dashboard (embedded)
│   ├── /properties → Property management
│   ├── /analytics  → LeadEngine funnel analytics (embedded)
│   └── /concierge  → LeadEngine concierge config (embedded)
├── /search         → Public property search (has LeadEngine pixel)
└── /api            → Shared API
```

For Property Connect, LeadEngine isn't a separate product — it's a MODULE within the platform. The same codebase, just rendered inside the PCL dashboard shell instead of its own standalone dashboard.

For standalone LeadEngine clients (estate agents, ecommerce), it's the full standalone product with its own dashboard.

**Same code. Two presentation modes:**
1. Standalone: LeadEngine dashboard (its own Brainwave shell)
2. Embedded: LeadEngine components inside Property Connect shell

---

## PRICING STRUCTURE (Updated)

| Tier | Price | Hosting | What They Get |
|------|:---:|:---:|---------------|
| **Hosted** | £5,000/mo | Your servers, multi-tenant | Full platform, branded widget, dashboard, all features |
| **Dedicated** | £7,500/mo | Your servers, isolated container | Everything above + own container, custom domain, full data isolation |
| **Self-hosted** | £10,000 setup + £2,000/mo | Their servers | Docker package, deployment support, updates, your LLM API key included |
| **Enterprise** | Custom | Negotiable | On-premise, custom integrations, SLA, dedicated support |

All tiers include:
- Branded concierge widget
- Full dashboard access
- Knowledge base ingestion
- Visitor tracking + company ID
- Lead capture + scoring + routing
- Funnel analytics
- Email/Slack notifications
- Onboarding support

---

## DEPLOYMENT COMPLEXITY SUMMARY

| Aspect | Hosted | Container |
|--------|:---:|:---:|
| Client effort | Paste 1 script tag | Paste 1 script tag + DNS |
| Support effort | Create tenant (1 min) | Run deploy script (5 min) |
| Time to live | 15 minutes | 30 minutes |
| Ongoing maintenance | Zero (you manage) | Updates pushed via Docker pull |
| Scaling | Automatic | Manual (upgrade VPS) |
| Data isolation | Logical (tenant_id) | Physical (separate DB) |
| Custom domain | Subdomain of yours | Their own domain |
| Complexity for client | None | Minimal (DNS only) |

**Bottom line: it's not complex.** The deployment script handles everything. The client's only job is pasting a script tag (same as installing Google Analytics) and pointing a DNS record if they want a custom domain.
