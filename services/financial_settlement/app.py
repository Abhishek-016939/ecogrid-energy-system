from services.financial_settlement.internals import record_ledger_entry

_processed = {}


def settle_trade(trade_id, amount, gateway):
    key = f"{trade_id}-PAYMENT"
    if key in _processed:
        return _processed[key]
    if not gateway(key, amount):
        return {"trade_id": trade_id, "idempotency_key": key, "status": "FAILED"}
    record_ledger_entry(trade_id, amount)
    result = {"trade_id": trade_id, "idempotency_key": key, "status": "SETTLED"}
    _processed[key] = result
    return result
