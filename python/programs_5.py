import time
def count_up(end , start = 0):
    for x in range(start,end):
        print(x)
        time.sleep(1)
    print("------------ Done! ------------")

# count_up(10)

# *args = allows you to pass multiple non-key arguments. -> passed arguments will be in type tuple.
# **kwargs = allows you to pass multiple keyword-arguments. -> passed args will be type dictionary


def print_address(**kwargs):
    for key in kwargs.keys():
        print(kwargs[key],end=" ")

# print_address(street="123 Fake St.",city="Detroit",state="MI",zip="54321")


# Itterables :- An Object/collection that can return it's elements one at a time, allowing it to be iterated over in a loop.

# sets

# fruits = {"apples","bananas","oranges","pineapples"}
#
# for fruit in fruits:
#     print(fruit)


#  List-Comprehensions

# List comprehensions = A consise way to create list in python.
# compact and easier to read than traditional loops
# [expression for value in itterables if condition] -> formula for list - comprehensions


doubles = []
for x in range(1,11):
    doubles.append(x * 2)

# print(doubles)


new_list = [x * 5 for x in range(1,11) if x > 0]
# print(new_list)

# Match -> Switch Statments

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            print("Weekend!")
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("Weekday!")
        case _:
            print("Invalid Day")

is_weekend("Sunday")
