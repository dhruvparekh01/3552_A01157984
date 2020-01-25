import abc


class CatalogueItem(abc.ABC):
    """
    Abstract class to represent all catalogue items
    """
    def __init__(self, num_copies, call_num, title):
        """
        Initialize the catalogue item
        :param num_copies: int
        :param call_num: String
        """
        self.no_of_copies = num_copies
        self.call_num = call_num
        self.title = title

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        if self.no_of_copies > 0:
            return True
        else:
            return False

    def get_title(self):
        return self.title

    def decrement_number_of_copies(self):
        self.no_of_copies -= 1

    def increment_number_of_copies(self):
        self.no_of_copies += 1

