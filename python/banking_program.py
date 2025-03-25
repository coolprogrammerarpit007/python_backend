# # Banking Program
# # 1. Show Balance
# # 2. Deposit
# # 3. Withdraw
#
#


# Scope Resolution Order (LEGB Rule)
# Python follows the LEGB rule for resolving names, which stands for:
#
# Local: Names assigned within a function (local scope).
#
# Enclosing: Names in the local scope of enclosing functions (nonlocal scope).
#
# Global: Names assigned at the top level of a module (global scope).
#
# Built-in: Names pre-defined in Python (built-in scope).
#
# When you reference a variable, Python will check these scopes in order until it finds the variable or raises an error if it cannot be found.
#
# Key Points to Remember
# Variables defined inside a function are local to that function and cannot be accessed outside it unless declared as global or nonlocal.
#
# The global keyword allows modification of global variables from within functions.
#
# The nonlocal keyword allows modification of variables from an enclosing (non-global) scope within nested functions.
#
# Built-in names are always accessible and take precedence over user-defined names if they exist.
balance = 0
def show_balance():
    print(f"Your account has ${balance} in your bank account.")

def deposit(amount):
    global balance
    balance += amount
    print(f"${amount} sucessfully deposited to the bank-account.")
    print(f"Your account has ${balance} in your bank account.")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"${amount} sucessfully withdrawn from your bank-account.")
        print(f"Your account has ${balance} in your bank account.")
    else:
        print("Your account has In-Sufficient balance for the withdrawal.")

is_running = True

while is_running:
    print("--- Banking Application -----")
    print("1. Show Balance")
    print("2. Deposit Balance")
    print("3. Withdraw Balance")
    print("4. Exit")

    user_choice = int(input("Enter Option: "))

    if user_choice == 1:
        show_balance()

    elif user_choice == 2:
        amount = float(input("Enter the amount you want to be deposited: "))
        deposit(amount)

    elif user_choice == 3:
        amount = float(input("Enter the amount you want to be withdrawn: "))
        withdraw(amount)
    elif user_choice == 4:
        print("Thankyou for your time! we wish you back soon.....")
        is_running = False
    else:
        print("You enter a wrong Invalid Choice!")



# def outer_function():
#     y = 20  # Enclosing variable
#
#     def inner_function():
#         nonlocal y  # Declare y as nonlocal to modify it
#         y += 5
#         print(y)
#
#     inner_function()  # Output: 25
#     print(y)         # Output: 25
#
# outer_function()
