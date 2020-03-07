from Labs.Lab8.factories import JournalFactory, BookFactory, DvdFactory
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

        new_item = None
        if item_type == 1:
            new_item = BookFactory().create_catalogue_item()
        elif item_type == 2:
            new_item = JournalFactory().create_catalogue_item()
        elif item_type == 3:
            new_item = DvdFactory().create_catalogue_item()
        else:
            print('Invalid choice')
            return

        self.items_list.append(new_item)

    def remove_item(self, call_num):
        """
        Remove an existing item from the catalogue
        :param call_num: a string
        :precondition call_number: a unique identifier
        """
        found_item = self.retrieve_item_by_call_number(call_num)
        if found_item:
            self.items_list.remove(found_item)
            print(f"Successfully removed {found_item.title()} with "
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

