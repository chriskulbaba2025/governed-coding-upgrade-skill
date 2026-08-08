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
    'branding/logo.svg', 'branding/icon.svg', 'branding/icon.png', 'branding/social-card.svg', 'branding/social-card.png', 'branding/README.md',
    '.github/PULL_REQUEST_TEMPLATE.md', '.github/CODEOWNERS',
    '.github/workflows/repository-quality.yml',
]

errors = []
for rel in REQUIRED:
    p = ROOT / rel
    if not p.is_file() or p.stat().st_size == 0:
        errors.append(f'missing or empty: {rel}')

version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip() if (ROOT/'VERSION').exists() else ''
for rel in ['SKILL.md', 'SCORECARD.md']:
    p = ROOT / rel
    if p.exists() and version and version not in p.read_text(encoding='utf-8'):
        errors.append(f'{rel}: does not contain VERSION {version}')

skill = (ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
for phrase in ['FROZEN CHECKLIST', 'EXACT-HEAD AUDIT', 'Governed Change Profile']:
    if phrase.lower() not in skill.lower():
        errors.append(f'SKILL.md: required control phrase absent: {phrase}')

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
print('Semantic threshold: >=19/20 in all five areas')
