from Assignments.Assignment1.user import User

"""
Make all the user sub classes. These classes inherit from the User class and specify the warning and locking limits for
the user. 
"""


class Angel(User):
    def __init__(self, name, age, acc_number, bank_name, bank_balance, all_budgets):
        """
        Initializes a new user of type Angel
        """
        super().__init__(name, age, acc_number, bank_name, bank_balance, all_budgets)
        # Variable to set lock out point for this category. This is the percentage spending above which the user has to
        # be locked out of the category
        self.lock_out_point = 100000  # Very high lock out point makes sure this user is never locked out

        # Variable to set warning out point for this category. This is the percentage spending limit above which, the
        # user is warned.
        self.warning_point = 90

        # Specify if the user has to be notified politely or harshly
        self.notify_polite = True

        # Variable to set complete lock out limit for this category. This is the number of categories that the user
        # needs to be locked in, in order to be completely locked out
        self.complete_lockout = 5  # limit > 4 means this user is never locked out


class Troublemaker(User):
    def __init__(self, name, age, acc_number, bank_name, bank_balance, all_budgets):
        super().__init__(name, age, acc_number, bank_name, bank_balance, all_budgets)
        self.lock_out_point = 120
        self.warning_point = 75
        self.notify_polite = False
        self.complete_lockout = 5


class Rebel(User):
    def __init__(self, name, age, acc_number, bank_name, bank_balance, all_budgets):
        super().__init__(name, age, acc_number, bank_name, bank_balance, all_budgets)
        self.lock_out_point = 100
        self.warning_point = 50
        self.notify_polite = False
        self.complete_lockout = 2
