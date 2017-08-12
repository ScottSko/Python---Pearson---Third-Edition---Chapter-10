class Book:

    def __init__(self, title, author, publisher):

        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def set_title(self, title):

        self.__title = title

    def set_author(self, author):

        self.__author = author

    def set_publisher(self, publisher):

        self.__publisher = publisher

    def get_tite(self):

        return self.__title

    def get_author(self):

        return self.__author

    def get_publisher(self):

        return self.__publisher

    def __str__(self):

        return "Title: " + self.__title + \
                "\nAuthor: " + self.__author + \
                "\neEmail: " + self.__publisher

def main():

    t = "hello"
    a = "hi"
    p = "hey"

    book = Book(t, a, p)

    message = str(book)

    print(message)

main()
