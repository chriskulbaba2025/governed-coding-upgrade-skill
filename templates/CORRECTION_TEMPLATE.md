# Consolidated Correction

**Protocol version:** 2.1.0  
**Failed head SHA:**  
**Failed checklist IDs / release conditions:**  

Correct only the listed failed checklist IDs or release conditions.

## Rules

- Do not reopen accepted IDs unless directly required by the correction.
- Do not add optional scope.
- Assign each defect to the smallest owning section/boundary.
- Add or repair direct proof before changing implementation when the original claim was unproven.
- Keep permitted/prohibited scope unless a proven contract defect requires a versioned checklist revision.
- Rerun the owning section’s narrow proof first.
- Rerun only affected sections that can be invalidated.
- Repeat contract-map/cross-section review when the correction changes a handoff.
- If the defect escaped earlier green proof, correct both the production defect and the proof system that allowed the false PASS.
- Re-run terminal-path/full-system readiness checks when they can be affected.
- Run the complete terminal verification sequence after affected sections are green.
- Rerun the terminal machine release gate.
- Produce a corrected exact head and perform a new independent exact-head audit.
- Do not substitute local commands for mandatory exact-head CI.
- If controlled code verification passes but a mandatory external release condition remains unavailable, report `CODE VERIFIED / GOVERNANCE HOLD`.
- Do not merge, deploy, release, or activate without required authorization.
