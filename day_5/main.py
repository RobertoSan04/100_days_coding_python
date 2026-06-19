import random


def main() -> None:
    # 37. Day 5 Goals: what we will make by the end of the day


    # 38. Using the for loop with Python Lists
    print("\n38. Using the for loop with Python Lists")
    fruits = ["Apple", "Peach", "Pear"]
    for fruit in fruits:
        print(fruit)
        print(fruit + " pie")
    print(fruits)

    # 39. Highest Score
    print("\n39. Highest Score")
    student_scores = [180, 124, 165, 173, 189, 169, 146]
    total_exam_scores = sum(student_scores)
    print(total_exam_scores)

    sum = 0
    for score in student_scores:
        sum += score

    print(sum)

    max_score = 0
    for score in student_scores:
        if score > max_score:
            max_score = score

    # 40. for loops and the range() function
    for number in range(1, 10):
        print(number)

    for number in range(1, 10):
        print(number)

    # Coding Exercise 6: FizzBuzz
    for number in range(1, 101):
        if number % 3 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

    # Day 5 Project: Password Generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Easy version:
    print("Easy version")
    password = ""
    for char in range(nr_letters):
        password += random.choice(letters)

    for char in range(nr_symbols):
        password += random.choice(symbols)

    for char in range(nr_numbers):
        password += random.choice(numbers)

    print(f"Your password is {password}")

    # Hard version
    print("Hard version")
    password_char_list = []
    password = ""
    for char in range(nr_letters):
        password_char_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_char_list.append(random.choice(symbols))

    for char in range(nr_numbers):
        password_char_list.append(random.choice(letters))

    random.shuffle(password_char_list)

    password = "".join(password_char_list)

    print(f"Your password is {password}")

if __name__ == "__main__":
    main()
