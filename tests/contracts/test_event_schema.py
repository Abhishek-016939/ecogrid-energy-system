import json
from pathlib import Path

from jsonschema import validate

from services.smart_meter_integration.app import build_surplus_event

SCHEMA = json.loads(Path("contracts/surplus_energy_available.v1.json").read_text())


def test_event_matches_contract_v1():
    event = build_surplus_event("M1025", "2026-10-04T10:00Z", 4.8)
    validate(instance=event, schema=SCHEMA)
