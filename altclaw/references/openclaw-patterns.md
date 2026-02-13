# OpenClaw/Moltbot/Clawdbot Common Patterns

This reference document details common patterns found in OpenClaw/Moltbot/Clawdbot installations and their Claude Code equivalents.

## Configuration File Locations

### OpenClaw
- Main config: `~/.openclaw/config.yaml`
- API keys: `~/.openclaw/.env`
- Custom prompts: `~/.openclaw/prompts/`
- Scripts: `~/.openclaw/scripts/`

### Moltbot
- Main config: `~/.moltbot/settings.json`
- Credentials: `~/.moltbot/credentials.yaml`
- Workflows: `~/.moltbot/workflows/`
- Hooks: `~/.moltbot/hooks/`

### Clawdbot
- Config: `~/.clawdbot/config.toml`
- API settings: `~/.clawdbot/api.conf`
- Templates: `~/.clawdbot/templates/`
- Integrations: `~/.clawdbot/integrations/`

## Common Integration Patterns

### Pattern 1: GitHub Automation
**OpenClaw/Moltbot:**
```python
# Custom script using PyGithub
from github import Github
g = Github(token)
repo = g.get_repo("user/repo")
# Manual PR creation, issue management, etc.
```

**Claude Code Equivalent:**
- Built-in `gh` CLI tool via Bash
- Native GitHub integration
- No additional dependencies needed
- Better error handling and auth

**Migration:** Remove Python scripts, use native `gh` commands

---

### Pattern 2: Web Scraping
**OpenClaw/Moltbot:**
```python
import requests
from bs4 import BeautifulSoup
# Manual HTTP requests and parsing
```

**Claude Code Equivalent:**
- WebFetch tool (built-in)
- WebSearch tool (built-in)
- Automatic markdown conversion
- Prompt injection protection

**Migration:** Delete scraping scripts, use WebFetch/WebSearch

---

### Pattern 3: File Processing Loops
**OpenClaw/Moltbot:**
```python
for file in os.listdir(directory):
    content = open(file).read()
    result = api_call(content)
    write_output(result)
```

**Claude Code Equivalent:**
- Glob tool for finding files
- Read tool for content
- Edit/Write tools for output
- Single context across all files

**Migration:** Remove processing scripts, use native file tools

---

### Pattern 4: Multi-Step Workflows
**OpenClaw/Moltbot:**
```yaml
workflow:
  - step: fetch_data
  - step: process_data
  - step: generate_report
  - step: send_notification
```

**Claude Code Equivalent:**
- TodoWrite for workflow tracking
- Native tool orchestration
- Single coherent conversation
- Better error recovery

**Migration:** Convert YAML workflows to natural language instructions or Skills

---

### Pattern 5: MCP Server Proxies
**OpenClaw/Moltbot:**
```python
# Custom middleware to connect to services
class SlackProxy:
    def __init__(self, token):
        self.client = SlackClient(token)
    # Wrapper methods
```

**Claude Code Equivalent:**
- Direct MCP server integration
- Native credential management
- No proxy code needed
- Better security

**Migration:** Remove proxy code, install official MCP servers

---

### Pattern 6: Cost Tracking
**OpenClaw/Moltbot:**
```python
# Manual token counting and cost calculation
import tiktoken
tokens = len(tiktoken.encode(text))
cost = tokens * RATE_PER_1K / 1000
```

**Claude Code Equivalent:**
- Automatic usage tracking
- Built-in cost monitoring
- No manual calculation needed

**Migration:** Remove tracking code, use built-in metrics

---

### Pattern 7: Credential Management
**OpenClaw/Moltbot:**
```env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
```

**Claude Code Equivalent:**
- MCP server credential storage
- OS keychain integration
- Environment variable support
- Better security practices

**Migration:** Move credentials to MCP server configs, remove from .env files

---

## Cost Comparison Framework

### API Call Patterns
| Pattern | OpenClaw/Moltbot | Claude Code | Savings |
|---------|------------------|-------------|---------|
| Single file analysis | 1 API call | 0 API calls (local) | 100% |
| Multi-file project | N API calls | 1 conversation | ~90% |
| Iterative refinement | N API calls | 1 extended conversation | ~80% |
| GitHub operations | 1-3 API calls + GitHub API | 0 additional API calls | ~60% |
| Web research | 3-5 API calls | 1 API call (with caching) | ~70% |

### Cost Calculation Formula
```
OpenClaw Monthly Cost = (API calls/day × 30) × (avg_input_tokens × $0.003/1K + avg_output_tokens × $0.015/1K)
Claude Code Monthly Cost = Claude Pro subscription ($20) + (reduced API usage × rates)
```

## Security Audit Checklist

When analyzing installations, check for:

- [ ] Hardcoded API keys in scripts
- [ ] World-readable config files with credentials
- [ ] Overly broad file system permissions
- [ ] Unencrypted credential storage
- [ ] API keys in version control
- [ ] Shared credentials across users
- [ ] No rate limiting or quota management
- [ ] Exposed ports or network services
- [ ] Outdated dependencies with vulnerabilities
- [ ] No audit logging

## Migration Complexity Matrix

| Feature | Complexity | Time Estimate | Notes |
|---------|-----------|---------------|-------|
| GitHub automation | Low | 1-2 hours | Direct `gh` replacement |
| File processing | Low | 1-2 hours | Native tools |
| Web scraping | Low | 30min-1hr | WebFetch/WebSearch |
| Simple workflows | Medium | 2-4 hours | Convert to Skills |
| MCP integrations | Medium | 1-3 hours | Install MCP servers |
| Complex state management | High | 1-2 days | Redesign needed |
| Real-time monitoring | High | 2-3 days | May need external tools |
| Custom ML models | High | N/A | Cannot migrate |

## Quick Win Checklist

Prioritize these for immediate value:

1. **Replace hardcoded API keys** → MCP credential management
2. **Remove web scraping scripts** → WebFetch/WebSearch
3. **Consolidate file processing** → Native file tools + extended context
4. **Simplify GitHub automation** → Built-in `gh` CLI
5. **Eliminate proxy middleware** → Direct MCP server connections
6. **Convert simple workflows** → Natural language or simple Skills

## Red Flags

Stop and consult user if you find:

- ⚠️ Production systems with no backup migration path
- ⚠️ Highly customized ML models (cannot migrate)
- ⚠️ Real-time requirements with <100ms latency needs
- ⚠️ Integration with proprietary/internal APIs not available as MCP
- ⚠️ Compliance requirements requiring specific infrastructure
- ⚠️ Team workflows requiring simultaneous multi-user access

## Resources

- Claude Code Documentation: https://docs.anthropic.com/claude/docs
- MCP Server Registry: https://github.com/modelcontextprotocol/servers
- Claude API Pricing: https://www.anthropic.com/pricing
- Migration examples: See `/examples/` directory
