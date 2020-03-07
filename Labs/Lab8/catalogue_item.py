import abc


class CatalogueItem(abc.ABC):
    """
    Abstract class to represent all catalogue items
    """
    def __init__(self, **kwargs):
        """
        Initialize the catalogue item
        :param **kwargs: See below

        :keyword Arguments:
            * *call_num* (```str```)
            * *title* (```str```)
            * *num_copies* (```int```)

        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self.__dict__.update(kwargs)
        self.name = kwargs.get('name')
        self.call_num = kwargs.get('call_num')
        self.num_copies = kwargs.get('num_copies')

    def check_availability(self):
        """
        Returns True if the book is available and False otherwise
        :return: A Boolean
        """
        return self.num_copies > 0

    @property
    def title(self): return self.name

    def decrement_number_of_copies(self):
        self.num_copies -= 1

    def increment_number_of_copies(self):
        self.num_copies += 1

