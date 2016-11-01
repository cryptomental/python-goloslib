from steembase.signedtransactions import Signed_Transaction as SteemSigned_Transaction


class Signed_Transaction(SteemSigned_Transaction) :
    """ Create a signed transaction and offer method to create the
        signature

        :param num refNum: parameter ref_block_num (see ``getBlockParams``)
        :param num refPrefix: parameter ref_block_prefix (see ``getBlockParams``)
        :param str expiration: expiration date
        :param Array operations:  array of operations
    """
    def __init__(self, *args, **kwargs):
        super(Signed_Transaction, self).__init__(*args, **kwargs)

    def sign(self, wifkeys, chain="GOLOS"):
        return super(Signed_Transaction, self).sign(wifkeys, chain)

    def verify(self, pubkeys=[], chain="GOLOS"):
        return super(Signed_Transaction, self).verify(pubkeys, chain)
