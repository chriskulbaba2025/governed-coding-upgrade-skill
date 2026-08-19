#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md', 'SKILL.md', 'GLOBAL_AGENT_RULE.md', 'GLOBAL_CLAUDE_RULE.md', 'SCORECARD.md',
    'VERSION', 'CHANGELOG.md', 'NOTICE.md', 'CONTRIBUTING.md', 'SECURITY.md',
    'REPOSITORY_DESCRIPTOR.md', 'docs/ARCHITECTURE.md', 'docs/ADOPTION_GUIDE.md',
    'docs/UNIVERSAL_PROJECT_MODEL.md', 'docs/AGENT_ORCHESTRATION.md',
    'docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md', 'docs/TEST_AREAS.md',
    'docs/WHAT_GCU_DOES.md', 'docs/SURGICAL_CHANGE_DETERMINACY.md',
    'docs/CLAUDE_CODE_QUICKSTART.md', 'docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md',
    'docs/LLM_AGNOSTIC_USAGE.md',
    'schemas/execution_control_request.schema.json',
    'templates/GOVERNED_CHANGE_PROFILE_TEMPLATE.md',
    'templates/PROJECT_ADAPTER_TEMPLATE.md',
    'templates/AGENT_ROSTER_TEMPLATE.md',
    'templates/TEST_AREA_MAP_TEMPLATE.md',
    'templates/CHANGE_WORKSPACE_TEMPLATE.md',
    'templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md',
    'templates/CHANGE_CHECKLIST_TEMPLATE.md',
    'templates/INDEPENDENT_AUDIT_TEMPLATE.md',
    'templates/CORRECTION_TEMPLATE.md', 'templates/FINAL_REPORT_TEMPLATE.md',
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
    text = re.sub(r'[*_`]', '', text)
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
    'Project Discovery', 'Project Adapter', 'Requirement Preservation',
    'Surgical Change Determinacy Gate', 'Discovery does not create authorization',
    'Structural change budget', 'Causal Necessity Audit', 'Surgical Determinacy Audit',
    'Change Tier', 'Agent orchestration', 'Execution control plane integration',
    'gcu-execution-control/1.0.0', 'Release Authority is not an AI model-execution role',
    'Execution cost versus product external-call cost', 'usage-receipt references',
    'Test Area Map', 'Challenger gate', 'SELF_AUDIT', 'monorepo', 'FROZEN CHECKLIST',
    'EXACT-HEAD AUDIT', 'Production Spine gate', 'Producer → Contract → Consumer map',
    'Acceptance contract freeze', 'False-PASS scan', 'Sequential Evidence Gate',
    'Balanced verification', 'Real production path acceptance', 'Evidence preservation',
    'External-call contract', 'Single validated-object rule', 'Production Closure Mode',
    'Durable-job contract', 'Terminal-path gate', 'Change PASS is not Production Ready',
    'Full-system production-readiness gate', 'Machine release gate',
    'Independent exact-head audit', 'escaped-proof regression', 'vertical-spine rule',
    'GOVERNANCE HOLD', 'Interrupted-agent resume',
], 'SKILL.md', errors)

if not re.search(r'^name:\s*governed-coding-upgrade\s*$', skill, re.MULTILINE):
    errors.append('SKILL.md: machine-facing skill name must remain governed-coding-upgrade')

for rel, phrases in {
    'GLOBAL_AGENT_RULE.md': [
        'Surgical Change Determinacy Gate', 'Discovery does not create authorization',
        'Causal Necessity Audit', 'Surgical Determinacy Audit', 'T1_LOCAL',
        'PRODUCTION_READY', 'SELF_AUDIT', 'gcu-execution-control/1.0.0'
    ],
    'GLOBAL_CLAUDE_RULE.md': [
        'T1_LOCAL', 'Project Adapter', 'Test Areas', 'Challenger gate', 'SELF_AUDIT',
        'CHANGE_ONLY', 'PRODUCTION_READY', 'Producer → Contract → Consumer', 'false-PASS',
        'gcu-execution-control/1.0.0', 'usage-receipt', 'Surgical Change Determinacy Gate',
        'Causal Necessity Audit'
    ],
    'docs/SURGICAL_CHANGE_DETERMINACY.md': [
        'Requirement Preservation', 'Structural change budget',
        'Discovery does not create authorization', 'Causal Necessity Audit',
        'Surgical Determinacy Audit', 'Why only two gates'
    ],
    'docs/CLAUDE_CODE_QUICKSTART.md': [
        'Claude Code', 'GLOBAL_AGENT_RULE.md', 'Project Adapter',
        'Surgical Change Determinacy Gate', 'SELF_AUDIT'
    ],
    'docs/CHATGPT_AND_CUSTOM_GPT_USAGE.md': [
        'ChatGPT Project', 'Custom GPT', 'Project instructions', 'Knowledge',
        'GLOBAL_AGENT_RULE.md', 'Surgical Change Determinacy Gate'
    ],
    'docs/LLM_AGNOSTIC_USAGE.md': [
        'LLM-Agnostic', 'SKILL.md', 'GLOBAL_AGENT_RULE.md', 'Project Adapter'
    ],
    'docs/UNIVERSAL_PROJECT_MODEL.md': [
        'Project Discovery', 'Project Adapter', 'T1', 'T4', 'Monorepo'
    ],
    'docs/AGENT_ORCHESTRATION.md': [
        'Scout', 'Planner', 'Builder', 'Challenger', 'Verifier', 'Auditor', 'SELF_AUDIT'
    ],
    'docs/EXECUTION_CONTROL_PLANE_INTEGRATION.md': [
        'gcu-execution-control', 'capability_floor', 'Escalation contract',
        'Persistent usage receipts', 'execution-resource cost',
        'GCU MUST NOT choose a provider or concrete model', 'Fail-closed behavior'
    ],
    'docs/ARCHITECTURE.md': [
        'Execution Control Plane architecture', 'Release Authority is not model-dispatched',
        'Persistent usage architecture', 'Execution-resource cost'
    ],
    'docs/TEST_AREAS.md': [
        'STRUCTURE', 'UNIT', 'CONTRACT', 'INTEGRATION', 'END_TO_END',
        'SECURITY / PRIVACY', 'RELEASE / DEPLOYMENT'
    ],
    'templates/SURGICAL_CHANGE_CONTRACT_TEMPLATE.md': [
        'Protocol version: 2.3.0', 'Requirement Preservation', 'Structural Change Budget',
        'Causal Necessity Audit', 'Surgical Determinacy Audit'
    ],
    'templates/PROJECT_ADAPTER_TEMPLATE.md': [
        'Adapter schema version: 1.0.0', 'Project kind(s)', 'Default agent roster',
        'Execution control plane', 'Usage-ledger authority'
    ],
    'templates/AGENT_ROSTER_TEMPLATE.md': [
        'Scout', 'Challenger', 'Auditor', 'Release Authority', 'Capability floor',
        'Escalation record'
    ],
    'templates/FINAL_REPORT_TEMPLATE.md': [
        'Skill version: 2.3.0', 'Surgical Change Determinacy Gate',
        'Causal Necessity Audit', 'Surgical Determinacy Audit',
        'EXECUTION CONTROL PLANE', 'usage-receipt', 'EXECUTION COST STATUS'
    ],
    'templates/TEST_AREA_MAP_TEMPLATE.md': [
        'STRUCTURE', 'CONTRACT', 'RELIABILITY / RECOVERY', 'RELEASE / DEPLOYMENT'
    ],
    'templates/CHANGE_WORKSPACE_TEMPLATE.md': [
        'INTAKE.md', 'SURGICAL_CHANGE.md', 'TEST_AREA_MAP.md', 'EVIDENCE.md', 'AUDIT.md'
    ],
    'templates/PRODUCTION_SPINE_TEMPLATE.md': [
        'Production Spine', 'Producer → Contract → Consumer map', 'Terminal-path proof'
    ],
    'templates/ACCEPTANCE_CONTRACT_TEMPLATE.md': [
        'Acceptance Contract Template', 'False-PASS scan'
    ],
    'templates/CHANGE_CHECKLIST_TEMPLATE.md': [
        'Protocol version: 2.3.0', 'Requirement Preservation',
        'Surgical Change Determinacy Gate', 'Causal Necessity Audit',
        'Surgical Determinacy Audit', 'Test Area Map', 'Challenger gate', 'Acceptance freeze'
    ],
}.items():
    p = ROOT / rel
    require_phrases(p.read_text(encoding='utf-8') if p.exists() else '', phrases, rel, errors)

schema_path = ROOT / 'schemas/execution_control_request.schema.json'
if schema_path.exists():
    try:
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        if schema.get('properties', {}).get('contract', {}).get('const') != 'gcu-execution-control/1.0.0':
            errors.append('execution-control schema: contract version is not canonical')
        roles = schema.get('properties', {}).get('role', {}).get('enum', [])
        if roles != ['SCOUT', 'PLANNER', 'BUILDER', 'CHALLENGER', 'VERIFIER', 'AUDITOR']:
            errors.append('execution-control schema: AI-executable role enum is not canonical')
        capability = schema.get('properties', {}).get('capabilityFloor', {}).get('enum', [])
        if capability != ['ECONOMY', 'STANDARD', 'ADVANCED', 'PREMIUM']:
            errors.append('execution-control schema: capabilityFloor enum is not canonical')
        reasons = schema.get('properties', {}).get('escalationReason', {}).get('enum', [])
        expected_reasons = [
            'CAPABILITY_INSUFFICIENT', 'INDEPENDENCE_REQUIRED', 'CONTEXT_LIMIT',
            'REPEATED_PROOF_FAILURE', 'POLICY_REQUIREMENT', 'MATERIAL_AMBIGUITY'
        ]
        if reasons != expected_reasons:
            errors.append('execution-control schema: escalationReason enum is not canonical')
    except json.JSONDecodeError as exc:
        errors.append(f'execution-control schema: invalid JSON: {exc}')

score = (ROOT/'SCORECARD.md').read_text(encoding='utf-8') if (ROOT/'SCORECARD.md').exists() else ''
nums = [int(x) for x in re.findall(r'—\s*(\d{1,2})/20', score)]
if len(nums) < 5 or any(n < 19 for n in nums[:5]):
    errors.append('SCORECARD.md: five semantic areas are not all >=19/20')

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
print('Requirement Preservation controls: PRESENT')
print('Surgical Change Determinacy Gate: PRESENT')
print('Structural change budget controls: PRESENT')
print('Causal Necessity Audit: PRESENT')
print('Surgical Determinacy Audit: PRESENT')
print('LLM-agnostic invocation rule: PRESENT')
print('Project Discovery / Adapter controls: PRESENT')
print('Change Tier controls: PRESENT')
print('Agent orchestration controls: PRESENT')
print('Execution control plane integration: PRESENT')
print('Canonical execution-control request schema: PRESENT')
print('Universal Test Area Map controls: PRESENT')
print('Production Spine controls: PRESENT')
print('Contract-map controls: PRESENT')
print('Acceptance freeze / false-PASS controls: PRESENT')
print('Sequential Evidence Gates: PRESENT')
print('Challenger gate: PRESENT')
print('Terminal-path / full-system readiness controls: PRESENT')
print('Semantic threshold: >=19/20 in all five areas')
