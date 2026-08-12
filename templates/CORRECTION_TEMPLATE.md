# Consolidated Correction

**Protocol version:** 1.2.0  
**Failed head SHA:**  
**Failed checklist IDs / release conditions:**  

Correct only the listed failed checklist IDs or machine-gate conditions.

## Rules

- Do not reopen accepted IDs unless directly required by the correction.
- Do not add optional scope.
- Assign each defect to the smallest owning section/boundary.
- Add or repair direct proof before changing implementation when the original implementation claim was unproven.
- Keep the original permitted/prohibited file boundary unless a proven contract defect requires a versioned checklist revision.
- Rerun the owning section's narrow proof first.
- Rerun only affected later/earlier sections that can be invalidated by the correction.
- Repeat cross-section review when the correction changes a boundary contract.
- Run the complete terminal verification sequence once affected sections are green.
- Rerun the terminal machine release gate.
- Produce one corrected exact head.
- Perform a new independent exact-head audit.
- Do not substitute local commands for mandatory exact-head CI.
- If code verification passes but a mandatory temporary external release condition remains unavailable, report `CODE VERIFIED / GOVERNANCE HOLD` rather than final PASS.
- Do not merge, deploy, release, or activate without required authorization.
