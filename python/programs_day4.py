# using default arguments in a function.
import time


def net_price(list_price,discount = 0,tax = 0.05):
    amount = list_price * (1-discount) * tax
    return amount

final_price = net_price(1000)
print(f"Final Price: ${final_price}")

