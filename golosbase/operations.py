from steembase.operations import  (Operation, Permission, Memo, Vote, Comment,
                                   Exchange_rate, Witness_props, Account_create,
                                   Account_update, Transfer, Transfer_to_vesting,
                                   Withdraw_vesting, Limit_order_create,
                                   Limit_order_cancel, Set_withdraw_vesting_route,
                                   Convert, Feed_publish, Witness_update,
                                   Transfer_to_savings, Transfer_from_savings,
                                   Cancel_transfer_from_savings)

from steembase.operations import Amount as SteemAmount

prefix = "GLS"


class Amount(SteemAmount):
    def __init__(self, d):
        self.amount, self.asset = d.strip().split(" ")
        self.amount = float(self.amount)

        if self.asset == "GOLOS":
            self.precision = 3
        elif self.asset == "GESTS":
            self.precision = 6
        elif self.asset == "GBG":
            self.precision = 3
        else:
            raise Exception("Asset unknown")
