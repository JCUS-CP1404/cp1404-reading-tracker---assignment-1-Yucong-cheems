"""
Replace the contents of this module docstring with your own details
Name: YUCONG NI
Date started: 15/12/2022
GitHub URL:https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-1-Yucong-cheems/blob/master/assignment1.py
"""


import csv

FILENAME = "books.csv"


def main():
    """main function contains basic menu and options"""
    print("Reading Tracker 1.0 - by YUCONG NI")
    Menu = """Menu:\n L - List all books\n A - Add new book\n M - Mark a book as completed\n Q - Quit"""  # create menu
    book_list = load_books(FILENAME)
    print("{} books loaded".format(len(book_list)))
    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_books(book_list)
        elif choice == "A":
            add_books(book_list)
        elif choice == "M":
            mark_completed(book_list)
        else:
            print("Invalid input!")
        print(Menu)
        choice = input(">>> ").upper()

    with open("books.csv", "w", encoding="utf-8-sig", newline='') as book_data:
        books_writer = csv.writer(book_data)
        # create the writer
        for data in book_list:
            # write the data
            books_writer.writerow(data)

    print("See you next time!")


def load_books(filename):
    # read the file
    book_list = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            book_info = line.strip().split(",")
            book_list.append(book_info)
        in_file.close()
    return book_list


def add_books(book_list):
    # add new books
    title = add_title()
    author = add_author()
    pages = add_pages()
    new_book = [title, author, pages, "r"]
    book_list.append(new_book)
    print(f"{title} by {author}, ({pages}pages) added to Reading Tracker")


def add_pages():
    while True:
        try:
            page = int(input("pages: "))
        except ValueError:
            print("Invalid input; enter a valid number")
        if page < 0:
            print("Number must be > 0")
        else:
            return page


def add_author():
    book_author = input("Author: ")
    while len(book_author) == 0:
        print("Input can not be blank")
        book_author = input("Author: ")
    else:
        return book_author


def add_title():
    book_title = input("Title: ")
    while book_title.isdigit() == " " and len(book_title) == 0:
        print("Input can not be blank")
        book_title = input("Title: ")
    else:
        return book_title


def list_books(book_list):
    # list all books from the file as a standard form
    counted_page = 0
    counted_book = 0

    for i, book in enumerate(book_list):
        if book[3] == "c":
            print(f"*{i + 1:>2}. {book[0]:45} {'by ' + book[1]:30} {book[2]:>5} pages")
            counted_book += 1
            counted_page += int(book[2])
        else:
            print(f"{i + 1:>3}. {book[0]:45} {'by ' + book[1]:30} {book[2]:>5} pages")

    if counted_book == 0:
        print("No books left to read.Why not add a new book?")
    else:
        print(f"You need to read {counted_page} pages in {counted_book} books")


def mark_completed(book_list):
    # mark the book is already read
    if check_books(book_list):
        list_books(book_list)
        print("Enter the number of a book to mark as completed")
        book_number = counted_number(book_list)
        book_index = int(book_number) - 1

        if book_list[book_index][3] == "w":
            print("The book is already completed")
        else:
            book_list[book_index][3] = "w"
            print(f"{book_list[book_index][0]} by {book_list[book_index][1]} completed!")
    else:
        print("No required books")

        return book_list


def counted_number(book_list):
    try:
        number = int(input(">>> "))
        if number < 0:
            print("Number must be > 0")
        else:
            return number
    except ValueError:
        print("Invalid input; enter a valid number")


def check_books(book_list):
    # check books to read or not
    for book in book_list:
        if book[3] == "r":
            return True
    return False


if __name__ == '__main__':
    main()
