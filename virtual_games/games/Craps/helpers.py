import random


def roll_dice() -> int:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    result = dice1 + dice2
    print(f"Roll: {dice1} and {dice2}. Result: {dice1 + dice2}")

    return result


def insufficient_funds(stack: int, method=None) -> str:
    print(f"Your stack is: {stack}")
    decision = ''
    if method == 'place_a_bet':
        while decision not in {'a', 'b', 'e'}:
            decision = input("Select:\n "
                             "'a' -> if you want to add more chips;\n "
                             "'b' -> to decrease your bet; \n "
                             "'e' -> to exit: ").lower()

            if decision not in {'a', 'b', 'e'}:
                print("Invalid selection. Continue with 'a', 'b', 'e'")

    else:
        while decision not in {'a', 'e'}:
            decision = input("Select:\n "
                             "'a' -> if you want to add more chips;\n "
                             "'e' -> to exit: ").lower()

            if decision not in {'a', 'e'}:
                print("Invalid selection. Continue with 'a', 'e'")

    return decision
