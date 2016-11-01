from steemapi.steemasyncclient import SteemAsyncClient, Config


class GolosAsyncClient(SteemAsyncClient):
    """ Golos Asynchronous Client

        The ``GolosAsyncClient`` class is an abstraction layer that makes asynchronous
        use of the RPC API of either golosd (witness) or cli_wallet (wallet)  easy to use.

        :param class config: the configuration class

        Example usage of this class:

        .. code-block:: python

            from golosasyncclient import GolosAsyncClient, Config

            @asyncio.coroutine
            def print_block_number(golos):
               res = yield from golos.database.get_dynamic_global_properties()
               print(res["head_block_number"])

            golos = GolosAsyncClient(Config(witness_url="ws://localhost:8090",
                                            witness_apis=["database"]))
            golos.run([print_block_number])

        See more examples of how to use this class in the examples folder.
    """
    def __init__(self, config):
        super(GolosAsyncClient, self).__init__(config)
