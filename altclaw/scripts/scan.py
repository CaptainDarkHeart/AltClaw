#!/usr/bin/env python3
"""
AltClaw Scanner
Automatically discovers and analyzes OpenClaw/Moltbot/Clawdbot installations
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any

class InstallationScanner:
    """Scans for OpenClaw/Moltbot/Clawdbot installations"""

    KNOWN_LOCATIONS = {
        'openclaw': [
            '~/.openclaw/',
            '~/.config/openclaw/',
        ],
        'moltbot': [
            '~/.moltbot/',
            '~/.config/moltbot/',
        ],
        'clawdbot': [
            '~/.clawdbot/',
            '~/.config/clawdbot/',
        ]
    }

    CONFIG_FILES = {
        'openclaw': ['config.yaml', 'config.yml', '.env'],
        'moltbot': ['settings.json', 'config.yaml', 'credentials.yaml'],
        'clawdbot': ['config.toml', 'api.conf', 'settings.json']
    }

    def __init__(self):
        self.findings = {
            'openclaw': [],
            'moltbot': [],
            'clawdbot': []
        }

    def scan(self) -> Dict[str, Any]:
        """Run full scan of the system"""
        print("🔍 Scanning for OpenClaw/Moltbot/Clawdbot installations...\n")

        for tool_name, locations in self.KNOWN_LOCATIONS.items():
            for location in locations:
                expanded = Path(location).expanduser()
                if expanded.exists():
                    print(f"✓ Found {tool_name} at: {expanded}")
                    installation = self.analyze_installation(tool_name, expanded)
                    if installation:
                        self.findings[tool_name].append(installation)

        return self.findings

    def analyze_installation(self, tool_name: str, path: Path) -> Dict[str, Any]:
        """Analyze a specific installation"""
        installation = {
            'path': str(path),
            'configs': [],
            'scripts': [],
            'integrations': [],
            'security_issues': []
        }

        # Find config files
        for config_file in self.CONFIG_FILES.get(tool_name, []):
            config_path = path / config_file
            if config_path.exists():
                installation['configs'].append({
                    'file': config_file,
                    'path': str(config_path),
                    'size': config_path.stat().st_size
                })

                # Check for security issues
                if config_file == '.env':
                    if oct(config_path.stat().st_mode)[-3:] != '600':
                        installation['security_issues'].append(
                            f"{config_file} has overly permissive permissions"
                        )

        # Find Python scripts
        for script in path.rglob('*.py'):
            installation['scripts'].append(str(script))

            # Basic security scan
            content = script.read_text(errors='ignore')
            if 'sk-' in content or 'api_key' in content.lower():
                installation['security_issues'].append(
                    f"Potential hardcoded API key in {script.name}"
                )

        # Look for integration indicators
        requirements_file = path / 'requirements.txt'
        if requirements_file.exists():
            content = requirements_file.read_text()
            integrations = []
            if 'pygithub' in content.lower() or 'github' in content.lower():
                integrations.append('GitHub')
            if 'requests' in content.lower() or 'beautifulsoup' in content.lower():
                integrations.append('Web Scraping')
            if 'slack' in content.lower():
                integrations.append('Slack')
            if 'openai' in content.lower():
                integrations.append('OpenAI API')
            if 'anthropic' in content.lower():
                integrations.append('Anthropic API')
            installation['integrations'] = integrations

        return installation if installation['configs'] else None

    def generate_report(self) -> str:
        """Generate a summary report"""
        report = ["# AltClaw Scan Results\n"]

        total_installations = sum(len(v) for v in self.findings.values())

        if total_installations == 0:
            report.append("No OpenClaw/Moltbot/Clawdbot installations found.\n")
            return "\n".join(report)

        report.append(f"Found {total_installations} installation(s)\n")

        for tool_name, installations in self.findings.items():
            if not installations:
                continue

            report.append(f"\n## {tool_name.title()}\n")

            for install in installations:
                report.append(f"### Installation at {install['path']}\n")

                if install['configs']:
                    report.append("**Configuration Files:**")
                    for cfg in install['configs']:
                        report.append(f"- {cfg['file']} ({cfg['size']} bytes)")
                    report.append("")

                if install['scripts']:
                    report.append(f"**Scripts:** {len(install['scripts'])} Python files found\n")

                if install['integrations']:
                    report.append("**Integrations:**")
                    for integration in install['integrations']:
                        report.append(f"- {integration}")
                    report.append("")

                if install['security_issues']:
                    report.append("**⚠️ Security Issues:**")
                    for issue in install['security_issues']:
                        report.append(f"- {issue}")
                    report.append("")

        return "\n".join(report)

def main():
    scanner = InstallationScanner()
    findings = scanner.scan()

    # Output JSON for Claude to parse
    print("\n" + "="*60)
    print("JSON Output:")
    print("="*60)
    print(json.dumps(findings, indent=2))

    # Output human-readable report
    print("\n" + "="*60)
    print("Summary Report:")
    print("="*60)
    print(scanner.generate_report())

if __name__ == '__main__':
    main()
