class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)


class ClassTest2:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

ClassTest2.class_method()

class ClassTest3:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

ClassTest3.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}gr>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book("Harry Potter", "hardcover", 1500)
print(Book.TYPES)
print(book)

book = Book.hardcover("Harry Potter", 1500)
light_book = Book.paperback("Python 101", 600)

print(book)
print(light_book)



