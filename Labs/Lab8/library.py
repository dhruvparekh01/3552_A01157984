""" This module houses the library"""
import difflib
from Labs.Lab8.catalogue import Catalogue


class Library:
    """
    The Library consists of a list of items and provides an
    interface for users to check out, return and find items.
    """
    def __init__(self):
        """
        Initialize the library with a list of items.
        """
        self.catalogue = Catalogue()

    def check_out(self, call_num):
        """
        Check out an item with the given call number from the library.
        :param call_num: a string
        :precondition call_number: a unique identifier
        """
        library_item = self.catalogue.retrieve_item_by_call_number(call_num)
        if library_item.check_availability():
            status = self.catalogue.reduce_item_count(call_num)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_num}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_num}"
                  f". Checkout failed.")

    def return_item(self, call_num):
        """
        Return an item with the given call number from the library.
        :param call_num: a string
        :precondition call_number: a unique identifier
        """
        status = self.catalogue.increment_item_count(call_num)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_num}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove a item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.catalogue.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the book")
                self.catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = [item.get_title() for item in self.catalogue.items_list]
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    my_epic_library = Library()
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
