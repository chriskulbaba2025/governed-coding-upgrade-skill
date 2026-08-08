# Contributing

Changes to this repository are themselves governed changes.

## Required process

1. Start from a verified branch, SHA, and clean or explained working tree.
2. Identify the exact change objective and protected invariants.
3. Freeze a checklist before changing governed behavior.
4. Keep changed files inside the approved scope.
5. Provide direct proof for every requirement.
6. Run `python scripts/validate-package.py` before opening a pull request.
7. Use the pull-request template and report the exact final SHA.
8. Do not merge until required review/audit gates pass.

A change that weakens the protocol's frozen-scope, direct-proof, exact-head, independent-audit, or authorization controls must be explicitly identified as a governance change and reviewed as such.
