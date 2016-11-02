********
Exchange
********

Quickstart
==========

.. code-block:: python

    from pprint import pprint
    from golosexchange import GolosExchange

    class Config():
        witness_url     = "wss://node.golos.ws"
        account         = "xeroc"
        # Either provide a cli-wallet RPC
        wallet_host     = "localhost"
        wallet_port     = 8092
        # or the (active) private key for your account
        wif             = ""

    golos = GolosExchange(Config)
    pprint(golos.buy(10, "GBG", 100))
    pprint(golos.sell(10, "GBG", 100))
    pprint(golos.cancel("24432422"))
    pprint(golos.returnTicker())
    pprint(golos.return24Volume())
    pprint(golos.returnOrderBook(2))
    pprint(golos.ws.get_order_book(10, api="market_history"))
    pprint(golos.returnTradeHistory())
    pprint(golos.returnMarketHistoryBuckets())
    pprint(golos.returnMarketHistory(300))
    pprint(golos.get_lowest_ask())
    pprint(golos.get_higest_bid())
    pprint(golos.transfer(10, "GBG", "fabian", "foobar"))

Definition
===========

.. autoclass:: golosexchange.exchange.GolosExchange
    :members:
