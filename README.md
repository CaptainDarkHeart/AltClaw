# AltClaw

**Analyze your OpenClaw/Moltbot/Clawdbot setup and discover better alternatives with Claude Code**

AltClaw is a Claude Code skill that scans existing OpenClaw, Moltbot, and Clawdbot installations to identify opportunities for improved performance, cost-effectiveness, and security through migration to Claude Code.

## What It Does

AltClaw helps you:

- 🔍 **Discover** OpenClaw/Moltbot/Clawdbot installations on your system
- 📊 **Analyze** configurations, workflows, and resource usage
- 💰 **Calculate** cost savings from migrating to Claude Code
- 🔒 **Identify** security vulnerabilities and improvement opportunities
- 🗺️ **Generate** step-by-step migration plans with prioritized recommendations
- ⚡ **Recommend** Claude Code features, MCP servers, and tools as direct replacements

## Why Migrate to Claude Code?

| Feature | OpenClaw/Moltbot | Claude Code |
|---------|------------------|-------------|
| **Cost** | Pay-per-API-call | Flat monthly rate + reduced API usage |
| **Integration** | Custom Python scripts | Native tools + MCP servers |
| **Security** | Manual credential management | OS keychain + MCP credential storage |
| **Context** | Limited, multiple API calls | Extended context, single conversation |
| **Maintenance** | Update dependencies, scripts | Automatic updates |
| **Performance** | Network latency per call | Local execution + caching |

## Installation

### For Claude.ai (Web)

1. Download or clone this repository
2. Zip the `altclaw/` folder
3. In Claude.ai, go to **Settings > Capabilities > Skills**
4. Click **Upload skill** and select `altclaw.zip`

### For Claude Code (CLI)

1. Clone this repository:
   ```bash
   git clone https://github.com/CaptainDarkHeart/AltClaw.git
   cd AltClaw
   ```

2. Link the skill to your skills directory:
   ```bash
   ln -s "$(pwd)/altclaw" ~/.claude/skills/altclaw
   ```

3. Restart Claude Code or reload skills

## Usage

### Quick Start

Simply ask Claude to analyze your setup:

```
Analyze my OpenClaw installation
```

```
Check if I can migrate from Moltbot to Claude Code
```

```
Audit my Clawdbot configuration and recommend improvements
```

### What AltClaw Looks For

- **Configuration files** in `~/.openclaw/`, `~/.moltbot/`, `~/.clawdbot/`
- **Python scripts** and automation workflows
- **API usage patterns** and cost calculations
- **MCP integrations** and service connections
- **Security issues** like hardcoded keys, wrong permissions
- **Redundant operations** that Claude Code handles natively

### Sample Output

AltClaw generates a comprehensive report including:

- Executive summary with cost projections
- Current configuration analysis
- Migration opportunities (High/Medium/Low priority)
- Functionality gaps
- Recommended migration plan by phase
- Cost-benefit analysis
- Security improvements
- Actionable next steps

## Features

### Automated Scanning

Use the included Python scanner for automated discovery:

```bash
python altclaw/scripts/scan.py
```

This generates both JSON output (for Claude to parse) and a human-readable summary.

### Pattern Recognition

AltClaw recognizes common patterns and suggests Claude Code alternatives:

- **GitHub automation** → Built-in `gh` CLI
- **Web scraping** → WebFetch/WebSearch tools
- **File processing loops** → Native file tools with extended context
- **Multi-step workflows** → Natural language instructions or Skills
- **MCP server proxies** → Direct MCP integration
- **Manual cost tracking** → Built-in usage monitoring

### Security Audit

Automatically flags:

- Hardcoded API keys
- Overly permissive file permissions
- Credentials in version control
- Unencrypted credential storage
- Outdated dependencies

## Example Migration Scenarios

### Scenario 1: GitHub Automation
**Before (OpenClaw):**
```python
# Custom Python script with PyGithub
from github import Github
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo("user/repo")
# 50 lines of code...
```

**After (Claude Code):**
```
Create a PR with these changes
```
Native `gh` CLI integration, no code needed.

### Scenario 2: Multi-File Analysis
**Before (Moltbot):**
- Multiple API calls per file = $$$
- Manual aggregation needed
- Complex state management

**After (Claude Code):**
- Single conversation across all files
- Extended context window
- Natural conversation flow

### Scenario 3: Web Research
**Before (Clawdbot):**
```python
import requests, BeautifulSoup
# Custom scraping + parsing
# API call to process results
```

**After (Claude Code):**
```
Research the latest updates on X
```
Built-in WebFetch/WebSearch with automatic parsing.

## Advanced Usage

### Custom Scan Locations

Tell Claude to check specific directories:

```
Analyze the OpenClaw installation in ~/projects/automation/openclaw
```

### Focused Analysis

Request specific aspects:

```
Just analyze the security of my Moltbot setup
```

```
Calculate only the cost comparison for my Clawdbot usage
```

### Migration Planning

Get help implementing recommendations:

```
Help me migrate my GitHub automation from OpenClaw to Claude Code
```

## Project Structure

```
AltClaw/
├── README.md                           # This file
├── LICENSE                             # MIT License
├── altclaw/                            # The actual skill
│   ├── SKILL.md                        # Main skill definition
│   ├── scripts/
│   │   └── scan.py                     # Automated scanner
│   └── references/
│       └── openclaw-patterns.md        # Technical reference
└── examples/                           # Coming soon
    └── sample-reports/
```

## Requirements

- Claude Code or Claude.ai with Skills support
- Python 3.7+ (for automated scanner, optional)
- Read access to OpenClaw/Moltbot/Clawdbot directories

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with real OpenClaw/Moltbot/Clawdbot installations
5. Submit a pull request

## Known Limitations

AltClaw cannot migrate:

- Custom ML models or fine-tuned models
- Real-time monitoring requiring <100ms latency
- Proprietary integrations without MCP server equivalents
- Features requiring simultaneous multi-user access

For these cases, AltClaw will clearly document the gaps and suggest hybrid approaches.

## Support

- **Issues**: https://github.com/CaptainDarkHeart/AltClaw/issues
- **Discussions**: https://github.com/CaptainDarkHeart/AltClaw/discussions
- **Claude Documentation**: https://docs.anthropic.com/claude/docs

## License

MIT License - See [LICENSE](LICENSE) for details

## Acknowledgments

- Built using the [Claude Skills Starter Kit](https://github.com/CaptainDarkHeart/claude-skills-starter-kit)
- Follows the [Agent Skills Standard](https://agentskills.io)
- Inspired by the need to simplify AI automation workflows

---

**Ready to optimize your AI automation?** Install AltClaw and discover what Claude Code can do for you.
