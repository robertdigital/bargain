from datetime import timedelta
from operator import attrgetter

from bargain.currency import Currency


def test_get_candles(now, bitfinex):
    pair = (Currency.ETH, Currency.USD)
    interval = timedelta(hours=1)
    limit = 10

    candles = bitfinex.get_candles(pair, interval, now, limit)

    assert len(candles) == limit
    assert sorted(candles, key=attrgetter('time')) == candles


def test_get_ticker(bitfinex):
    pair = (Currency.ETH, Currency.USD)
    ticker = bitfinex.get_ticker(pair)
    assert ticker
