def main() -> None:
    # 6. Printing to the Console in Python
    print("6. Printing to the Console in Python")
    print("Hello World!")
    print()

    # Coding Exercise 1:
    print("Coding Exercise 1:")
    print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
    print("2. Knead the dough for 10 minutes.")
    print("3. Add 3g of Salt.")
    print("4. Leave to rise for 2 hours.")
    print("5. Bake at 200 degrees C for 30 minutes.")
    print()

    # 7. String Manipulation and Code Intelligence
    print("7. String Manipulation and Code Intelligence")
    print("Hello World!\nHello World!\nHello World!")
    print()

    print("String Concatenation: Hello " + "World")

    # Coding Exercise 2:
    print("\nCoding Exercise 2:")
    # Fix the code below 👇
    # print(Notes from Day 1")
    # print("The print statement is used to output strings")
    # print("Strings are strings of characters"
    # priint("String Concatenation is done with the + sign")
    # print(("New lines can be created with a \ and the letter n")

    print("Notes from Day 1")
    print("The print statement is used to output strings")
    print("Strings are strings of characters")
    print("String Concatenation is done with the + sign")
    print("New lines can be created with a\n and the letter")

    # 8. The Python Input Function
    print("\n8. The Python Input Function")
    print("Hello " + input("What's your name? "))

    # 9. Python Variables
    print("\n9. Python Variables")
    name = input("What's your name?\n")
    print("Hello " + name)

    print(len(name))

    # Coding Exercise 3: Variables
    print("\nCoding Exercise 3: Variables")
    glass1 = "milk"
    glass2 = "juice"
    print(f"Glass1: {glass1}\nGlass2: {glass2}")

    temp = glass1
    glass1 = glass2
    glass2 = temp
    print(f"\nGlass1: {glass1}\nGlass2: {glass2}")

    # 10. Variable Naming
    print("\n10. Variable Naming")

    # Quiz 1: Variable Naming Quiz
    print("\nQuiz 1: Variable Naming Quiz")

    # 11. Day 1 Project: Band Name Generator
    print("\n11. Day 1 Project: Band Name Generator")
    # 1. Create a greeting for your program.
    # 2. Ask the user for the city that they grew up in and store it in a variable.
    # 3. Ask the user for the name of a pet and store it in a variable.
    # 4. Combine the name of their city and pet and show them their band name.

    print("Hello user!")
    city = input("What is the name of the city where you grew up?\n")
    pets_name = input("What's the name of your pet?\n")
    print("Your's band name is " + city + " " + pets_name)

if __name__ == "__main__":
    main()
