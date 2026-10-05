from services.financial_settlement import internals
from services.financial_settlement.app import settle_trade


def gateway_ok(key, amount):
    return True


def test_duplicate_event_creates_one_ledger_entry():
    internals.LEDGER.clear()
    settle_trade("TRD-1", 10.0, gateway_ok)
    settle_trade("TRD-1", 10.0, gateway_ok)
    assert len(internals.LEDGER) == 1


def test_failed_gateway_creates_no_ledger_entry():
    internals.LEDGER.clear()
    result = settle_trade("TRD-9", 10.0, lambda key, amount: False)
    assert result["status"] == "FAILED"
    assert internals.LEDGER == []


def test_simulated_settlement_success_rate():
    results = [settle_trade(f"TRD-{i}", 5.0, gateway_ok) for i in range(1000)]
    rate = sum(r["status"] == "SETTLED" for r in results) / len(results)
    assert rate >= 0.999
