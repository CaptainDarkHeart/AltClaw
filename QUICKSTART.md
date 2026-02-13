# AltClaw Quick Start

Get started with AltClaw in 5 minutes.

## Install (Choose One)

### Claude.ai
```bash
git clone https://github.com/CaptainDarkHeart/AltClaw.git
cd AltClaw
zip -r altclaw.zip altclaw/
```
Then upload `altclaw.zip` to Claude.ai → Settings → Skills

### Claude Code
```bash
git clone https://github.com/CaptainDarkHeart/AltClaw.git
ln -s "$(pwd)/AltClaw/altclaw" ~/.claude/skills/altclaw
```

## Use It

Just ask Claude:

```
Analyze my OpenClaw installation
```

or

```
Check if I should migrate from Moltbot to Claude Code
```

## What You Get

AltClaw will:
1. 🔍 Find your OpenClaw/Moltbot/Clawdbot installation
2. 📊 Analyze configuration, workflows, and costs
3. 💰 Calculate potential savings
4. 🔒 Identify security issues
5. 🗺️ Create a migration plan
6. ⚡ Recommend Claude Code alternatives

## Example Output

```markdown
# AltClaw Analysis Report

## Executive Summary
- Current cost: $127/month
- Claude Code cost: $33/month
- Savings: 84% ($1,284/year)

## Migration Opportunities
1. GitHub automation → Built-in gh CLI
   - Remove 200 lines of Python
   - Save $45/month

2. Web scraping → WebFetch/WebSearch
   - Remove dependencies
   - Save $35/month

... [detailed analysis continues]
```

## Next Steps

After getting your analysis:

1. Review the migration opportunities
2. Ask Claude to help implement high-priority items
3. Test migrations in parallel with existing setup
4. Decommission OpenClaw/Moltbot once migrated

## Need Help?

- Full docs: [README.md](README.md)
- Installation: [INSTALLATION.md](INSTALLATION.md)
- Testing: [TESTING.md](TESTING.md)
- Issues: https://github.com/CaptainDarkHeart/AltClaw/issues

---

**That's it!** Start optimizing your AI automation now.
