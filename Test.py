import time

class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author  = author
        self.is_borrowed = is_borrowed
    
    def borrow(self):
        self.is_borrowed = True
        print("The Book attribute is_borrowed is now True!")

    def return_book(self):
        self.is_borrowed = False
        print("\nThe Book attribute is_borrowed is now False and returned")

book1 = Book("The Mysterious Rabbit", "Mr. Loli", False)
book2 = Book("Cute Little Magic Pups", "Mrs. Anter", False)
book3 = Book("Uncle's Search Mission", "Mrs. Dearie", False)

for book in[book1, book2, book3]:
    time.sleep(1)
    book.borrow()
    time.sleep(1)
    book.return_book()

