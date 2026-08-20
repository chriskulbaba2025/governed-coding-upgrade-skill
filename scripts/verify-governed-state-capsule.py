#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "GOVERNED_STATE_CAPSULE.md"
SCHEMA = ROOT / "schemas" / "governed_state_capsule.schema.json"
TEMPLATE = ROOT / "templates" / "GOVERNED_STATE_CAPSULE_TEMPLATE.json"
GLOBAL = ROOT / "GLOBAL_AGENT_RULE.md"
WORKSPACE = ROOT / "templates" / "CHANGE_WORKSPACE_TEMPLATE.md"

CONTRACT = "gcu-state-capsule/1.0.0"
SECRET_TOKENS = ("secret", "password", "credential", "api_key", "apikey", "token_value")


def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {message}")


def read_json(path: Path) -> dict:
    require(path.is_file(), f"required file exists: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: invalid JSON in {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
        raise SystemExit(1)


def validate_capsule(capsule: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    missing = [key for key in required if key not in capsule]
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    unknown = sorted(set(capsule) - set(properties))
    if schema.get("additionalProperties") is False and unknown:
        errors.append(f"unknown fields: {', '.join(unknown)}")

    if capsule.get("contract") != CONTRACT:
        errors.append("contract mismatch")

    if not capsule.get("contextManifest"):
        errors.append("contextManifest must be non-empty")

    valid = set(capsule.get("validProofRefs", []))
    invalid = set(capsule.get("invalidatedProofRefs", []))
    overlap = sorted(valid & invalid)
    if overlap:
        errors.append(f"proof refs cannot be both valid and invalidated: {', '.join(overlap)}")

    if capsule.get("executionState") == "CLOSED" and capsule.get("nextObligation") is not None:
        errors.append("closed capsule must not advertise a next obligation")

    if capsule.get("phase") == "CLOSED" and capsule.get("executionState") != "CLOSED":
        errors.append("CLOSED phase requires CLOSED executionState")

    blocking = [item for item in capsule.get("unresolved", []) if item.get("blocking") is True]
    if blocking and capsule.get("executionState") == "READY":
        errors.append("blocking unresolved items cannot coexist with READY executionState")

    for key in capsule:
        lowered = key.lower()
        if any(token in lowered for token in SECRET_TOKENS):
            errors.append(f"secret-like field name prohibited: {key}")

    return errors


def capsule_is_stale(capsule: dict, repository_sha: str) -> bool:
    return capsule.get("currentSha") != repository_sha


def require_phrases(path: Path, phrases: tuple[str, ...]) -> None:
    require(path.is_file(), f"required file exists: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for phrase in phrases:
        require(phrase in text, f"{path.name} contains: {phrase}")


def main() -> int:
    schema = read_json(SCHEMA)
    template = read_json(TEMPLATE)

    require(schema.get("properties", {}).get("contract", {}).get("const") == CONTRACT,
            "schema pins canonical state-capsule contract")
    require(schema.get("additionalProperties") is False,
            "schema rejects undeclared state fields")

    errors = validate_capsule(template, schema)
    require(not errors, f"template satisfies state-capsule invariants ({'; '.join(errors) if errors else 'clean'})")

    stale = copy.deepcopy(template)
    stale["currentSha"] = "aaaaaaa"
    require(capsule_is_stale(stale, "bbbbbbb"),
            "resume guard detects stale capsule SHA")

    overlap = copy.deepcopy(template)
    overlap["validProofRefs"] = ["P-001"]
    overlap["invalidatedProofRefs"] = ["P-001"]
    require(any("both valid and invalidated" in err for err in validate_capsule(overlap, schema)),
            "proof-cache contradiction is rejected")

    blocked = copy.deepcopy(template)
    blocked["unresolved"] = [{"id": "U-001", "claim": "material causal fact", "blocking": True}]
    blocked["executionState"] = "READY"
    require(any("blocking unresolved" in err for err in validate_capsule(blocked, schema)),
            "blocking unresolved state cannot masquerade as READY")

    closed = copy.deepcopy(template)
    closed["phase"] = "CLOSED"
    closed["executionState"] = "CLOSED"
    closed["nextObligation"] = "CHG-99"
    require(any("closed capsule" in err for err in validate_capsule(closed, schema)),
            "closed state cannot advertise additional work")

    require_phrases(DOC, (
        CONTRACT,
        "Resume-first rule",
        "contextManifest",
        "do not re-investigate",
        "derived index",
        "exact-head terminal CI",
    ))
    require_phrases(GLOBAL, (
        CONTRACT,
        "STATE.json",
        "contextManifest",
        "do not re-investigate",
    ))
    require_phrases(WORKSPACE, (
        "STATE.json",
        CONTRACT,
        "contextManifest",
        "nextObligation",
    ))

    print("PASS: GCU governed state capsule contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
