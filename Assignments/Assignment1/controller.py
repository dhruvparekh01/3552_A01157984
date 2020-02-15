"""
Entry point of application
"""
from Assignments.Assignment1.all_budgets import AllBudgets
from Assignments.Assignment1.budget import Budget
from Assignments.Assignment1.user_types import Angel, Troublemaker, Rebel


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
        :raises InvalidChoiceException if user inputs invalid character(s)
        """
        try:
            name = input('Enter the user name: ')
            age = int(input('Enter the user age: '))
            acc_number = input('Enter the account number: ')
            bank_name = input('Enter the bank name: ')
            bal = float(input('Enter the current bank balance: '))
            games = float(input('Enter games and entertainment budget: '))
            clothing = float(input('Enter clothing and accessories budget: '))
            eating = float(input('Enter eating out budget: '))
            misc = float(input('Enter miscellaneous budget: '))
        except ValueError:
            print('Invalid number entered. Please enter all details again')
            return self.add_user()

        budgets = AllBudgets(Budget(games), Budget(clothing), Budget(eating), Budget(misc))

        new_user = None
        while True:
            category = input('1. Angel\n2. Troublemaker\n3. Rebel\n').strip()

            if category == '1':
                new_user = Angel(name, age, acc_number, bank_name, bal, budgets)
                break
            elif category == '2':
                new_user = Troublemaker(name, age, acc_number, bank_name, bal, budgets)
                break
            elif category == '3':
                new_user = Rebel(name, age, acc_number, bank_name, bal, budgets)
                break
            else:
                print('Invalid option: your input cannot be greater than 3')

        self.users.append(new_user)
        return new_user

    @staticmethod
    def load_test_user():
        """
        Static method to add a test user
        :return: A user object
        """
        dummy_budgets = AllBudgets(Budget(50), Budget(60), Budget(80), Budget(40))
        dummy = Rebel('Jon', 10, '1111', 'RBC', 500, dummy_budgets)
        return dummy


if __name__ == '__main__':
    controller = Controller()

    temp = input('1) New user\n2) Test user\n')

    if temp == '1':
        test_user = controller.add_user()
    elif temp == '2':
        test_user = Controller.load_test_user()
    else:
        print('No valid choice entered. Add a new user')  # if the user entered an invalid choice, default to new user
        test_user = controller.add_user()

    while True:
        choice = input('1) View Budgets\n2) Record a transaction\n3) View transactions by budget\n'
                       '4) View bank account details\n5) Exit\n').strip()

        if choice == '1':
            test_user.print_all_budgets()
        elif choice == '2':
            test_user.all_budgets.add_transaction(test_user)
        elif choice == '3':
            test_user.all_budgets.print_transactions_by_budget()
        elif choice == '4':
            test_user.view_bank_details()
        elif choice == '5':
            break
        else:
            print('Invalid option: your input cannot be greater than 5')
