# PRD 8: Property Data Services (B2B)

**Version:** 2.0  
**Date:** 2025-11-04  
**Priority:** HIGH  
**Note:** B2B companion to Property Connect London (PRD 1)

---

## Vision

Create a comprehensive property data and intelligence platform for London property professionals, providing market analytics, deal flow, investment scoring, and API access to power their businesses with data-driven decision-making.

---

## Target Market (B2B Focus)

### Primary Customers
- **Estate Agents & Property Managers**
- **Property Investors** (individual & funds)
- **Property Developers**
- **Mortgage Brokers & Financial Advisors**
- **Property Lawyers & Conveyancers**
- **Surveyors & Valuers**
- **Letting Agents & Landlords**
- **PropTech Companies**

### Use Cases by Customer Type

**Estate Agents:**
- Pricing optimization
- Market analysis for clients
- Listing intelligence
- Competitor tracking
- Area performance data

**Property Investors:**
- Investment opportunity identification
- Yield analysis by area
- Market trend forecasting
- Deal scoring
- Portfolio performance tracking

**Developers:**
- Site selection
- Viability analysis
- Market demand assessment
- Planning intelligence
- Comparable sales data

**Mortgage Brokers:**
- Market data for client presentations
- Affordability analysis
- Investment property viability
- Market trends for advice

**Letting Agents:**
- Rental pricing optimization
- Yield benchmarking
- Tenant demand analysis
- Void period predictions

---

## Core Data Products

### 1. Market Intelligence Dashboard

**Real-Time Market Data:**
- **Price Index:** 
  - London-wide, borough-level, area-level
  - Updated weekly
  - Historical trends (10+ years)
  - Price per square foot
  - Property type breakdowns

- **Transaction Data:**
  - Sales volumes by area
  - Days on market analysis
  - Sale vs asking price ratios
  - Seasonal patterns
  - Buyer demographics

- **Rental Market:**
  - Rental price index
  - Yield analysis by area
  - Tenant demand indicators
  - Void period averages
  - Supply/demand dynamics

- **Supply Dynamics:**
  - New listings tracker
  - Stock levels by area
  - Planning permissions granted
  - Development pipeline
  - Construction starts

**Predictive Analytics:**
- Price trend forecasts (3, 6, 12 months)
- Hot spot identification (emerging areas)
- Gentrification indicators
- Investment opportunity scores
- Risk assessment by area

**Custom Alerts:**
- Price movement alerts
- New listing notifications
- Market condition changes
- Planning permission updates
- Competition activity

### 2. Deal Flow & Opportunity Finder

**Off-Market Opportunities:**
- Distressed properties
- Probate sales
- Motivated sellers (data signals)
- Pre-market listings
- Portfolio sales
- Development sites

**Auction Intelligence:**
- Upcoming auction listings
- Historical auction results
- Success rate analysis
- Valuation estimates
- Comparable sales

**Investment Scoring:**
- Automated investment analysis
- Yield calculations
- Capital growth projections
- Risk scoring
- ROI estimates
- Rental demand assessment

**Deal Alerts:**
- Custom criteria matching
- Real-time notifications
- Email/SMS alerts
- API webhooks

### 3. Area Intelligence Reports

**Comprehensive Area Profiles:**
- **Market Data:**
  - Price trends
  - Transaction volumes
  - Rental yields
  - Supply levels
  - Buyer/tenant demographics

- **Infrastructure:**
  - Transport links (tube, rail, bus)
  - Planned improvements
  - Crossrail/HS2 impact
  - Road developments
  - Cycling infrastructure

- **Amenities:**
  - Schools (ratings, catchments)
  - Healthcare (hospitals, GPs)
  - Shopping & dining
  - Parks & recreation
  - Cultural venues

- **Demographics:**
  - Population trends
  - Age distribution
  - Income levels
  - Employment sectors
  - Family composition

- **Crime & Safety:**
  - Crime rate trends
  - Type of offenses
  - Police presence
  - Safety scores

- **Planning:**
  - Recent approvals
  - Pipeline developments
  - Regeneration plans
  - Borough policies

**Custom Report Builder:**
- Select specific data points
- White-label reports
- Client-ready formatting
- Automated generation
- Scheduled delivery

### 4. Pricing Intelligence

**Automated Valuation Model (AVM):**
- Property-specific valuations
- Comparable sales analysis
- Confidence intervals
- Rental value estimates
- Price prediction ranges

**Pricing Recommendations:**
- Optimal listing prices
- Expected sale timeframe
- Discount scenarios
- Seasonal adjustments
- Competition analysis

**Market Position Analysis:**
- How property compares to area average
- Price per square foot benchmarking
- Feature value attribution
- Renovation potential value

### 5. Competitor Intelligence

**Agent Performance Tracking:**
- Market share by area
- Average sale prices
- Time on market
- Success rates
- Commission rates
- Marketing spend estimates

**Listing Analysis:**
- Active listings by competitor
- Pricing strategies
- Photography quality scores
- Description analysis
- Portal presence

**Market Share Dashboard:**
- Your position vs competitors
- Market concentration
- Opportunity gaps
- Performance benchmarks

### 6. Investment Analysis Tools

**ROI Calculator:**
- Purchase costs breakdown
- Ongoing costs (management, maintenance)
- Rental income projections
- Capital growth estimates
- Cash flow analysis
- Tax implications
- Total return calculations

**Portfolio Analyzer:**
- Multi-property performance
- Diversification analysis
- Risk assessment
- Rebalancing suggestions
- Exit strategy recommendations

**Scenario Planning:**
- What-if analysis
- Sensitivity to market changes
- Stress testing
- Leverage impact
- Exit timing optimization

### 7. Property Data API

**REST API Access:**
- **Endpoints:**
  - Property search
  - Market data retrieval
  - Transaction history
  - Rental data
  - Area statistics
  - Planning data
  - Comparable sales
  - Valuation estimates

- **Rate Limits:**
  - Tiered by subscription
  - Webhook support
  - Bulk data downloads
  - Real-time data streams

- **Documentation:**
  - Comprehensive API docs
  - Code examples (Python, JavaScript, etc.)
  - Swagger/OpenAPI spec
  - Postman collection
  - SDK libraries

**Use Cases:**
- Power internal systems
- Website integrations
- Mobile app backends
- Data warehousing
- Custom analytics
- Third-party integrations

### 8. Custom Data Solutions

**White-Label Platform:**
- Branded dashboard
- Custom domain
- Logo and colors
- Client login portals
- Report customization

**Data Feeds:**
- FTP/SFTP delivery
- S3 bucket sync
- Database replication
- Custom formats (CSV, JSON, XML)
- Scheduled updates

**Enterprise Solutions:**
- Custom data models
- Bespoke analytics
- Integration consulting
- Dedicated data engineer
- SLA guarantees

---

## Data Sources & Methodology

### Data Collection

**Primary Sources:**
- **Land Registry:** Price Paid Data (PPD), Title data
- **Rightmove/Zoopla:** Listing data (via partnerships/scraping)
- **Energy Performance Certificates (EPC):** Size, efficiency ratings
- **Planning Authorities:** Planning applications and decisions
- **ONS:** Census data, demographics
- **Transport for London:** Transport data
- **Ofsted:** School ratings
- **Police.uk:** Crime statistics

**Secondary Sources:**
- Estate agent APIs (partnerships)
- Auction houses (data partnerships)
- Mortgage lenders (market data)
- Property portals (comparison sites)
- Social media signals (gentrification indicators)
- Web scraping (legal, compliant)

**Proprietary Data:**
- PCL reader surveys
- Pro network insights
- Investment tracking
- Market sentiment indices

### Data Processing

**Quality Assurance:**
- Automated validation
- Outlier detection
- Cross-source verification
- Regular audits
- User reporting of errors

**Data Enrichment:**
- ML-based property feature extraction
- Image analysis (property photos)
- NLP on descriptions
- Geospatial analysis
- Temporal pattern recognition

**Data Updates:**
- Real-time where possible (listings, alerts)
- Daily updates (prices, new data)
- Weekly aggregations (market indices)
- Monthly reports (comprehensive analysis)

---

## Technical Architecture

### Data Infrastructure

**Data Pipeline:**
```
Collection → Validation → Enrichment → Storage → API/Dashboard
```

**Tech Stack:**
- **Data Collection:** Python (Scrapy, Selenium), API integrations
- **Data Processing:** Apache Spark, Pandas, DBT
- **Data Storage:** 
  - **Relational:** PostgreSQL (structured data)
  - **Time-Series:** TimescaleDB (price data, trends)
  - **Search:** Elasticsearch (property search)
  - **Cache:** Redis (API responses)
- **Data Warehouse:** Snowflake or BigQuery
- **ETL Orchestration:** Airflow
- **API:** FastAPI (Python) or Express (Node.js)
- **Frontend:** Next.js, React, Recharts/Plotly (visualizations)

### Geospatial Stack

- **Database:** PostGIS (geospatial queries)
- **Mapping:** Mapbox or Google Maps
- **Analysis:** GeoPandas, Turf.js
- **Visualization:** Deck.gl, Leaflet

### Machine Learning

**Models:**
- **AVM:** XGBoost, Random Forest for valuations
- **Forecasting:** ARIMA, Prophet for price predictions
- **NLP:** BERT-based models for text analysis
- **Image Analysis:** CNN for property photos
- **Recommendation:** Collaborative filtering for opportunities

**MLOps:**
- **Training:** Python (scikit-learn, TensorFlow)
- **Deployment:** Docker, Kubernetes
- **Monitoring:** MLflow, Weights & Biases
- **Feature Store:** Feast or Tecton

---

## Database Schema

```sql
-- Core Property Data
properties (address, type, features, coordinates, etc.)
property_history (sales, rentals over time)
property_features (bedrooms, bathrooms, sq_ft, etc.)
property_images

-- Market Data
price_index (area, date, value)
transactions (sale data)
listings (active and historical)
rental_data

-- Geographic
areas (boroughs, neighborhoods, postcodes)
area_boundaries (geometries)
transport_links
amenities (schools, hospitals, shops, etc.)
poi (points of interest)

-- Planning & Development
planning_applications
development_pipeline
regeneration_projects

-- Demographics & Statistics
census_data
crime_statistics
school_ratings
employment_data

-- Comparative & Analysis
comparable_sales
area_statistics
market_forecasts
investment_scores

-- Users & Access
organizations
users
api_keys
usage_logs

-- Alerts & Notifications
alert_rules
triggered_alerts
webhooks
```

---

## User Experience

### Dashboard Interface

**Home/Overview:**
- Key market metrics (London-wide)
- Recent alerts
- Saved searches
- Quick actions

**Property Search:**
- Map-based or list view
- Advanced filters (price, type, area, features)
- Sort and compare
- Save searches
- Export results

**Area Explorer:**
- Interactive map
- Layer toggles (price, yield, supply, demographics, etc.)
- Click for area deep-dive
- Compare areas side-by-side

**Deal Flow:**
- Opportunity feed
- Investment scoring
- Deal details
- Comparable analysis
- Add to watchlist

**Reports:**
- Pre-built report templates
- Custom report builder
- Schedule delivery
- White-label output

**API Dashboard:**
- API key management
- Usage monitoring
- Rate limit status
- Documentation access
- Test playground

---

## Pricing Model

### Subscription Tiers

**Starter (£99/mo):**
- 1 user
- Market intelligence dashboard (basic)
- Area reports (10/month)
- Deal alerts (basic criteria)
- Email support

**Professional (£299/mo):**
- 3 users
- Full market intelligence
- Unlimited area reports
- Advanced deal alerts
- Pricing intelligence
- Competitor tracking
- 1,000 API calls/month
- Phone support

**Agency/Team (£999/mo):**
- 10 users
- Everything in Professional
- White-label reports
- Custom branding
- Investment analysis tools
- Portfolio tracking
- 10,000 API calls/month
- Dedicated support
- Onboarding & training

**Enterprise (£5,000+/mo):**
- Unlimited users
- Custom data solutions
- Unlimited API access
- Data feeds
- Bespoke analytics
- Priority data updates
- Dedicated account manager
- SLA guarantees
- Custom integrations

### Add-Ons
- Additional API calls (£50/10,000)
- Historical data access (£200/month)
- White-label platform (£500/month)
- Custom data projects (£2,000+)
- Training sessions (£500/session)

---

## Go-to-Market Strategy

### Phase 1: Foundation (Months 1-3)
- Establish core data pipelines
- Build MVP dashboard
- Launch with 10 beta customers (free/discounted)
- Validate data quality and features
- Establish partnerships with 3-5 data providers

### Phase 2: Product Launch (Months 4-6)
- Public launch (Starter & Professional tiers)
- Content marketing (data reports, insights)
- Direct sales to estate agents & investors
- Industry conference presence
- Target: 50 paying customers

### Phase 3: Scale (Months 7-12)
- Launch Agency/Enterprise tiers
- API marketplace presence
- Strategic partnerships (PropTech integrations)
- Expand sales team
- Target: 500 customers, £500K ARR

### Phase 4: Market Leader (Year 2)
- Advanced analytics features
- Expand beyond London (UK-wide)
- International markets
- White-label partnerships
- Target: £5M ARR

---

## Competitive Analysis

### Existing Players

**Hometrack:**
- **Strength:** Established, comprehensive AVM
- **Weakness:** Legacy UI, expensive
- **Our Advantage:** Modern interface, better pricing, deal flow features

**PropertyData.co.uk:**
- **Strength:** Good API, established
- **Weakness:** Limited analytics, no deal flow
- **Our Advantage:** Comprehensive analytics, opportunity finder, community (PCL)

**Nimbus Maps:**
- **Strength:** Beautiful visualization
- **Weakness:** Limited to investors, narrow scope
- **Our Advantage:** Broader audience, more data types, API access

**Cotality:**
- **Strength:** Comprehensive platform
- **Weakness:** Expensive, enterprise-only
- **Our Advantage:** Accessible pricing, better UX, community integration

---

## Revenue Projections

### Year 1 Targets
- **Customers:** 500
- **ARPU:** £150/month
- **ARR:** £900K
- **Churn:** <10% monthly

### Year 3 Targets
- **Customers:** 5,000
- **ARPU:** £200/month
- **ARR:** £12M
- **Churn:** <5% monthly

### Revenue Mix
- Subscriptions: 70%
- API usage: 20%
- Custom projects: 10%

---

## Key Metrics

### Data Quality Metrics
- Data freshness (time since last update)
- Coverage (% of London properties)
- Accuracy (AVM error rate)
- Uptime (API availability)

### Product Metrics
- Daily active users
- Searches per user
- Reports generated
- API calls
- Feature adoption

### Business Metrics
- MRR/ARR growth
- Customer count by tier
- Churn rate
- NRR (Net Revenue Retention)
- CAC
- LTV:CAC ratio

---

## Integration with PCL Ecosystem

### Synergies with Property Connect London (PRD 1)

**Cross-Promotion:**
- PCL content → Data service CTAs
- Data service → PCL community/content
- Unified brand presence

**Data Sharing:**
- PCL user insights → Data product improvements
- Data insights → PCL editorial content
- Community sentiment → Market intelligence

**Bundled Offerings:**
- PCL Premium + Data Starter bundle
- Agency customers get PCL advertising
- Data Enterprise includes PCL magazine ads

**Product Integration:**
- PCL articles cite Data platform insights
- Data platform surfaces relevant PCL content
- Unified login/account

---

## Dependencies

### Data Provider Relationships
- Land Registry (official access)
- Rightmove/Zoopla (partnerships or scraping)
- EPC database (government API)
- Planning authorities (APIs/scraping)
- Transport for London (API)

### Internal Dependencies
- **Property Platform (PRD 1):** Content and community
- **Database:** PostgreSQL infrastructure
- **Agent OS:** Workflow orchestration
- **Copy Platform:** Marketing copy
- **Branding Platform:** Visual identity

### External Dependencies
- Cloud infrastructure (AWS/GCP)
- Mapping services (Mapbox, Google Maps)
- Payment processing
- ML/AI infrastructure

---

## Success Criteria

### Month 6
- Core data pipelines operational
- MVP dashboard launched
- 50 paying customers
- £50K ARR
- 95%+ data accuracy

### Month 12
- 500 customers
- £900K ARR
- API launched
- 98%+ uptime
- <10% churn

### Year 2
- 2,000 customers
- £4M ARR
- Market leader recognition
- Strategic partnerships
- Profitable

---

## Risk Mitigation

### Data Access Risks
- **Risk:** Lose access to key data sources
- **Mitigation:** Multiple redundant sources, partnerships, legal compliance

### Competitive Risks
- **Risk:** Established players improve products
- **Mitigation:** Faster innovation, better UX, community advantage (PCL)

### Regulatory Risks
- **Risk:** Data privacy regulations tighten
- **Mitigation:** GDPR compliance, data minimization, transparency

### Customer Concentration Risk
- **Risk:** Over-reliance on few large customers
- **Mitigation:** Diverse customer base across segments and tiers

---

## Next Steps (Priority Order)

1. **Data Partnerships:** Establish agreements with Land Registry, portals, etc.
2. **Data Pipeline:** Build ingestion and processing infrastructure
3. **Core Dashboard:** MVP with market intelligence and area reports
4. **Beta Launch:** Recruit 10 beta customers and iterate
5. **Sales & Marketing:** Hire sales rep, create marketing materials
6. **API Development:** Build and document API
7. **Scale:** Expand features and customer base

---

**Status:** Data partnership phase - Critical path to launch
**Owner:** [Your Name]
**Last Updated:** 2025-11-04

---

## Appendix: Data Provider Research

### Providers to Analyze (from user request)

**1. Houseful.co.uk**
- **Focus:** Property data for professionals
- **Services:** Market insights, property reports, data feeds
- **Analysis Needed:** Pricing, data coverage, API capabilities

**2. Hometrack.com**
- **Focus:** AVM and market analytics
- **Services:** Valuations, indices, risk scoring
- **Analysis Needed:** AVM methodology, accuracy claims, pricing

**3. UK Data Services**
- **Focus:** Property data extraction
- **Services:** Custom data extracts, APIs
- **Analysis Needed:** Data sources, coverage, formats

**4. TwentyEA.co.uk & TwentyCI**
- **Focus:** Property intelligence
- **Services:** Domus database, market reports, mover data
- **Analysis Needed:** Unique data points, depth of coverage

**5. Sprift.com**
- **Focus:** [Research needed]
- **Analysis Needed:** Services offered, target market

**6. Nestdata.co.uk**
- **Focus:** Property data API
- **Services:** API access, data feeds
- **Analysis Needed:** API capabilities, pricing, data freshness

**7. Cotality.com**
- **Focus:** Commercial property intelligence
- **Services:** Comprehensive platform for commercial sector
- **Analysis Needed:** Feature set, pricing, UX quality

**8. PropertyData.co.uk**
- **Focus:** Investment property data
- **Services:** API, dashboards, area analysis
- **Analysis Needed:** API pricing, coverage, investor focus

**9. Nimbus Maps**
- **Focus:** Property investment mapping
- **Services:** Visual analytics, investment scores
- **Analysis Needed:** Unique features, pricing, target users

**10. Adema.ai**
- **Focus:** AI-powered property intelligence
- **Services:** [Research needed - appears to be AI/ML focused]
- **Analysis Needed:** AI capabilities, differentiation

### Research Action Items
1. Sign up for free trials/demos of each platform
2. Document feature sets in comparison matrix
3. Analyze pricing models
4. Assess data quality and coverage
5. Identify gaps we can fill
6. Determine partnership vs build vs buy decisions
7. Map our differentiation strategy

---

**Note:** This PRD is designed to be implemented in parallel with Property Connect London (PRD 1) as they form a unified ecosystem serving both consumers and professionals in the London property market.
