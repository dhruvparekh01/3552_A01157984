class Budget:
    def __init__(self, total):
        """
        Initialize a budget for a particular category
        """
        self.total_budget = total
        self.amount_spent = 0
        self.status_locked = False
        self.transactions = list()

    def __str__(self):
        s = f'Current status: Locked-{self.status_locked}\nAmount spent: {self.amount_spent}\n' \
            f'Amount Left: {self.total_budget-self.amount_spent}\nTotal amount allocated: {self.total_budget}'

        return s

    def add_transactions(self, tran):
        """
        Add a transaction to this category
        :param tran: A Transaction object
        """
        self.transactions.append(tran)
        print('Transaction recorded!')

    def print_transactions(self):
        """
        Print all the transactions of this category
        """
        for i in self.transactions:
            print('\nTransaction:')
            print(i, '\n')
