# SESSION START PROTOCOL

## On Session Init

### 1. Load Context
- Read MASTER_CONTEXT.md from 00_SYSTEM_ROOT
- Check STATE_SNAPSHOTS for latest state
- Identify active goals

### 2. Determine Intent
- What is the user trying to accomplish?
- Is this continuation or new work?
- Which domain/project does this relate to?

### 3. Route Session
- Apply SESSION_ROUTER.md logic
- Create session log in appropriate location
- Load relevant domain context if needed

### 4. Set Up Workspace
- Identify which agents may be needed
- Prepare relevant templates
- Note any blockers or dependencies

## Context Injection Order
1. System context (MASTER_CONTEXT.md)
2. Current state (latest STATE_SNAPSHOT)
3. Domain context (if domain-specific work)
4. Project context (if project work)
5. Goal context (if goal-related)
