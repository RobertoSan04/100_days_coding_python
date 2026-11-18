> [!summary]
> Python Loops
# 37. Day 5 Goals: what we will make by the end of the day

> [!output]
> Password Generator

# 38. Using the for loop with Python Lists

```python title=
for item in list_of_items:
	# Do something to each item
```

```python title=
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
	print(fruit)
	print(fruit + " pie")
print(fruits)

```

> [!output]
> Apple
> Apple pie
> Peach
> Peach pie 
> Pear pie
> Pear
> ["Apple", "Peach", "Pear"]

# 39. Highest Score

## Sum Scores with function
```python title=
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_exam_scores = sum(student_scores)
print(total_exam_scores)

```

## Sum Scores with loop

```python title=
student_scores = [180, 124, 165, 173, 189, 169, 146]

sum = 0
for score in student_scores:
	sum += score

print(sum)

```

## Highest Score

```python title=
student_scores = [180, 124, 165, 173, 189, 169, 146]

max_score = 0
for score in student_scores:
	if score > max_score:
		max_score = score

```

# 40. for loops and the range() function

## Range Syntax

`for number in range(start, end, step)`
	`print(number)`

## Range function with For Loop
```python title=
for number in range (1, 10)
	print(number)
```

> [!output] 
> 1
> .
> .
> .
> 9

## Range function with For Loop with Steps
```python title=
for number in range (1, 11, 3)
	print(number)
```

> [!output] 
> 1
> 4
> 7
> 10


## Gaus Challenge

```python title=

total = 0
for number in range (1,101):
	total += number

print(total)

```

> [!output] 
> 5050

# Coding Exercise 6: FizzBuzz

FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.
- But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

```python title=
for number in range(1,101):
    if number % 3 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)

```

# Day 5 Project: Create a Password Generator

## Easy Version
Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

4 letters 2 symbols and 3 numbers then the password might look like this:

fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

## Hard Version

When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.

The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.

## Easy version

```python title=
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
password = ""  
for char in range(nr_letters):  
    password += random.choice(letters)  
  
for char in range(nr_symbols):  
    password += random.choice(symbols)  
  
for char in range(nr_numbers):  
    password += random.choice(numbers)  
  
print(f"Your password is {password}")
```

## Hard version

```python title=
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
```

