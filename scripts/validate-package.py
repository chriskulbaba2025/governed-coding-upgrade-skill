#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'SKILL.md', 'GLOBAL_CLAUDE_RULE.md', 'SCORECARD.md',
    'VERSION', 'CHANGELOG.md', 'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md',
    'REPOSITORY_DESCRIPTOR.md', 'docs/ARCHITECTURE.md', 'docs/ADOPTION_GUIDE.md',
    'templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md',
    'templates/CHANGE_CHECKLIST_TEMPLATE.md',
    'templates/INDEPENDENT_AUDIT_TEMPLATE.md',
    'templates/CORRECTION_TEMPLATE.md',
    'templates/FINAL_REPORT_TEMPLATE.md',
    'templates/PRODUCTION_CLOSURE_TEMPLATE.md',
    'templates/MACHINE_RELEASE_GATE_TEMPLATE.md',
    'templates/PRODUCTION_SPINE_TEMPLATE.md',
    'templates/ACCEPTANCE_CONTRACT_TEMPLATE.md',
    'branding/logo.svg', 'branding/icon.svg', 'branding/icon.png',
    'branding/social-card.svg', 'branding/social-card.png', 'branding/README.md',
    '.github/PULL_REQUEST_TEMPLATE.md', '.github/CODEOWNERS',
    '.github/workflows/repository-quality.yml',
]


def normalized(text: str) -> str:
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

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip() if (ROOT / 'VERSION').exists() else ''
for rel in ['SKILL.md', 'README.md', 'SCORECARD.md', 'REPOSITORY_DESCRIPTOR.md', 'CHANGELOG.md']:
    p = ROOT / rel
    if p.exists() and version and version not in p.read_text(encoding='utf-8'):
        errors.append(f'{rel}: does not contain VERSION {version}')

skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8') if (ROOT / 'SKILL.md').exists() else ''
require_phrases(skill, [
    'FROZEN CHECKLIST',
    'EXACT-HEAD AUDIT',
    'Production Spine gate',
    'Producer → Contract → Consumer map',
    'Acceptance contract freeze',
    'False-PASS scan',
    'Sequential Evidence Gate',
    'Balanced verification',
    'Real production path acceptance',
    'Evidence preservation',
    'External-call contract',
    'Single validated-object rule',
    'Production Closure Mode',
    'Durable-job contract',
    'Terminal-path gate',
    'Change PASS is not Production Ready',
    'Full-system production-readiness gate',
    'Machine release gate',
    'Independent exact-head audit',
    'escaped-proof regression',
    'vertical-spine rule',
    'GOVERNANCE HOLD',
    'Interrupted-agent resume',
], 'SKILL.md', errors)

if not re.search(r'^name:\s*governed-coding-upgrade\s*$', skill, re.MULTILINE):
    errors.append('SKILL.md: machine-facing skill name must remain governed-coding-upgrade')

for rel, phrases in {
    'templates/PRODUCTION_SPINE_TEMPLATE.md': [
        'Production Spine', 'Producer → Contract → Consumer map', 'Terminal-path proof'
    ],
    'templates/ACCEPTANCE_CONTRACT_TEMPLATE.md': [
        'Acceptance Contract Template', 'False-PASS scan'
    ],
    'GLOBAL_CLAUDE_RULE.md': [
        'CHANGE_ONLY', 'PRODUCTION_READY', 'Producer → Contract → Consumer', 'false-PASS'
    ],
    'templates/CHANGE_CHECKLIST_TEMPLATE.md': [
        'Protocol version: 2.1.0', 'Production correctness', 'Acceptance freeze'
    ],
}.items():
    p = ROOT / rel
    require_phrases(p.read_text(encoding='utf-8') if p.exists() else '', phrases, rel, errors)

score = (ROOT / 'SCORECARD.md').read_text(encoding='utf-8') if (ROOT / 'SCORECARD.md').exists() else ''
nums = [int(x) for x in re.findall(r'—\s*(\d{1,2})/20', score)]
if len(nums) < 5 or any(n < 19 for n in nums[:5]):
    errors.append('SCORECARD.md: five semantic areas are not all >=19/20')

for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if target.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        clean = target.split('#', 1)[0]
        if clean and not (md.parent / clean).resolve().exists():
            errors.append(f'{md.relative_to(ROOT)}: broken local link: {target}')

if errors:
    print('BLOCKED')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)

print('PASS')
print(f'Version: {version}')
print(f'Required files: {len(REQUIRED)}/{len(REQUIRED)}')
print('Production Spine controls: PRESENT')
print('Contract-map controls: PRESENT')
print('Acceptance freeze / false-PASS controls: PRESENT')
print('Sequential Evidence Gates: PRESENT')
print('Terminal-path / full-system readiness controls: PRESENT')
print('Semantic threshold: >=19/20 in all five areas')
