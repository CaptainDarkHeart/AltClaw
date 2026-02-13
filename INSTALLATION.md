# AltClaw Installation Guide

Quick guide to install and use the AltClaw skill.

## For Claude.ai (Web Version)

### Method 1: Download from GitHub
1. Visit https://github.com/CaptainDarkHeart/AltClaw
2. Click the green "Code" button → "Download ZIP"
3. Extract the ZIP file
4. Create a new ZIP containing ONLY the `altclaw/` folder:
   ```bash
   cd AltClaw
   zip -r altclaw.zip altclaw/
   ```
5. Go to [Claude.ai](https://claude.ai)
6. Click your profile → **Settings** → **Capabilities** → **Skills**
7. Click **Upload skill**
8. Select `altclaw.zip`
9. Wait for confirmation

### Method 2: Clone and Package
```bash
# Clone the repository
git clone https://github.com/CaptainDarkHeart/AltClaw.git
cd AltClaw

# Create skill package
zip -r altclaw.zip altclaw/

# Upload altclaw.zip to Claude.ai as described above
```

## For Claude Code (CLI)

### Method 1: Symlink (Recommended)
```bash
# Clone the repository
git clone https://github.com/CaptainDarkHeart/AltClaw.git
cd AltClaw

# Create symlink in Claude's skills directory
ln -s "$(pwd)/altclaw" ~/.claude/skills/altclaw

# Verify the link
ls -la ~/.claude/skills/
```

### Method 2: Copy Files
```bash
# Clone the repository
git clone https://github.com/CaptainDarkHeart/AltClaw.git
cd AltClaw

# Copy to skills directory
mkdir -p ~/.claude/skills
cp -r altclaw ~/.claude/skills/

# Verify installation
ls -la ~/.claude/skills/altclaw/
```

### Restart Claude Code
After installing, restart Claude Code or reload skills:
```bash
# If Claude Code is running
# Press Ctrl+C and restart, or use reload command if available
```

## Verify Installation

Ask Claude one of these questions:

```
When would you use the altclaw skill?
```

You should get a response mentioning analyzing OpenClaw/Moltbot/Clawdbot installations.

Or just try using it:

```
Analyze my OpenClaw installation
```

## Testing the Scanner Script

The included Python scanner can be run independently:

```bash
cd AltClaw/altclaw/scripts
python scan.py
```

This will scan your system for installations and output both JSON and a summary report.

## Troubleshooting

### Skill Not Found
- **Claude.ai**: Make sure you uploaded the `altclaw` folder itself, not the parent directory
- **Claude Code**: Check that `~/.claude/skills/altclaw/SKILL.md` exists
- Verify the YAML frontmatter in SKILL.md is properly formatted

### Skill Not Triggering
- Try more explicit phrases: "use altclaw to analyze my openclaw setup"
- Check that the skill description in SKILL.md includes relevant keywords
- Make sure you're asking about OpenClaw/Moltbot/Clawdbot specifically

### Scanner Script Issues
Make sure you have Python 3.7+:
```bash
python --version  # or python3 --version
```

The scanner uses only standard library modules, so no additional dependencies are needed.

### Permission Issues
If Claude can't read certain directories:
```bash
# Check permissions on config directories
ls -la ~/.openclaw
ls -la ~/.moltbot
ls -la ~/.clawdbot

# Fix if needed (example)
chmod 700 ~/.openclaw
```

## Updating the Skill

### Claude.ai
1. Download the latest version from GitHub
2. Package it: `zip -r altclaw.zip altclaw/`
3. Re-upload to Claude.ai (it will replace the existing version)

### Claude Code (Symlink Method)
```bash
cd AltClaw
git pull origin main
# No further action needed - symlink automatically uses latest version
```

### Claude Code (Copy Method)
```bash
cd AltClaw
git pull origin main
cp -r altclaw ~/.claude/skills/
# Restart Claude Code
```

## Next Steps

Once installed, see [README.md](README.md) for usage examples and documentation.

## Getting Help

- **Issues**: https://github.com/CaptainDarkHeart/AltClaw/issues
- **Documentation**: See README.md and examples/
- **Claude Docs**: https://docs.anthropic.com/claude/docs/skills
