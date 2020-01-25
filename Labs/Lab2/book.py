from Labs.Lab2.catalogue_item import CatalogueItem


class Book(CatalogueItem):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, call_num, title, num_copies, author):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(num_copies, call_num, title)
        self._author = author

    def get_author(self):
        return self._author

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.no_of_copies}\n" \
               f"Author: {self._author}"
