from Assignments.Assignment1.exceptions import NegativeBalanceException


class User:
    def __init__(self, name, age, acc_number, bank_name, bank_balance, all_budgets):
        """
        Initialize the user object
        :param name: (String) The name of the user
        :param age: (int) The age of the user
        :param acc_number: (String) The bank account number of the user
        :param bank_name: (String) User's bank name
        :param bank_balance: (int) The user's current bank balance
        :param all_budgets: (AllBudgets) Budgets allocated for all categories
        """
        self.name = name
        self.age = age
        self.acc_number = acc_number
        self.bank_name = bank_name
        self.bank_balance = bank_balance
        self.all_budgets = all_budgets

    def print_all_budgets(self):
        """
        Print all budgets category-wise
        """
        print(self.all_budgets)

    def view_bank_details(self):
        """
        Print all the bank account details along with all the transactions made by the user.
        """
        print(f'\nBank {self.bank_name}')
        print(f'Account number: {self.acc_number}')
        self.all_budgets.print_all_transactions()
        print(f'Closing balance: {self.bank_balance}\n')

    def warn_and_notify(self, budget):
        """
        This method is executed every time the user attempts to make a transaction. Here, we warn or notify the user if
        the requirements of that user is met. (Different for all users, determined by the instance variable of the
        subclass.
        :param budget: Budget object, to check the amount and category of budget
        """

        # Save the budget details
        spent = budget.amount_spent
        tot_budget = budget.total_budget

        percent_spent = spent/tot_budget * 100

        # If the money spent by the user exceeds the limit as specified by subclass, lock the category for user
        if percent_spent > self.lock_out_point:
            budget.lock()
            self.all_budgets.check_for_lockout(self)  # Check if the user is to be locked out of all categories

        # If the money spent by the user exceeds the warning limit as specified by subclass, notify the user
        elif percent_spent >= self.warning_point:
            # Check if user is to be notified politely or not
            if self.notify_polite is True:
                print(f'WARNING: EXCEEDED {self.warning_point}% OF THIS BUDGET!!')
            else:
                print(f'WARNING: EXCEEDED {self.warning_point}% OF THIS BUDGET!!\n' * 10)

    def update_bank_balance(self, amt):
        """
        Subtract the transaction amount from bank account
        :param amt: Transaction amount
        :raises NegativeBalanceException if the transaction amount is greater than bank balance
        """
        if amt > self.bank_balance:
            raise NegativeBalanceException("You don't have enough money for this transaction.\n")

        self.bank_balance -= amt
