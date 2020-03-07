from Labs.Lab8.book import Book
from Labs.Lab8.dvd import Dvd
from Labs.Lab8.journal import Journal


class LibraryItemGenerator:
    """
    Static class to populate the catalogue with dummy data
    """
    @staticmethod
    def generate_test_items():
        """
        Return a list of items with dummy data.
        :return: a list of CatalogueItem objects
        """
        item_list = [
            Book("J K Rowling", call_num="100.200.300", name="Harry Potter 1", num_copies=2 ),
            Book(call_num="999.224.854", name="Harry Potter 2", num_copies=5, author="J K Rowling"),
            Book(call_num="631.495.302", name="Harry Potter 3", num_copies=4, author="J K Rowling"),
            Book(call_num="123.02.204", name="The Cat in the Hat", num_copies=1, author="Dr. Seuss"),
            Journal(call_num="1.2.3", name="Journal 1", issue_no=122, pub="Publisher 1", num_copies=3),
            Dvd(call_num="1.3.5", release="01/01/01", reg_code=122, num_copies=2, name="Movie 1")
        ]
        return item_list

