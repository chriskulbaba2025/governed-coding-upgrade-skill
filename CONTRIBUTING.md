# Contributing

Changes to this repository are themselves governed changes.

## Maintainer authority

The canonical repository is maintained by **Chris Kulbaba (@chriskulbaba2025)**.

External contributors may propose changes through pull requests. A contribution does not grant write, merge, release, tag, administrative, or canonical-version authority. Only the repository maintainer may authorize an official merge or release unless that authority is explicitly delegated in GitHub repository settings.

## Required process

1. Start from a verified branch, SHA, and clean or explained working tree.
2. Identify the exact change objective and protected invariants.
3. Freeze a checklist before changing governed behavior.
4. Keep changed files inside the approved scope.
5. Provide direct proof for every requirement.
6. Run `python scripts/validate-package.py` before opening a pull request.
7. Use the pull-request template and report the exact final SHA.
8. Do not merge until required review/audit gates pass and the maintainer authorizes the merge.

A change that weakens the protocol's frozen-scope, direct-proof, exact-head, independent-audit, or authorization controls must be explicitly identified as a governance change and reviewed as such.
