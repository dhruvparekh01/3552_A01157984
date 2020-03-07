from Labs.Lab8.catalogue_item import CatalogueItem


class Book(CatalogueItem):
    """
    Represents a single book in a library which is identified through
    it's call number.
    """

    def __init__(self, author, **kwargs):
        """
        :param author: a string
        :param **kwargs: see below

        :keyword Arguments:
            * *call_num* (```str```)
            * *title* (```str```)
            * *num_copies* (```int```)

        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(**kwargs)
        self._author = author

    @property
    def author(self): return self._author

    def __str__(self):
        return f"---- Book: {self.title()} ----\n" \
               f"Call Number: {self.call_num}\n" \
               f"Number of Copies: {self.num_copies}\n" \
               f"Author: {self._author}"
