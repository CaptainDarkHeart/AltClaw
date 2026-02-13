# Testing AltClaw

Guide for testing the AltClaw skill.

## Pre-Installation Testing

### Verify Skill Structure
```bash
cd AltClaw

# Check that SKILL.md exists
test -f altclaw/SKILL.md && echo "✓ SKILL.md found" || echo "✗ SKILL.md missing"

# Check that SKILL.md has YAML frontmatter
head -n 5 altclaw/SKILL.md | grep -q "^name:" && echo "✓ YAML frontmatter present" || echo "✗ YAML frontmatter missing"

# Check folder naming (should be lowercase with hyphens)
basename altclaw | grep -q "^[a-z-]*$" && echo "✓ Folder name is kebab-case" || echo "✗ Folder name invalid"

# Verify scanner script is executable
test -x altclaw/scripts/scan.py && echo "✓ Scanner is executable" || echo "✗ Scanner not executable"
```

### Package for Claude.ai
```bash
# Create distribution package
zip -r altclaw.zip altclaw/

# Verify package contents
unzip -l altclaw.zip

# Should show:
# altclaw/SKILL.md
# altclaw/scripts/scan.py
# altclaw/references/openclaw-patterns.md
```

## Post-Installation Testing

### Test 1: Skill Recognition
Ask Claude:
```
When would you use the altclaw skill?
```

**Expected Response:**
Should mention analyzing OpenClaw, Moltbot, or Clawdbot installations.

### Test 2: Trigger Phrases
Try each of these phrases:

```
Analyze my OpenClaw installation
```

```
Check my Moltbot setup for improvements
```

```
Audit my Clawdbot configuration
```

```
Can I migrate from OpenClaw to Claude Code?
```

```
Compare my automation to Claude Code
```

**Expected Behavior:**
- AltClaw skill should activate
- Should ask for installation location if not found automatically
- Should begin discovery phase

### Test 3: Scanner Script
```bash
# Run the scanner directly
cd altclaw/scripts
python scan.py

# Should output:
# - Search results for known locations
# - JSON output of findings
# - Human-readable summary
```

### Test 4: False Positive Check
These should NOT trigger AltClaw:

```
Help me with Python
```

```
Create a web scraper
```

```
Analyze this code
```

**Expected Behavior:**
AltClaw should NOT activate for general requests.

## Functional Testing

### Test 5: Mock Installation Analysis

Create a test OpenClaw installation:

```bash
# Create test structure
mkdir -p /tmp/test-openclaw/{scripts,prompts}

# Create mock config
cat > /tmp/test-openclaw/config.yaml <<EOF
api:
  provider: openai
  model: gpt-4
  rate_limit: 100

github:
  token: ghp_test123
  auto_pr: true

workflows:
  - name: daily_report
    schedule: "0 9 * * *"
EOF

# Create mock .env
cat > /tmp/test-openclaw/.env <<EOF
OPENAI_API_KEY=sk-test123456
GITHUB_TOKEN=ghp_test789
EOF

# Create mock script
cat > /tmp/test-openclaw/scripts/github_helper.py <<'EOF'
from github import Github
import os

g = Github(os.getenv('GITHUB_TOKEN'))
# Does stuff
EOF
```

Now ask Claude:
```
Analyze the OpenClaw installation at /tmp/test-openclaw
```

**Expected Response:**
- Should read config files
- Should identify API usage patterns
- Should flag security issues (permissions, hardcoded keys)
- Should suggest Claude Code alternatives
- Should generate migration recommendations

### Test 6: Security Audit

Using the test installation above, AltClaw should flag:
- ✓ Hardcoded API keys in config
- ✓ Tokens in .env file
- ✓ PyGithub dependency (can be replaced)
- ✓ File permissions (if wrong)

### Test 7: Cost Analysis

Ask Claude:
```
Calculate the cost savings for migrating this OpenClaw setup to Claude Code
```

**Expected Response:**
- Current estimated monthly cost
- Projected Claude Code cost
- Percentage savings
- ROI calculation

### Test 8: Migration Planning

Ask Claude:
```
Create a migration plan for moving from OpenClaw to Claude Code
```

**Expected Response:**
- Phased approach (Phase 1, 2, 3)
- Prioritized by impact/effort
- Specific recommendations for each component
- Timeline estimates
- Next steps

## Edge Cases

### Test 9: No Installation Found
```
Analyze my OpenClaw installation
```

When no installation exists.

**Expected Behavior:**
- Should report no installation found
- Should ask if user wants to specify a custom location
- Should offer to analyze a different location

### Test 10: Custom Location
```
Analyze the Moltbot installation at ~/custom/path/moltbot
```

**Expected Behavior:**
- Should accept custom path
- Should scan that specific location
- Should work even if not in standard location

### Test 11: Partial Installation
Create incomplete installation:
```bash
mkdir -p /tmp/partial-moltbot
touch /tmp/partial-moltbot/config.json
# No other files
```

Ask:
```
Analyze /tmp/partial-moltbot
```

**Expected Behavior:**
- Should handle gracefully
- Should report what was found
- Should not crash

## Performance Testing

### Test 12: Large Installation
Create a large test installation:
```bash
mkdir -p /tmp/large-openclaw/scripts
for i in {1..50}; do
  echo "# Script $i" > /tmp/large-openclaw/scripts/script_$i.py
done
```

Ask:
```
Analyze /tmp/large-openclaw
```

**Expected Behavior:**
- Should complete within reasonable time (<2 minutes)
- Should summarize findings, not list all 50 scripts individually
- Should focus on patterns, not individual files

## Cleanup

Remove test installations:
```bash
rm -rf /tmp/test-openclaw
rm -rf /tmp/partial-moltbot
rm -rf /tmp/large-openclaw
```

## Automated Test Script

Save this as `test-altclaw.sh`:

```bash
#!/bin/bash

echo "=== AltClaw Skill Tests ==="

# Test 1: File structure
echo -n "Test 1: SKILL.md exists... "
test -f altclaw/SKILL.md && echo "PASS" || echo "FAIL"

# Test 2: YAML frontmatter
echo -n "Test 2: YAML frontmatter... "
head -n 5 altclaw/SKILL.md | grep -q "^name: altclaw" && echo "PASS" || echo "FAIL"

# Test 3: Scanner executable
echo -n "Test 3: Scanner executable... "
test -x altclaw/scripts/scan.py && echo "PASS" || echo "FAIL"

# Test 4: Scanner runs
echo -n "Test 4: Scanner runs... "
python altclaw/scripts/scan.py > /dev/null 2>&1 && echo "PASS" || echo "FAIL"

# Test 5: References exist
echo -n "Test 5: Reference docs... "
test -f altclaw/references/openclaw-patterns.md && echo "PASS" || echo "FAIL"

echo ""
echo "=== Tests Complete ==="
```

Run with:
```bash
chmod +x test-altclaw.sh
./test-altclaw.sh
```

## Success Criteria

AltClaw is working correctly if:

- ✅ Skill recognized by Claude ("When would you use...")
- ✅ Activates on relevant trigger phrases
- ✅ Does NOT activate on unrelated requests
- ✅ Scanner script runs without errors
- ✅ Generates structured analysis reports
- ✅ Identifies security issues
- ✅ Provides cost calculations
- ✅ Creates migration plans
- ✅ Handles edge cases gracefully

## Reporting Issues

If tests fail, please report at:
https://github.com/CaptainDarkHeart/AltClaw/issues

Include:
- Which test failed
- Claude version (ai or CLI)
- Error messages
- Platform (macOS, Linux, Windows)
