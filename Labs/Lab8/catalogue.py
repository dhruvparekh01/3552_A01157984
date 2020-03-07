from Labs.Lab8.book import Book
from Labs.Lab8.dvd import Dvd
from Labs.Lab8.factories import JournalFactory
from Labs.Lab8.journal import Journal
from Labs.Lab8.lib_item_generator import LibraryItemGenerator


class Catalogue:
    def __init__(self):
        """
        Initialize the catalogue with a list of books.
        """
        self.items_list = LibraryItemGenerator.generate_test_items()

    def retrieve_item_by_call_number(self, call_num):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the catalogue.
        :param call_num: a string
        :return: catalogue_item object if found, None otherwise
        """
        found_item = None
        for item in self.items_list:
            if item.call_num == call_num:
                found_item = item
                break
        return found_item

    def add_item(self):
        """
        Add a brand new item to the catalogue with a unique call number.
        """
        item_type = int(input('1) Book\n2) Journal\n3) DVD\n'))

        new_item = JournalFactory().create_catalogue_item()
        self.items_list.append(new_item)

        # if item_type == 1:
        #     title = input("Enter title: ")
        #     author = input("Enter Author Name: ")
        #     new_item = Book(call_num, title, num_copies, author)
        #
        # elif item_type == 2:
        #     name = input("Enter name: ")
        #     issue = input("Enter issue number: ")
        #     pub = input("Enter publisher name: ")
        #     new_item = Journal(call_num, name, issue, pub, num_copies)
        #
        # elif item_type == 3:
        #     title = input("Enter title: ")
        #     release = input("Enter release date: ")
        #     reg_code = input("Enter registration code: ")
        #     new_item = Dvd(call_num, release, reg_code, num_copies, title)
        #
        # else:
        #     print("Invalid input")
        #     return

        # found_item = self.retrieve_item_by_call_number(call_num)
        #
        # if found_item:
        #     print(f"Could not add item with call number "
        #           f"{new_item.call_num}. It already exists. ")
        # else:
        #     self.items_list.append(new_item)
        #     print("book added successfully! book details:")
        #     print(new_item)

    def remove_item(self, call_num):
        """
        Remove an existing item from the catalogue
        :param call_num: a string
        :precondition call_number: a unique identifier
        """
        found_item = self.retrieve_item_by_call_number(call_num)
        if found_item:
            self.items_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_num}")
        else:
            print(f"book with call number: {call_num} not found.")

    def reduce_item_count(self, call_num):
        """
        Decrement the item count for an item with the given call number
        in the catalogue.
        :param call_num: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count decremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_num)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_item_count(self, call_num):
        """
        Increment the item count for an book with the given call number
        in the catalogue.
        :param call_num: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_num)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def display_available_items(self):
        """
        Display all the items in the catalogue.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for library_book in self.items_list:
            print(library_book)

