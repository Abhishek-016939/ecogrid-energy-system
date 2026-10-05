import pytest

from services.marketplace.app import create_trade


def test_trade_is_pending_settlement():
    trade = create_trade("S1", "B1", 5, 0.2)
    assert trade["status"] == "PENDING_SETTLEMENT"
    assert trade["amount"] == 1.0


def test_invalid_quantity_rejected():
    with pytest.raises(ValueError):
        create_trade("S1", "B1", 0, 0.2)
