from library.library import Library
from library.logger_config import setup_logger


def display_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Exit")


def main():
    setup_logger()
    lib = Library()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ")
                author = input("Enter Author Name: ")
                lib.add_book(book_id, title, author)
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to remove: "))
                lib.remove_book(book_id)
                print("Book removed successfully.")
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to issue: "))
                if lib.issue_book(book_id):
                    print("Book issued successfully.")
                else:
                    print("Book not available or not found.")
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "4":
            try:
                book_id = int(input("Enter Book ID to return: "))
                if lib.return_book(book_id):
                    print("Book returned successfully.")
                else:
                    print("Book not found.")
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "5":
            books = lib.view_books()
            if not books:
                print("No books available.")
            else:
                print("\nAvailable Books:")
                for book in books:
                    status = "Available" if book.available else "Issued"
                    print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Status: {status}")

        elif choice == "6":
            print("Exiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1-6.")


if __name__ == "__main__":
    main()