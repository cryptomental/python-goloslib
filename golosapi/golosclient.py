from steemapi.steemclient import SteemClient


class GolosClient(SteemClient):
    """ The ``GolosClient`` class is an abstraction layer that makes the use
        of the RPC and the websocket interface easier to use. A part of this
        abstraction layer is to simplify the usage of objects and have
        an internal objects map updated to reduce unnecessary queries
        (for enabled websocket connections). Advanced developers are of
        course free to use the underlying API classes instead as well.

        :param class config: the configuration class

        If a websocket connection is configured, the websocket subsystem
        can be run by:

        .. code-block:: python

            golos = GolosClient(config)
            golos.run()
    """
    def __init__(self, config, **kwargs):
        super(GolosClient, self).__init__(config, **kwargs)
