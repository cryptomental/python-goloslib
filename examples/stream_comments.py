from golosapi.golosnoderpc import GolosNodeRPC
from pprint import pprint

rpc = GolosNodeRPC("wss://node.golos.ws")

for a in rpc.stream("comment"):
    pprint(a)
