# slot machine
import random
def spin_row():
    symbols = ["🍒", "🍉" ,"🥭" ,"🔔", "🌟"]
    result = [random.choice(symbols) for item in range(3)]
    return result

def print_row(row):
    print("*****************************")
    print(" | ".join(row))
    print("*****************************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 5
        else:
            return bet * 10

def main():
    balance = 100
    print("**********************************")
    print("Welcome to the Slot Machine......")
    print("Symbols: 🍒 🍉 🥭 🔔 🌟 ")
    print("**********************************")

    while balance > 0:
        print(f"Current balance ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Enter a valid value")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds!")
            continue

        if bet <= 0:
            print("Bet must be some amount: ")
            continue

        balance -= bet
        print(f"You bet ${bet} and your balance is ${balance}")

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout > 0:
            print(f"You Won!")
        else:
            print(f"sorry you lost!")

        balance += payout

if __name__ == "__main__":
    main()