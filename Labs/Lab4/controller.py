"""
Entry point of application
"""
from Labs.Lab4.all_budgets import AllBudgets
from Labs.Lab4.budget import Budget
from Labs.Lab4.user import User


class Controller:
    """
    Controls the entire FAM system. Stores a list of users registered to the system.
    """
    def __init__(self):
        """
        Initialize the object with an empty list of users
        """
        self.users = list()

    def add_user(self):
        """
        Add a new user to the system by a series of prompts
        """
        name = input('Enter the user name')
        age = int(input('Enter the user age'))
        acc_number = input('Enter the account number')
        bank_name = input('Enter the bank name')
        bal = input('Enter the current bank balance')

        games = input('Enter games and entertainment budget')
        clothing = input('Enter clothing and accessories budget')
        eating = input('Enter eating out budget')
        misc = input('Enter miscellaneous budget')

        # budgets = AllBudgets(games, clothing, eating, misc)
        new_user = User(name, age, acc_number,bank_name, bal, budgets)
        self.users.append(new_user)

    @staticmethod
    def load_test_user():
        """
        Static method to add a test user
        :return: A user object
        """
        dummy_budgets = AllBudgets(Budget(50), Budget(60), Budget(80), Budget(40))
        dummy = User('Jon', 10, '1111', 'RBC', 500, dummy_budgets)
        return dummy


if __name__ == '__main__':
    controller = Controller()
    test_user = Controller.load_test_user()

    while True:
        choice = int(input('1) Add a transaction\n2) Show all transactions\n3) Exit\n'))

        if choice == 1:
            test_user.all_budgets.add_transaction()
        elif choice == 2:
            test_user.all_budgets.print_all_transactions()
        elif choice == 3:
            break
        else:
            print('Invalid Input.')
