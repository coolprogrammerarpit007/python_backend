# Object Oriented Programming

# object :- A bundle of related attributes (variables) and methods (functions)
# Ex:- phone, cup, book
# You need a class (blueprint) to create many objects.

# Good Pratice is to acess the class variables by using Class Name not by the Instance.

class Student:
    class_year = 1995
    class_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.class_students += 1


student1 = Student("Arpit",25)
student2 = Student("Priyanshu",27)

# print(student1.name + " " + str(student1.age))
# print(Student.class_year)
# print(Student.class_students)


# Inheritance in python

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

class Dog(Animal):
    def speak(self):
        print("WOFFF WOOOF WOOOF!!")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

# dog.speak()
# cat.sleep()


# Multiple inheritance :- Inherit from More than one class
#                         C(A,B)
# MultiLevel Inheritance :- Inherit from a parent which inherit from another parent.
 #                        C(B) -> B(A) -> A



class Animal:
    def eat(self):
        print("All animals power to eat!")


class Prey(Animal):
    def flee(self):
        print("This animal is fleeing!")

class Predator(Animal):
    def hunt(self):
        print("This animal is Hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
# rabbit.flee()

hawk = Hawk()
# hawk.hunt()

fish = Fish()
# fish.hunt()
# fish.flee()


# fish.eat()

# super() :- Functions used in a child class to call methods from the parent class., Allows you to extend the functuanillity of the inherited methods.
# class Shape:
#     def __init__(self,color,filled):
#         self.color = color
#         self.filled = filled
#
# class Circle(Shape):
#     def __init__(self,color,filled,radius):
#         super().__init__(color,filled)
#         self.radius = radius
#
# class Square(Shape):
#     def __init__(self,color,filled,width):
#         super().__init__(color, filled)
#         self.width = width
#
# class Triangle(Shape):
#     def __init__(self,color,filled,width,height):
#         super().__init__(color, filled)
#         self.width = width
#         self.height = height
#
#
# circle = Circle("red",True,5)





# Polymorphism:- Greek words that means to "have many forms or faces"
# Two way to achieve Polymorphism
# 1. Inheritance :- An object could be treated of the same type as a parent class.
# 2. "Duck typing" :- Objects must have necessary attributes/methods.

from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Cirle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return  3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self,width):
        self.width = width

    def area(self):
        return self.width * self.width

class Triangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return  0.5 * self.height * self.width

class Pizza(Cirle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Cirle(4),Square(5),Triangle(7,8),Pizza("Peporanni",9.5)]

for shape in shapes:
    print(shape.area())