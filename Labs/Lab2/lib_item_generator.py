from Labs.Lab2.book import Book
from Labs.Lab2.journal import Journal


class LibraryItemGenerator:
    @staticmethod
    def generate(catalogue):
        while True:
            user_in = input("Enter 1 for Book\nEnter 2 for Journal\nEnter 3 for DVD")
            if user_in == 1:
                call_number = input("Enter Call Number: ")
                title = input("Enter title: ")
                num_copies = int(input("Enter number of copies "
                                       "(positive number): "))
                book_data = (call_number, title, num_copies)
                author = input("Enter Author Name: ")
                new_book = Book(book_data[0], book_data[1], book_data[2], author)

                found_book = catalogue._retrieve_book_by_call_number(new_book.call_number)
                if found_book:
                    print(f"Could not add book with call number "
                          f"{new_book.call_number}. It already exists. ")
                else:
                    self.catalogue.items_list.append(new_book)
                    print("book added successfully! book details:")
                    print(new_book)

            elif user_in == 2:
                issue_number = input("Enter Issue Number: ")
                name = input("Enter name: ")
                pub = input("Enter publisher: ")
                num_copies = int(input("Enter number of copies "
                                       "(positive number): "))
                new_journal = Journal(issue_number, name, pub, num_copies)

                found_journal = catalogue._retrieve_book_by_call_number(new_book.call_number)
                if found_book:
                    print(f"Could not add book with call number "
                          f"{new_book.call_number}. It already exists. ")
                else:
                    catalogue.items_list.append(new_book)
                    print("book added successfully! book details:")
                    print(new_book)

