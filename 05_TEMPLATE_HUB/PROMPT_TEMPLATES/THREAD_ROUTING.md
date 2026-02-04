# THREAD SUMMARY + ROUTING PROMPT

Paste this into any thread you want to summarize and route:

---

## PROMPT (COPY THIS)

```
I need a summary of this conversation for routing to my Enterprise_OS folder structure.

Please provide:

1. **THREAD TITLE** (descriptive, max 10 words)

2. **PRIMARY DOMAIN** (pick ONE from this list):
   - PIL_01_AVATARS
   - PIL_02_BRANDING
   - PIL_03_COPY
   - PIL_04_CONTENT
   - PIL_05_GRAPHICS
   - PIL_06_VIDEO
   - PIL_07_UI_LIBRARY
   - PIL_08_KNOWLEDGE_INGESTION
   - PIL_09_ROLES_SKILLS
   - PIL_10_WORKING_PRACTICES
   - PIL_11_BUILD_STORY
   - PIL_12_KEYWORDS
   - PIL_13_SEO
   - PIL_14_NAVIGATION
   - PIL_15_ENTERPRISE_OS
   - PIL_16_CONTENT_GENERATION
   - PIL_17_RAG_SYSTEM
   - PIL_18_AGENT_FRAMEWORK
   - PIL_19_PROPERTY
   - PIL_20_FITNESS
   - PIL_21_MARKET_RESEARCH
   - PIL_22_VOICE_TRAINING
   - PIL_23_DOG_PLATFORM

3. **SECONDARY DOMAINS** (if any, max 2)

4. **SUMMARY** (3-5 bullets of what was covered)

5. **KEY OUTPUTS** (any artifacts, frameworks, decisions, or reusable content created)

6. **ROUTING RECOMMENDATION**:
   - Thread file → [PILLAR]/01_threads/
   - Artifacts → [PILLAR]/02_artifacts/ or specific subfolder

Format as a single block I can copy into my routing log.
```

---

## ROUTING LOG TEMPLATE

Use this to track where everything goes:

```
# THREAD ROUTING LOG
Last Updated: 2026-02-02

## ROUTED THREADS

| Date | Thread Title | Primary Pillar | Routed To | Artifacts |
|------|--------------|----------------|-----------|-----------|
| 2026-02-02 | [title] | PIL_XX_NAME | PIL_XX/01_threads/ | Y/N |

## PENDING ROUTING

| Thread | Status | Notes |
|--------|--------|-------|
| | | |

## ROUTING DECISIONS

### [Thread Title]
- **Primary:** PIL_XX
- **Secondary:** PIL_YY, PIL_ZZ
- **Summary:** 
- **Key Outputs:**
- **Thread → ** PIL_XX/01_threads/[filename].md
- **Artifacts →** PIL_XX/02_artifacts/

---
```

---

## YOUR EXISTING FOLDER PATHS

These need to be moved to V7 pillars:

### ALREADY HAVE 01_threads + 02_artifacts:
```
C:\Users\under\Downloads\UI Component System\01_threads          → PIL_07_UI_LIBRARY
C:\Users\under\Downloads\UI Component System\02_artifacts        → PIL_07_UI_LIBRARY
C:\Users\under\Downloads\Video Creation System\01_threads        → PIL_06_VIDEO
C:\Users\under\Downloads\Video Creation System\02_artifacts      → PIL_06_VIDEO
C:\Users\under\Downloads\Copywriting System\01_threads           → PIL_03_COPY
C:\Users\under\Downloads\Copywriting System\02_artifacts         → PIL_03_COPY
C:\Users\under\Downloads\Copywriting System\Copy Asset Artifacts → PIL_03_COPY/02_artifacts/
C:\Users\under\Downloads\Keyword Structure\01_threads            → PIL_12_KEYWORDS
C:\Users\under\Downloads\Keyword Structure\02_artifacts          → PIL_12_KEYWORDS
C:\Users\under\Downloads\Keyword Research\01_threads             → PIL_12_KEYWORDS
C:\Users\under\Downloads\Keyword Research\02_artifacts           → PIL_12_KEYWORDS
C:\Users\under\Downloads\Market Research System\01_threads       → PIL_21_MARKET_RESEARCH
C:\Users\under\Downloads\Market Research System\02_artifacts     → PIL_21_MARKET_RESEARCH
C:\Users\under\Downloads\Fitness App\01_threads                  → PIL_20_FITNESS
C:\Users\under\Downloads\Fitness App\02_artifacts                → PIL_20_FITNESS
```

### NEED TO ADD 01_threads + 02_artifacts:
```
C:\Users\under\Downloads\Navigation System\01_threads            → PIL_14_NAVIGATION
C:\Users\under\Downloads\Navigation System\02_artifacts          → PIL_14_NAVIGATION
C:\Users\under\Downloads\Knowledge Ingestion\01_threads          → PIL_08_KNOWLEDGE_INGESTION
C:\Users\under\Downloads\Knowledge Ingestion\02_artifacts        → PIL_08_KNOWLEDGE_INGESTION
C:\Users\under\Downloads\Roles and Skills System\01_threads      → PIL_09_ROLES_SKILLS
C:\Users\under\Downloads\Roles and Skills System\02_artifacts    → PIL_09_ROLES_SKILLS
C:\Users\under\Downloads\Graphic design System\01_threads        → PIL_05_GRAPHICS
C:\Users\under\Downloads\Graphic design System\02_artifacts      → PIL_05_GRAPHICS
C:\Users\under\Downloads\Content System\01_threads               → PIL_04_CONTENT
C:\Users\under\Downloads\Content System\02_artifacts             → PIL_04_CONTENT
C:\Users\under\Downloads\Build Story\01_threads                  → PIL_11_BUILD_STORY
C:\Users\under\Downloads\Build Story\02_artifacts                → PIL_11_BUILD_STORY
C:\Users\under\Downloads\Work Practices\01_threads               → PIL_10_WORKING_PRACTICES
C:\Users\under\Downloads\Work Practices\02_artifacts             → PIL_10_WORKING_PRACTICES
C:\Users\under\Downloads\Voice training System\01_threads        → PIL_22_VOICE_TRAINING
C:\Users\under\Downloads\Voice training System\02_artifacts      → PIL_22_VOICE_TRAINING
C:\Users\under\Downloads\Enterprise_OS\01_threads                → PIL_15_ENTERPRISE_OS
C:\Users\under\Downloads\Enterprise_OS\02_artifacts              → PIL_15_ENTERPRISE_OS
C:\Users\under\Downloads\Branding System\01_threads              → PIL_02_BRANDING
C:\Users\under\Downloads\Branding System\02_artifacts            → PIL_02_BRANDING
```

---

## WORKFLOW

1. **Open a thread** you want to route
2. **Paste the prompt** above
3. **Copy the response** into your routing log
4. **Export/download the thread** as .md
5. **Move to the recommended pillar's 01_threads/ folder**
6. **Move any artifacts** to 02_artifacts/ or specific subfolder

Once you have all summaries, we consolidate the routing log and batch-move everything.
