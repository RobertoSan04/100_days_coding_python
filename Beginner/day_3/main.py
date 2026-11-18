def main() -> None:

    # 26. Pizza Order Practice
    print("n 26. Pizza Order Practice")
    print("Welcome to Python Pizza Deliveries")
    size = input("What size pizza do you want? S, M or L: ")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if size == "S":
        price = 15
    elif size == "M":
        price = 20
    elif size == "L":
        price = 25
    else:
        print("You typed something wrong")
        return

    if pepperoni == "Y":
        if size == "S":
            price += 2
        else:
            price += 3

    if extra_cheese == "Y":
        price += 1

    print(f"Your price for the pizza is {price}")

    #28. Day 3 Project: Treasure Island
    print("\n28. Day 3 Project: Treasure Island")
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure")
    choice1 = input("You are at a crossroad, where do you want to go? \"left\" or \"right\"?").lower()

    if choice1 == "left":
        choice2 = input("You have come to a lake. "
                        "There is a island in the middle of the lake. "
                        "Type \"wait\" to wait for the boat. "
                        "Type \"swim\" to swim across").lower()
        if choice2 == "wait":
            choice3 = input("You arrive at island unharmed"
                "There is house with 3 doors."
                "One red, one yellow, one blue"
                "Which colour do you choose?").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice3 == "yellow":
                print("You found the treasure. You Win!")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")




if __name__ == "__main__":
    main()
