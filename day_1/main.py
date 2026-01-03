def main() -> None:
    print("Hello, my name is Roberto")
    
    # .strip function removes leading/trailing whitespace from inputs
    name = input("What's your name? ").strip()
    age = input("How old are you? ").strip()
    
    # If doesn't insert a name
    if not name:
        name = "friend"
    
    # Check if age is a digit
    if age.isdigit():
        print(f"Hello {name}, it's nice to meet another {age}-year-old!")
    else:
        print(f"Hello {name}, it's nice to meet you!")


if __name__ == "__main__":
    main()