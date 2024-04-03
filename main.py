import os
import mysql.connector as ms

db=ms.connect(
    host="127.0.0.1",
    user="root",
    password="gvvk@007",
    database='library',
    autocommit=True
)

cursor=db.cursor()

sql="describe books"
cursor.execute(sql)

# for x in cursor:
#     print(x)

def addBook():
    try:
        # Get book details from user input
        print("Enter Book Details:")
        isbn = input("Enter the ISBN: ")
        title = input("Enter the book's title: ")
        author = input("Enter the author's name: ")
        category=input("Category:")
        pages=input("Enter No. of pages:")
        year=input("Enter Publication Year:")

        # Insert the book into the database
        query = "INSERT INTO Books (ISBN, BookName, Author, Category, NumOfPages, PublicationYear) VALUES(%s, %s, %s, %s, %s, %s)"
        values = (isbn, title, author, category, pages, year)
        cursor.execute(query, values)
        print(title, " added successfully.")

    except ms.Error as err:
        print("Error: ", err)

    finally:
        cursor.close()


def deleteBook():
    b=input("Enter the name of the book you want to delete: ")
    try:
        # Delete the book from the database
        query = "DELETE FROM Books WHERE BookName = %s"
        values = (b)
        cursor.execute(query, values)
        print(b," has been deleted from the library.")

    except ms.Error as err:
        print("Error: ",err)

    finally:
        cursor.close()


def bookSearch():
    try:
        # Get user input for book title or author
        search_book = input("Enter book title or author: ")

        # Execute the search query
        query = "SELECT * FROM Books WHERE BookName LIKE %s OR Author LIKE %s"
        values = (search_book, search_book)
        cursor.execute(query, values)

        # Fetch and display the results
        results = cursor.fetchall()
        if results:
            print("Search results:")
            for row in results:
                print(f"Book ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")
        else:
            print("No matching books found.")

    except ms.Error as err:
        print("Error: ",err)

    finally:
        cursor.close()



print("================================ LIBRARY MANAGEMENT SYSTEM ================================")
print("WELCOME ADMIN!")
print("Please Login to Continue.")

u=input("Username:")
p=input("Password:")
if u=='admin' and p=='admin123':
    os.system('clear')
    print("================================ LIBRARY MANAGEMENT SYSTEM ================================")
    print("WELCOME ADMIN!")
    print("             MENU            ")
    print("-----------------------------")
    print("1.Add Book      2.Delete Book")
    print("3.Issue Book    4.Return Book")
    print("5.Search Book   6.")

else:
     print("Wrong Password...Try again later")
