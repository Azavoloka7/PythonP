import mysql.connector
from bookshop_classes import Book

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port = "3308",
    password="Z@v010ka",
    database="bookshop"
)

# Create a cursor object
cursor = mydb.cursor()

# Function to load books from the database
def load_books_from_db():
    try:
        # Execute SQL query to retrieve books data
        cursor.execute("SELECT * FROM books")
        books_data = cursor.fetchall()

        # Create a list to store Book objects
        books = []

        # Iterate over each row of books data and create Book objects
        for book_data in books_data:
            book_id, title, author, price = book_data
            book = Book(book_id, title, author, price)
            books.append(book)

        return books
    except mysql.connector.Error as err:
        print("Error loading books from the database:", err)
        return []

# Example usage:
def display_books():
    books = load_books_from_db()
    if books:
        for book in books:
            book.display_info()
    else:
        print("No books found.")

# Update the choice '1' case in the main function to call the display_books function
def main():
    while True:
        print("\nBookShop Management System")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Add Client")
        print("4. Add Manager")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_books()
        elif choice == '2':
            add_new_book()
        elif choice == '3':
            add_new_client()
        elif choice == '4':
            add_new_manager()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
