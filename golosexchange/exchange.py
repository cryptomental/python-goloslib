from steemexchange.exchange import ExampleConfig, InvalidWifKey, WifNotActive, SteemExchange


class GolosExchange(SteemExchange):
    """ This class serves as an abstraction layer for the decentralized
        exchange within the network and simplifies interaction for
        trading bots.

        :param config config: Configuration Class, similar to the
                              example above

        This class tries to map the poloniex API around the DEX but has
        some differences:

            * market pairs are denoted as 'quote'_'base', e.g. `USD_BTS`
            * Prices/Rates are denoted in 'base', i.e. the USD_BTS market
              is priced in BTS per USD.
              Example: in the USD_BTS market, a price of 300 means
              a USD is worth 300 BTS
            * All markets could be considered reversed as well ('BTS_USD')

        Usage:

        .. code-block:: python

            from golosexchange import GolosExchange
            from pprint import pprint

            class Config():
                wallet_host           = "localhost"
                wallet_port           = 8092
                witness_url           = "ws://localhost:8090/"
                account = "xeroc"

            golos = GolosExchange(Config)
            pprint(steem.buy(10, "GBG", 100))
            pprint(steem.sell(10, "GBG", 100))
            pprint(steem.returnTicker())
            pprint(steem.return24Volume())
            pprint(steem.returnOrderBook(2))
            pprint(steem.ws.get_order_book(10, api="market_history"))
            pprint(steem.returnTradeHistory())
            pprint(steem.returnMarketHistoryBuckets())
            pprint(steem.returnMarketHistory(300))
            pprint(steem.get_lowest_ask())
            pprint(steem.get_highest_bid())
    """
    # Available Assets
    assets = ["GOLOS", "GBG"]

    def __init__(self, config, **kwargs):
        super(GolosExchange, self).__init__(config, **kwargs)
        self.prefix = "GLS"

    def _get_asset(self, symbol):
        """ Return the properties of the assets tradeable on the
            network.

            :param str symbol: Symbol to get the data for (i.e. GOLOS, GBG, GESTS)
        """
        if symbol == "GOLOS":
            return {"symbol": "GOLOS",
                    "precision": 3
                    }
        elif symbol == "GBG":
            return {"symbol": "GBG",
                    "precision": 3
                    }
        elif symbol == "GESTS":
            return {"symbol": "GESTS",
                    "precision": 6
                    }
        else:
            return None

    def returnTicker(self):
        """ Returns the ticker for all markets.

            Output Parameters:

            * ``latest``: Price of the order last filled
            * ``lowest_ask``: Price of the lowest ask
            * ``highest_bid``: Price of the highest bid
            * ``sbd_volume``: Volume of GBG
            * ``steem_volume``: Volume of GOLOS
            * ``percent_change``: 24h change percentage (in %)

            .. note::

                All prices returned by ``returnTicker`` are in the **reversed**
                orientation as the market. I.e. in the GBG:GOLOS market, prices are
                GOLOS per GBG. That way you can multiply prices with `1.05` to
                get a +5%.

            Sample Output:

            .. code-block:: js

                {'GBG:GOLOS': {'highest_bid': 3.3222341219615097,
                               'latest': 1000000.0,
                               'lowest_ask': 3.0772668228742615,
                               'percent_change': -0.0,
                               'sbd_volume': 108329611.0,
                               'steem_volume': 355094043.0},
                 'GOLOS:GBG': {'highest_bid': 0.30100226633322913,
                               'latest': 0.0,
                               'lowest_ask': 0.3249636958897082,
                               'percent_change': 0.0,
                               'sbd_volume': 108329611.0,
                               'steem_volume': 355094043.0}}
        """
        ticker = {}
        t = self.ws.get_ticker(api="market_history")
        ticker["GOLOS:GBG"] = {'highest_bid': float(t['highest_bid']),
                               'latest': float(t["latest"]),
                               'lowest_ask': float(t["lowest_ask"]),
                               'percent_change': float(t["percent_change"]),
                               'sbd_volume': t["sbd_volume"],
                               'steem_volume': t["steem_volume"]}
        ticker["GBG:GOLOS"] = {'highest_bid': 1.0 / float(t['highest_bid']),
                               'latest': 1.0 / (float(t["latest"]) or 1e-6),
                               'lowest_ask': 1.0 / float(t["lowest_ask"]),
                               'percent_change': -float(t["percent_change"]),
                               'sbd_volume': t["sbd_volume"],
                               'steem_volume': t["steem_volume"]}
        return ticker

    def return24Volume(self):
        """ Returns the 24-hour volume for all markets, plus totals for primary currencies.

            Sample output:

            .. code-block:: js

                {'sbd_volume': 108329.611, 'steem_volume': 355094.043}

        """
        v = self.ws.get_volume(api="market_history")
        return {'gbg_volume': v["sbd_volume"],
                'golos_volume': v["steem_volume"]}

    def returnOrderBook(self, limit=25):
        """ Returns the order book for the GBG/GOLOS markets in both orientations.

            :param int limit: Limit the amount of orders (default: 25)

            Market is GBG:GOLOS and prices are GOLOS:MARKET

            Sample output:

            .. code-block:: js

                {'asks': [{'price': 3.086436224481787,
                           'gbg': 318547,
                           'golos': 983175},
                          {'price': 3.086429621198315,
                           'gbg': 2814903,
                           'golos': 8688000}],
                 'bids': [{'price': 3.0864376216446257,
                           'gbg': 545133,
                           'golos': 1682519},
                          {'price': 3.086440512632327,
                           'gbg': 333902,
                           'golos': 1030568}]},
        """
        orders = self.ws.get_order_book(limit, api="market_history")
        r = {"asks": [], "bids": []}
        for side in ["bids", "asks"]:
            for o in orders[side]:
                r[side].append({
                    'price': float(o["price"]),
                    'gbg': o["sbd"] / 10 ** 3,
                    'golos': o["steem"] / 10 ** 3,
                })
        return r

    def returnBalances(self):
        """ Return GBG and GOLOS balance of the account
        """
        # riverhead - July 19. 2016
        balances = {}
        result = self.ws.get_account(self.config.account)
        balances["GOLOS"] = result['balance']
        balances["GBG"] = result['sbd_balance']
        return balances
