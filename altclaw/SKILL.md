---
name: altclaw
description: Analyzes OpenClaw, Moltbot, and Clawdbot installations to identify opportunities for migration to Claude Code. Use when user asks to "analyze OpenClaw", "check Moltbot performance", "audit Clawdbot", "compare to Claude Code", or wants to optimize their AI automation workflows.
---

# AltClaw - Claude Code Migration Analyzer

AltClaw scans and analyzes existing OpenClaw/Moltbot/Clawdbot installations to identify opportunities for improved performance, cost-effectiveness, and safety through migration to Claude Code.

## Instructions

When activated, follow this workflow:

### 1. Discovery Phase
- Ask user for the installation location(s) of OpenClaw/Moltbot/Clawdbot
- Identify which variant(s) they're running
- Locate configuration files, typically in:
  - `~/.openclaw/`
  - `~/.moltbot/`
  - `~/.clawdbot/`
  - Project-specific `.env` files

### 2. Analysis Phase
Scan and document the following:

**Configuration Analysis:**
- Read all config files (YAML, JSON, .env)
- Identify API keys, model configurations, rate limits
- Document current model usage (GPT-4, Claude API via OpenClaw, etc.)
- Map all MCP servers or integrations

**Workflow Analysis:**
- Examine Python scripts and automation code
- Identify repeated tasks and patterns
- Document custom prompts and templates
- Note any scheduled or triggered workflows

**Resource Analysis:**
- Calculate estimated API costs based on usage patterns
- Identify redundant or inefficient operations
- Check for security concerns (hardcoded keys, overly broad permissions)
- Note resource-intensive operations

### 3. Comparison & Recommendation Phase
Generate a detailed report with:

**Direct Equivalents:**
- MCP servers available in Claude Code that replace OpenClaw integrations
- Native Claude Code features that eliminate custom Python scripts
- Built-in tools that replace manual implementations

**Improvement Opportunities:**
- Cost savings from using Claude Code's native capabilities vs API calls
- Performance improvements from local execution
- Security enhancements from better credential management
- Workflow simplification by removing unnecessary middleware

**Migration Path:**
- Step-by-step migration plan prioritized by impact/effort
- Identify quick wins (easy migrations with high value)
- Flag complex migrations requiring careful planning
- List any functionality gaps where OpenClaw/Moltbot still needed

### 4. Output Format
Create a structured markdown report including:

```markdown
# AltClaw Analysis Report
Generated: [timestamp]

## Executive Summary
- Current setup: [brief overview]
- Estimated monthly cost: $X
- Projected Claude Code cost: $Y (Z% savings)
- Migration complexity: [Low/Medium/High]

## Current Configuration
[Document what was found]

## Migration Opportunities

### High Priority (Quick Wins)
1. [Opportunity]: [Description]
   - Current: [how it's done now]
   - Claude Code alternative: [specific tool/feature]
   - Expected benefit: [cost/performance/security improvement]

### Medium Priority
[Similar format]

### Low Priority / Advanced
[Similar format]

## Functionality Gaps
[Things Claude Code cannot currently do that OpenClaw/Moltbot does]

## Recommended Migration Plan
1. Phase 1: [Quick wins - Week 1]
2. Phase 2: [Core workflows - Weeks 2-3]
3. Phase 3: [Advanced features - Week 4+]

## Cost-Benefit Analysis
[Detailed breakdown]

## Security Improvements
[Specific security enhancements from migration]

## Next Steps
[Actionable recommendations]
```

### 5. Follow-up Actions
- Offer to help implement any recommended migrations
- Provide specific Claude Code configuration examples
- Suggest relevant MCP servers or skills to install

## Key Principles

- **Be thorough but focused**: Don't analyze every file, focus on configuration and key workflows
- **Be honest about gaps**: If OpenClaw does something Claude Code can't, say so clearly
- **Prioritize safety**: Flag any security concerns immediately
- **Calculate real costs**: Use actual API pricing and usage patterns
- **Provide actionable recommendations**: Every suggestion should have clear next steps

## Common Patterns to Look For

1. **Repetitive API calls** → Claude Code's extended context and caching
2. **Custom GitHub automation** → Native `gh` CLI integration
3. **Web scraping scripts** → Built-in web browsing capabilities
4. **File processing loops** → Direct file tool usage
5. **Multiple model orchestration** → Single Claude interface with tool use
6. **Credential management hacks** → Proper MCP server credential handling
7. **Custom logging/monitoring** → Built-in conversation persistence

## Error Handling

- If config files are inaccessible, ask user to provide them
- If unfamiliar OpenClaw/Moltbot variant found, ask for documentation
- If missing permissions, request sudo/access as needed
- If migration path unclear, present options and ask user preference
