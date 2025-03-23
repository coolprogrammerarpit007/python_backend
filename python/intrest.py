# Program to calculate Simple Intrest

principle_amount = 0
intrest_rate = 0
time = 0

while principle_amount <= 0:
    principle_amount = float(input("Enter the Principle amount: "))
    if principle_amount <= 0:
        print("Principle amount can not be less than or equal to zero.")

while intrest_rate <= 0:
    intrest_rate = float(input(("Enter the Intrest rate: ")))
    if intrest_rate <= 0:
        print("Intrest rate can not be less than or equal to zero.")

while time <= 0:
    time = int(input("Enter the time of period: "))
    if time <= 0:
        print("Time can not be less than or equal to zero.")

calculated_amount = principle_amount * pow((1 + intrest_rate/100),time)
print(f"The amount calculated will be: {calculated_amount:.2f}")
