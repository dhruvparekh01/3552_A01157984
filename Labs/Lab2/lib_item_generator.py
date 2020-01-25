from Labs.Lab2.book import Book
from Labs.Lab2.dvd import Dvd
from Labs.Lab2.journal import Journal


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
            Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
            Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
            Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
            Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
            Journal("1.2.3", "Journal 1", 122, "Publisher 1", 3),
            Dvd("1.3.5", "01/01/01", 122, 2, "Movie 1")

        ]
        return item_list

