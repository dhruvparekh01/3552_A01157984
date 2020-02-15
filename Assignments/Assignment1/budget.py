from Assignments.Assignment1.exceptions import NegativeBalanceException


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

    def add_transactions(self, tran, user):
        """
        Add a transaction to this category
        :param tran: A Transaction object
        :param user The user requesting the transaction
        """
        # Check if user is completely locked out
        if user.all_budgets.status_locked:
            print('You are completely locked out and cannot spend any more money!!\n')
            return

        # Check if user is locked out of this category
        if self.status_locked:
            print('Transaction cannot be added. You are locked out of this category\n')
            return

        self.amount_spent += tran.amount

        try:
            user.update_bank_balance(tran.amount)
        except NegativeBalanceException as e:
            print('Transaction cannot be recorded.')
            print(e.args[0])
            return

        self.transactions.append(tran)
        print('Transaction recorded!')
        user.warn_and_notify(self)  # Check if this transactions caused any warnings or notifications.

    def print_transactions(self):
        """
        Print all the transactions of this category
        """
        for i in self.transactions:
            print('\nTransaction:')
            print(i, '\n')

    def lock(self):
        """
        Lock the user out of this category
        """
        print('You are locked out of spending any more money in this category\n')
        self.status_locked = True
