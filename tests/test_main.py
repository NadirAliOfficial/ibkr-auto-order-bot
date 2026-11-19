import pytest
from ib_insync import MarketOrder

def test_market_order_buy_one():
    """Ensure a BUY MarketOrder for 1 share is created with correct attributes."""
    order = MarketOrder('BUY', 1)
    assert order.action == 'BUY'
    assert order.totalQuantity == 1
    assert order.orderType == 'MKT'
