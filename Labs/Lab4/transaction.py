class Transaction:
    def __init__(self, time, amt, src):
        """
        Instantiate a transaction with the time, amount and source
        :param time: (datetime object) The time of recording the transaction
        :param amt: (int) the transaction amount
        :param src: The place or website the transaction was carried out
        """
        self.time = time
        self.amount = amt
        self.purchase_source = src

    def __str__(self):
        return f'Time: {self.time}\nAmount: {self.amount}\nSource: {self.purchase_source}'
