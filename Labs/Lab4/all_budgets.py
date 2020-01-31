import datetime

from Labs.Lab4.transaction import Transaction


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

    def add_transaction(self):
        """
        Add a transaction to the budget of particular category
        """
        time = datetime.datetime.now()
        amt = int(input('Enter the amount\n'))
        src = input('Enter the source of purchase\n')
        choice = int(input('Category:\n1) Games and Entertainment\n2) Clothing and Accessories\n3) Eating Out'
                           '\n4) Miscellaneous\n'))

        temp = Transaction(time, amt, src)

        if choice == 1:
            self.games_budget.add_transactions(temp)
        elif choice == 2:
            self.clothing_budget.add_transactions(temp)
        elif choice == 3:
            self.eating_budget.add_transactions(temp)
        elif choice == 4:
            self.misc_budget.transctions.append(temp)
        else:
            print('Invalid')

    def print_all_transactions(self):
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

