# List -> [], ordered and changable
# sets -> {}, unordered and immutable, but add or remove ok, no duplicates.
# Tuple -> (), ordered and unchangable, Duplicates Ok Fast


# Shopping Cart Program
foods = [

]

prices = []
total = 0


while True:
    food = input("What food would you like to buy ? (q to quit): ")
    if food.lower() == "q":
        break
    price = input(f"Enter the price of the food: {food}, It is in $")
    price = float(price)
    foods.append(food)
    prices.append(price)

print(f"-------------- Your Cart ----------------")

count = 0
for food in foods:
    print(f"Food Item: {food} And Price: {prices[count]}")
    count += 1

print(f"Your Shopping Total is: {sum(prices)}")