class Library:
    def __init__(self):
        """Initialization """
        self.books = []

    def add_book(self, title, author, category):
        book = {
            "title": title,
            "author": author,
            "category": category
        }
        self.books.append(book)
        print(f'Book "{title}" added successfully!')

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f' Book "{title}" removed successfully!')
                return
        print(f' Book "{title}" not found in the library.')

    def search_book(self, query):
        results = [book for book in self.books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
        if results:
            print("\n Search Results:")
            for book in results:
                print(f' {book["title"]} by {book["author"]} [{book["category"]}]')
        else:
            print(f' No books found matching "{query}".')

    def display_books(self):
        if not self.books:
            print(" The library is currently empty.")
        else:
            print("\n Library Collection:")
            for index, book in enumerate(self.books, start=1):
                print(f'{index}.  {book["title"]} by {book["author"]} [{book["category"]}]')



#main
if __name__ == "__main__":
    library = Library()

    while True:
        print("\n Library Management System")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            category = input("Enter book category: ")
            library.add_book(title, author, category)

        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == "3":
            query = input("Enter book title or author name: ")
            library.search_book(query)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print(" Invalid choice! Please enter a number between 1 and 5.")
