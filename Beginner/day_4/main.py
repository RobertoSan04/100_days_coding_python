def main() -> None:
    import random

    # 33. Who will pay the bill?
    print("\n33. Who will pay the bill?")
    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    print(f"{random.choice(friends)} need to pay\n")

    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    print(f"{friends[random.randint(0, len(friends)-1)]} need to pay")

    # 35. Day 4 Project: Rock Paper Scissors
    print("\n35. Day 4 Project: Rock Paper Scissors")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    machine_choice = random.randint(0,2)
    if  (user_choice == 0 and machine_choice == 2) or \
        (user_choice == 1 and machine_choice == 0) or \
        (user_choice == 2 and machine_choice == 1):
        print(f"\nMachine Choice: {machine_choice}")
        print("You win!")
    elif user_choice == machine_choice:
        print(f"\nMachine Choice: {machine_choice}")
        print("It's a tie!")
    else:
        print(f"Machine Choice: {machine_choice}")
        print("You lose :( ")

if __name__ == "__main__":
    main()
