def get_float(propmt: str, min: float, max: float) -> float:
    while True:
        try:
            value = float(input(propmt).strip())
            if value > min and value < max:
                return value
            print(f"Please enter a number within the range [{min}, {max}")
        except ValueError:
            print("Please enter a valid number")



def get_positive_int(prompt: str) -> int:
    """Get a positive integer input from the user."""
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a positive whole number.")
        except ValueError:
            print("Please enter a valid whole number.")


def calculate_tip_split(bill: float, tip_percentage: float, num_people: int) -> float:
    """Calculate how much each person should pay including tip."""
    tip_amount = bill * (tip_percentage / 100)
    total_amount = bill + tip_amount
    return total_amount / num_people


def main() -> None:
    """Tip calculator that splits the bill among multiple people."""
    print("🧾 Welcome to the Tip Calculator! 🧾")
    print("-" * 35)
    
    # Get user inputs with validation
    bill = get_positive_float("What is the total bill amount?\n$: ")
    tip_percentage = get_positive_float("How much tip would you like to give?\nPercent: ")
    num_people = get_positive_int("How many people to split the bill?\nPeople: ")
    
    # Calculate amount per person
    amount_per_person = calculate_tip_split(bill, tip_percentage, num_people)
    
    # Display results with better formatting
    print("-" * 35)
    print(f"💰 Bill: ${bill:.2f}")
    print(f"💡 Tip: {tip_percentage}% (${bill * tip_percentage / 100:.2f})")
    print(f"👥 Split between: {num_people} people")
    print("-" * 35)
    print(f"✨ Each person should pay: ${amount_per_person:.2f}")


if __name__ == "__main__":
    main()