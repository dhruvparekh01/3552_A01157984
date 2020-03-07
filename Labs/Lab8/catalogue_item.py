import abc


class CatalogueItem(abc.ABC):
    """
    Abstract class to represent all catalogue items
    """
    def __init__(self, **kwargs):
        """
        Initialize the catalogue item
        :param num_copies: int
        :param call_num: String
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
        if self.num_copies > 0:
            return True
        else:
            return False

    @property
    def title(self): return self.name

    def decrement_number_of_copies(self):
        self.num_copies -= 1

    def increment_number_of_copies(self):
        self.num_copies += 1

