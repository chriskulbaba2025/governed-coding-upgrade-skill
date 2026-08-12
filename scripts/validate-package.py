#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'SKILL.md', 'GLOBAL_CLAUDE_RULE.md', 'SCORECARD.md',
    'VERSION', 'CHANGELOG.md', 'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md',
    'REPOSITORY_DESCRIPTOR.md', 'docs/ARCHITECTURE.md', 'docs/ADOPTION_GUIDE.md',
    'templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md',
    'templates/CHANGE_CHECKLIST_TEMPLATE.md',
    'templates/INDEPENDENT_AUDIT_TEMPLATE.md',
    'templates/CORRECTION_TEMPLATE.md', 'templates/FINAL_REPORT_TEMPLATE.md',
    'templates/PRODUCTION_CLOSURE_TEMPLATE.md',
    'templates/MACHINE_RELEASE_GATE_TEMPLATE.md',
    'branding/logo.svg', 'branding/icon.svg', 'branding/icon.png',
    'branding/social-card.svg', 'branding/social-card.png', 'branding/README.md',
    '.github/PULL_REQUEST_TEMPLATE.md', '.github/CODEOWNERS',
    '.github/workflows/repository-quality.yml',
]


def normalized(text: str) -> str:
    """Normalize formatting whitespace without weakening phrase requirements."""
    return re.sub(r'\s+', ' ', text).strip().lower()


def require_phrases(text: str, phrases, label: str, errors):
    haystack = normalized(text)
    for phrase in phrases:
        if normalized(phrase) not in haystack:
            errors.append(f'{label}: required control phrase absent: {phrase}')


errors = []
for rel in REQUIRED:
    p = ROOT / rel
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f'missing or empty: {rel}')

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip() if (ROOT/'VERSION').exists() else ''
for rel in ['SKILL.md', 'README.md', 'SCORECARD.md', 'REPOSITORY_DESCRIPTOR.md', 'CHANGELOG.md']:
    p = ROOT / rel
    if p.exists() and version and version not in p.read_text(encoding='utf-8'):
        errors.append(f'{rel}: does not contain VERSION {version}')

skill = (ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
require_phrases(skill, [
    'FROZEN CHECKLIST',
    'EXACT-HEAD AUDIT',
    'Governed Change Profile',
    'PRODUCTION CLOSURE',
    'repository-owned',
    'real production',
    'genuine external blocker',
    'Sequential Evidence Gate',
    'Balanced machine verification',
    'Terminal machine release gate',
    'GOVERNANCE HOLD',
    'Interrupted-agent resume',
    'Controlled external-call and credential isolation',
], 'SKILL.md', errors)

if not re.search(r'^name:\s*governed-coding-upgrade\s*$', skill, re.MULTILINE):
    errors.append('SKILL.md: machine-facing skill name must remain governed-coding-upgrade')

closure = (ROOT/'templates/PRODUCTION_CLOSURE_TEMPLATE.md').read_text(encoding='utf-8') if (ROOT/'templates/PRODUCTION_CLOSURE_TEMPLATE.md').exists() else ''
require_phrases(closure, [
    'PRODUCTION_CLOSURE',
    'real production',
    'genuine external blocker',
    'MANDATORY SEQUENTIAL SECTION RULE',
    'BALANCED MACHINE CHECKS',
    'TERMINAL MACHINE RELEASE GATE',
    'GOVERNANCE HOLD',
    'Do not merge',
], 'PRODUCTION_CLOSURE_TEMPLATE.md', errors)

machine = (ROOT/'templates/MACHINE_RELEASE_GATE_TEMPLATE.md').read_text(encoding='utf-8') if (ROOT/'templates/MACHINE_RELEASE_GATE_TEMPLATE.md').exists() else ''
require_phrases(machine, [
    'Machine Release Gate Template',
    'exit `0`',
    'exact final SHA',
    'GOVERNANCE HOLD',
    'Local reruns do not substitute for mandatory exact-head CI',
    'controlled transports',
], 'MACHINE_RELEASE_GATE_TEMPLATE.md', errors)

global_rule = (ROOT/'GLOBAL_CLAUDE_RULE.md').read_text(encoding='utf-8') if (ROOT/'GLOBAL_CLAUDE_RULE.md').exists() else ''
require_phrases(global_rule, [
    'automatically continue on PASS',
    'balanced machine verification',
    'terminal machine release gate',
    'CODE VERIFIED / GOVERNANCE HOLD',
], 'GLOBAL_CLAUDE_RULE.md', errors)

score = (ROOT/'SCORECARD.md').read_text(encoding='utf-8') if (ROOT/'SCORECARD.md').exists() else ''
nums = [int(x) for x in re.findall(r'—\s*(\d{1,2})/20', score)]
if len(nums) < 5 or any(n < 19 for n in nums[:5]):
    errors.append('SCORECARD.md: five semantic areas are not all >=19/20')

# Validate relative Markdown links to local files.
for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','#','mailto:')):
            continue
        clean = target.split('#',1)[0]
        if not clean:
            continue
        if not (md.parent / clean).resolve().exists():
            errors.append(f'{md.relative_to(ROOT)}: broken local link: {target}')

if errors:
    print('BLOCKED')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print('PASS')
print(f'Version: {version}')
print(f'Required files: {len(REQUIRED)}/{len(REQUIRED)}')
print('Machine-facing skill name: governed-coding-upgrade')
print('Production Closure controls: PRESENT')
print('Sequential Evidence Gates: PRESENT')
print('Balanced machine verification: PRESENT')
print('Terminal machine release gate: PRESENT')
print('Governance-hold state: PRESENT')
print('Semantic threshold: >=19/20 in all five areas')
