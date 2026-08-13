## Governed change

**Change ID:**  
**Frozen checklist:**  
**Starting SHA:**  
**Final SHA:**  
**Primary class:**  
**Release intent:** CHANGE_ONLY / STAGING_READY / PRODUCTION_READY  

### Scope

- [ ] Changed files are inside the permitted list.
- [ ] Prohibited files are untouched.
- [ ] Complete diff was reviewed.

### Production correctness

- [ ] Production spine is traced when applicable.
- [ ] Producer → Contract → Consumer map is complete when applicable.
- [ ] Acceptance contract was frozen before implementation.
- [ ] False-PASS scan completed.
- [ ] Terminal-path/full-system readiness proof matches the declared release intent.

### Proof

- [ ] Every checklist ID has direct evidence.
- [ ] Required negative paths are proven.
- [ ] Protected invariants are proven.
- [ ] Required regression passes.
- [ ] Package validation passes.

### Exact-head audit

- [ ] CI corresponds to the reported final SHA when applicable.
- [ ] Independent exact-head audit returns PASS.
- [ ] Merge/release authorization is explicit and has not been inferred.
