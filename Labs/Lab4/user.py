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
        :return:
        """
        print(self.all_budgets)
