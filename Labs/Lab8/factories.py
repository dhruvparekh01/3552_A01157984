from Labs.Lab8.book import Book
from Labs.Lab8.dvd import Dvd
from Labs.Lab8.journal import Journal
from abc import ABC


class CatalogueItemFactory(ABC):
    """
    The base factory class that all the concrete factories extend.
    Makes a dictionary of the common attributes for all the concrete
    factories and return it. Enforces code reuse.
    """
    def create_catalogue_item(self):
        """
        Take user input for common attributes across all concrete factories
        :return a dictionary of arguments which can be used as keyword args
        """
        kwargs = {'call_num': input("Enter Call Number: \n")}
        try:
            num_copies = int(input("Enter number of copies (positive number): \n"))
        except ValueError:
            print('Invalid input. Number of copies set to default (1).')
            num_copies = 1
        name = input("Enter name: ")
        kwargs.update({'num_copies': num_copies})
        kwargs.update({'name': name})
        return kwargs


class JournalFactory(CatalogueItemFactory):
    """
    Concrete Journal Factory to instantiate Journal objects from user input.
    """
    def create_catalogue_item(self):
        """
        Create Journal object
        :return: Journal object
        """
        kwargs = super().create_catalogue_item()
        issue = input("Enter issue number: ")
        pub = input("Enter publisher name: ")
        new_item = Journal(issue_no=issue, pub=pub, **kwargs)
        return new_item


class BookFactory(CatalogueItemFactory):
    """
    Concrete Book Factory to instantiate Book objects from user input.
    """
    def create_catalogue_item(self):
        """
        Create Book object
        :return: Book object
        """
        kwargs = super().create_catalogue_item()
        author = input("Enter Author Name: ")
        new_item = Book(author=author, **kwargs)
        return new_item


class DvdFactory(CatalogueItemFactory):
    """
    Concrete Dvd Factory to instantiate Dvd objects from user input.
    """
    def create_catalogue_item(self):
        """
        Create Dvd object
        :return: Dvd object
        """
        kwargs = super().create_catalogue_item()
        release = input("Enter release date: ")
        reg_code = input("Enter registration code: ")
        new_item = Dvd(release=release, reg_code=reg_code, **kwargs)
        return new_item
