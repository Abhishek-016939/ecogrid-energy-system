def process_meter_reading(reading):
    if reading.get("energy_kwh", -1) < 0:
        raise ValueError("invalid reading")
    return {
        "meter_id": reading["meter_id"],
        "energy_kwh": reading["energy_kwh"],
        "status": "VALIDATED",
    }


def build_surplus_event(meter_id, interval, surplus_kwh):
    return {
        "eventType": "SurplusEnergyAvailable",
        "version": 1,
        "meterId": meter_id,
        "interval": interval,
        "surplusKWh": surplus_kwh,
    }
