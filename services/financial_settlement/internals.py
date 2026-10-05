LEDGER = []


def record_ledger_entry(trade_id, amount):
    LEDGER.append({"trade_id": trade_id, "amount": amount})
