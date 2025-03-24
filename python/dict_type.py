# dictionary = collection of {key:value} pairs. ordered and changable . No Duplicates

countries = {
    "USA":"Washington D.C",
    "India":"New Delhi",
    "China" : "Bejjing",
    "Russia":"Mosscow"
}

# if(countries.get("USA")):
#     print("Country does exist!")
# else:
#     print("Country does not exist!")

# countries.update({"Japan":"Tokyo"})
# print(countries)
# countries.pop("China")
countries.popitem()
# print(countries)


# Concession Start Program


menu = {
    "pizza":3.00,
    "nachos":4.50,
    "popcorn":6.00,
    "fries":2.50,
    "chips":1.00,
    "pretzel":3.50,
    "soda":3.00,
    "lemonade":4.25
}

cart = []
total = 0


for key,value in menu.items():
    print(f"Food-Item: {key} And Price: ${value:.2f}")


while True:
    food = input("Enter Food Item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print("Item added to the cart")
    else:
        print("Fodd Item is not in the menu list.")


print("----------------- CART Items ----------------")
# print(cart)

for food in cart:
    print(f"Food: {food} And Price: {menu[food]}")
    total += menu[food]


print(f"The Total Price Of Your Menu Item Is: ${total}")