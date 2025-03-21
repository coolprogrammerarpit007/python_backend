# Calculator Program

operator = input("Enter Operator: (+,-,*,/): ")
inp1 = float(input("Enter number 1: "))
inp2 = float(input("Enter number 2: "))

if operator == "+":
    print(f"Total: {inp1 + inp2}")
elif operator == "-":
    print(f"Subtract: {inp1 - inp2}")
elif operator == "*":
    print(f"Multipliction: {inp1 * inp2}")
elif operator == "/":
    print(f"Division: {inp1 / inp2}")
else:
    print("Wrong Operator Inputted!")