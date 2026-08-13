# Acceptance Contract Template

**Change ID / checklist section:**  
**Frozen before production implementation:** YES / NO  

## Positive path

- Entry boundary:
- Real production modules executed:
- Controlled dependency seam:
- Production validators/contracts used:
- Persisted state/artifacts inspected:
- Terminal result asserted:
- Exact command:

## Negative / fail-closed path

- Invalid/failure input:
- Exact rejection/classification:
- Persisted failure state:
- Prohibited later events:
- Prohibited later effects:

## Execution ceiling

- Live execution allowed:
- Maximum explicitly authorized usage when applicable:
- Counter source:
- Unexpected external execution behavior:

## False-PASS scan

- [ ] No unconditional assertion or hardcoded PASS.
- [ ] No always-valid validator.
- [ ] No fabricated normalized success replacing the production producer.
- [ ] No pre-seeded intermediate/terminal state bypassing the path under proof.
- [ ] No persistence double that bypasses required persistence semantics.
- [ ] No hardcoded execution/cost PASS.
- [ ] No mocks above the production boundary being proved.
- [ ] No `A OR B` assertion where one governed result is required.
- [ ] No local substitute presented as mandatory exact-head CI.
