import time

import pytest

from services.smart_meter_integration.app import process_meter_reading


def test_valid_reading():
    reading = {"meter_id": "M1", "energy_kwh": 1.2}
    assert process_meter_reading(reading)["status"] == "VALIDATED"


def test_negative_reading_rejected():
    with pytest.raises(ValueError):
        process_meter_reading({"meter_id": "M1", "energy_kwh": -1})


def test_processing_speed_guard():
    readings = [{"meter_id": f"M{i}", "energy_kwh": 1.0} for i in range(10_000)]
    start = time.perf_counter()
    for reading in readings:
        process_meter_reading(reading)
    assert time.perf_counter() - start < 1.0
