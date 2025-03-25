# module = a file containing code you want to include in your program use import to include a module (built-in or your-own)

# variable scope :- where a variable is visible and acessible
# scope resolution :- (LEGB) Local -> Enclosed -> Global -> Built-In


# def func1():
#     a = 1
#     print(a)
#
# def func(2):
#     b = 2
#     print(b)
#
#
# # if __name__ = __main__: (this script can be imported or run standalone)
# # functions and classes in this module can be reused without the main block of the code executing.
#
# def main():
#     pass
#
# if __name__ == '__main__':
#     main()

import harry

print(__name__)
print("___________________________")
harry.welcome()