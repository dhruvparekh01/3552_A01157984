import datetime

from Assignments.Assignment1.transaction import Transaction


class AllBudgets:
    """
    A bridging class to decouple User and Budget. Stores all the different Budget objects for all categories.
    """

    def __init__(self, games, clothing, eating, misc):
        """
        Initialize the individual categorical budgets
        :param games: (Budget) Games and entertainment budget
        :param clothing: (Budget) Clothing and accessories budget
        :param eating: (Budget) Eating out budget
        :param misc: (Budget) Miscellaneous budget
        """
        self.games_budget = games
        self.clothing_budget = clothing
        self.eating_budget = eating
        self.misc_budget = misc
        self.status_locked = False

    def __str__(self):
        s = f'Games and Entertainment Budget\n{self.games_budget}\n\n' \
            f'Clothing and accessories Budget\n{self.clothing_budget}\n\n' \
            f'Eating out Budget\n{self.eating_budget}\n\n' \
            f'Miscellaneous Budget\n{self.misc_budget}\n\n'

        return s

    def add_transaction(self, user):
        """
        Add a transaction to the budget of particular category
        """

        # Check if the user is completely locked out
        if self.status_locked:
            print('Cannot add any transaction!! You are locked out of all categories\n')
            return

        time = datetime.datetime.now()

        try:
            amt = float(input('Enter the amount\n'))
        except ValueError:
            print('Please enter a valid number')
            self.add_transaction(user)

        src = input('Enter the source of purchase\n')
        choice = input('Category:\n1) Games and Entertainment\t2) Clothing and Accessories\t3) Eating Out'
                       '\t4) Miscellaneous\n')

        temp = Transaction(time, amt, src)

        if choice == '1':
            self.games_budget.add_transactions(temp, user)
        elif choice == '2':
            self.clothing_budget.add_transactions(temp, user)
        elif choice == '3':
            self.eating_budget.add_transactions(temp, user)
        elif choice == '4':
            self.misc_budget.add_transactions(temp, user)
        else:
            print('Invalid option: your input cannot be greater than 4. Please enter your choice again.')

    def print_transactions_by_budget(self):
        """
        Print all the transaction for the user category wise
        """
        print('----------------------------')
        print('Games and Entertainment')
        self.games_budget.print_transactions()
        print('----------------------------')
        print('Clothing and Accessories')
        self.clothing_budget.print_transactions()
        print('----------------------------')
        print('Eating Out')
        self.eating_budget.print_transactions()
        print('----------------------------')
        print('Miscellaneous')
        self.misc_budget.print_transactions()
        print('----------------------------')

    def print_all_transactions(self):
        """
        Print all transactions regardless of categories
        """
        self.games_budget.print_transactions()
        self.clothing_budget.print_transactions()
        self.eating_budget.print_transactions()
        self.misc_budget.print_transactions()

    def print_all_budgets(self):
        """
        Print all the budgets
        """
        print(self.games_budget)
        print(self.clothing_budget)
        print(self.eating_budget)
        print(self.misc_budget)

    def check_for_lockout(self, user):
        """
        Check if user is to be completely locked out. For the scope of this assignment, only the rebel can be
        completely locked out.
        """
        if self.status_locked is True:
            return

        count = 0

        if self.games_budget.status_locked:
            count += 1
        if self.clothing_budget.status_locked:
            count += 1
        if self.eating_budget.status_locked:
            count += 1
        if self.misc_budget.status_locked:
            count += 1

        if count >= user.complete_lockout:
            self.status_locked = True
            print("You have now been locked out of all the categories and cannot spend any more money\n")
