from steemapi.steemnoderpc import SteemNodeRPC


class GolosNodeRPC(SteemNodeRPC):
    """ This class allows to call API methods synchronously, without
        callbacks. It logs in and registers to the APIs:

        * database
        * history

        :param str urls: Either a single Websocket URL, or a list of URLs
        :param str user: Username for Authentication
        :param str password: Password for Authentication
        :param Array apis: List of APIs to register to (default: ["database", "network_broadcast"])

        Available APIs

              * database
              * network_node
              * network_broadcast
              * history

        Usage:

        .. code-block:: python

            ws = GolosNodeRPC("ws://10.0.0.16:8090")
            print(ws.get_account_count())

    """
    def __init__(self,
                 urls,
                 user="",
                 password="",
                 **kwargs):
        super(GolosNodeRPC, self).__init__(urls, user, password, **kwargs)

    def get_asset(self, name):
        raise NotImplementedError  # We overwrite this method from graphenelib

    def getFullAccountHistory(self, account, begin=1, limit=100, sort="block"):
        raise NotImplementedError  # We overwrite this method from graphenelib

    def get_object(self, o):
        raise NotImplementedError  # We overwrite this method from graphenelib
