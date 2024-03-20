import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    print(f"Roll: {dice1} and {dice2}. Result: {dice1 + dice2}")

    return result


def insufficient_funds(stack):
    print(f"Your stack is: {stack}")
    decision = input("Select 'a' if you want to add more chips or 'e' to exit: ")
    while True:
        if decision == 'a':
            return 'a'
        elif decision == 'e':
            return 'e'
        else:
            print("Invalid selection. Please proceed with a/e.")
