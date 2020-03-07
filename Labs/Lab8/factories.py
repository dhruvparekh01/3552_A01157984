from Labs.Lab8.book import Book
from Labs.Lab8.dvd import Dvd
from Labs.Lab8.journal import Journal


class CatalogueItemFactory:
    def create_catalogue_item(self):
        kwargs = {'call_num': input("Enter Call Number: \n")}
        num_copies = int(input("Enter number of copies (positive number): \n"))
        name = input("Enter name: ")
        kwargs.update({'num_copies': num_copies})
        kwargs.update({'name': name})
        return kwargs


class JournalFactory(CatalogueItemFactory):
    def create_catalogue_item(self):
        kwargs = super().create_catalogue_item()
        issue = input("Enter issue number: ")
        pub = input("Enter publisher name: ")
        new_item = Journal(issue_no=issue, pub=pub, **kwargs)
        return new_item


class BookFactory(CatalogueItemFactory):
    def create_catalogue_item(self):
        kwargs = super().create_catalogue_item()
        author = input("Enter Author Name: ")
        new_item = Book(author=author, **kwargs)
        return new_item


class DvdFactory(CatalogueItemFactory):
    def create_catalogue_item(self):
        kwargs = super().create_catalogue_item()
        release = input("Enter release date: ")
        reg_code = input("Enter registration code: ")
        new_item = Dvd(release=release, reg_code=reg_code, **kwargs)
        return new_item
