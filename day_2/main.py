def main() -> None:

    #Day 2 Project: Tip Calculator
    print("\nDay 2 Project: Tip Calculator ")
    print("Welcome to the tip calculator")
    bill = int(input("What was the total bill? "))
    tip = int(input("How much tip would you like to give? (Only int) "))
    people = int(input("How many people to split the bill? "))

    pay_per_person = round((bill * (1 + tip / 100)) / people, 3)

    print(f"Each person should pay: {pay_per_person}")

if __name__ == "__main__":
    main()
