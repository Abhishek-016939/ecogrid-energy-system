def create_trade(seller_id, buyer_id, quantity_kwh, price_per_kwh):
    if quantity_kwh <= 0 or price_per_kwh <= 0:
        raise ValueError("quantity and price must be positive")
    return {
        "event": "TradeMatched",
        "seller_id": seller_id,
        "buyer_id": buyer_id,
        "quantity_kwh": quantity_kwh,
        "amount": round(quantity_kwh * price_per_kwh, 2),
        "status": "PENDING_SETTLEMENT",
    }
