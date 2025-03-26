# for shape in shapes:
#     print(shape.area())
# from tkinter.font import names


# "Duck Typing":- Another way to achieve polimorphism besides Inheritance. Objects must have the minimum attributes/methods
# "If it looks like a duck and quacks like a Duck , It must be a duck too."

# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
# class Car:
#     alive = False
#     def speak(self):
#         print("Horn!")
#
#
# animals = [Dog(),Cat(),Car()]
#
# for animal in animals:
#     animal.speak()


# Static Methods:- A method that belongs to a class rather than any Object from that class(Instance) Usually used for generally
#                  Utility Functions.

# Instance Method:- Best for the operation on Instance of the class (Objects.)
# Static Methods:- Best for Utility functions that do not need the acess to class Data.

# class Employee:
#     def __init__(self,name,position):
#             self.name = name
#             self.position = position
#
#     def get_info(self):
#         return f"{self.name} = {self.position}"  # Static Method
#
#     # Static Methods:- Utility Functions
#
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions = ["Manager","Cashier","Cook","Janitor"]
#         return position in valid_positions
#
# employee = Employee("Mohit","Cook")
# print(employee.is_valid_position("Engineer"))
# print(employee.get_info())


# Class Methods:- Allow operations related to the class itself
#                 Take (cls) as the first parameter , which represents the class itself.

# class Student:
#     count = 0
#     total_gpa = 0
#
#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     def get_info(self):
#         return f"{self.name} = {self.gpa}"   # Instance Method
#
#     @classmethod
#     def get_count(cls):
#         return f"Total Number of students are: {cls.count}"
#
#     @classmethod
#     def get_total_gpa(cls):
#         return f"Student Total GPA IS: {(cls.total_gpa/3)}"
#
# student1 = Student("Spoangebob",3.5)
# student2 = Student("Patrick",2.5)
# student3 = Student("Sandy",4.9)
# print(Student.get_count())
# print(Student.get_total_gpa())


#Magic Methods:- Dunder Methods (double underscores) __init__,__str__,__eq__
# They are automatically called by many of the Python's built In operations.
# They allow developers to define or customize the behaviour of objects.

class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} By {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages


book1 = Book("The Hobbit","J.R.R Tolkien",310)
book2 = Book("Harry Potter","J.K Rowling",420)
book4 = Book("Harry Potter","J.K Rowling",420)
book3 = Book("The Lion King","Andrew Simonds",190)

print(book2 < book3)
print(book3)
print(book2 == book4)