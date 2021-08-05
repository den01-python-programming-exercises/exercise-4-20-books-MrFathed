from book import Book

def main():
    #write your code below this line
    books = []

    while True:
        title = input("Title:")
        
        if not title:
            break

        pages = int(input("Pages:"))
        pub_year = int(input("Publication year:"))

        books.append(Book(title, pages, pub_year))

    reply = input("What information will be printed?")

    if reply == "everything":
        for book in books:
            print(book)
    elif reply == "name":
        for book in books:
            print(book.get_title())

if __name__ == '__main__':
    main()
