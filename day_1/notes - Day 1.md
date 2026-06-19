# 6. Printing to the Console in Python

```Python
print("Hello World!")

```

> [!fail]
> `print("Hello World!)` - No closing ""

> [!help]
> Stack Overflow
> Follow PEP8 rules

**Without PEP8**
Warning in pycharm

```Python
print("Hello World!")
```

**With PEP8**
PEP8 says that it need to be a line below the final python line

```Python
print("Hello World!")

```

# Coding Exercise 1: Printing Practice
## Printing Practice
Write a program that uses print statements to print the following recipe into the Output console. The text to print is already there, you just need to make it into code. Your code should print all five lines exactly the same as the example output below. Make sure that you don't change any of these text as everything, punctuation and casing all need to match!

```Python
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes.
```

## Solution

```Python
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
```

# 7. String Manipulation and Code Intelligence
## Creating a new line

Use `\n`

```python
print("Hello World!\nHello World\Hello World)
```

## Concatenate Strings
```python
print("Hello " + "World")
print("Hello" + " " + "World")
```

> [!fail]
> `2-  print("Hello" + " World")` - Indentation Error (No white space before python line)

> [!fail]
> `print( "Hello World")` - Syntax Error

# Coding Exercise 2: Debugging Practice
## Debugging Practice

Look at the code in the code editor. There are errors on all 5 lines of code. Fix the code so that it runs without errors. Try to run the code and debug each line using the error messages and feedback.

```python
# Fix the code below 👇

print(Notes from Day 1")
 print("The print statement is used to output strings")
print("Strings are strings of characters"
priint("String Concatenation is done with the + sign")
print(("New lines can be created with a \ and the letter n")

```
## Solution

```python
# Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

```

# 8. The Python Input Function

```python
input("What is your name?")
```

## Concatenate String

```python
print("Hello " + input("What's your name?"))
```

> [!tip]
> Use [Thonny](https://thonny.org/) to visualize step-by-step python code

## Comments

```python
# This is a comment
```

# 9. Python Variables

Saves data in a variable

```python
name = input("What's your name?")
print("Hello " + name)
```

**Example**
Phone Book

| Variable | Data          |
| -------- | ------------- |
| James    | 123-1234-1234 |

> [!attention]
> Variables changes

```python
name = "Jack"
print(name)

name = "Angela"
print(name)
```

> [!tip]
> Search things in [GeeksForGeeks](https://www.geeksforgeeks.org/)

## Len function

Prints the length of characters of a string variable.

```python
name = "Jack"
print(len(name))
```

> [!output]
> 4

# Coding Exercise 3: Variables
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. **You are not allowed to type the words "milk" or "juice"**. You are only allowed to use variables to solve this exercise.

```python
glass1 = "milk"
glass2 = "juice"
```

## Solution

```python
glass1 = "milk"
glass2 = "juice"

temp = glass1
glass1 = glass2
glass2 = temp
```

# 10. Variable Naming

Make your code readable

> [!error] Errors in variables
> **No space between naming a variables:** user name = "Angela" -> username = "Angela"
> **No numbers at the beginning of the variable name:** 1length = len(username) -> length1 = len(username)
> 

# Quiz 1: Variable Naming Quiz

**Question 1:**
Which line of Python code is valid?

- var a = 12
- **a = 12**
- a: 12
- 12 = a

**Question 2:**
Which is the **best** variable name for Player 1's username?

- p1 user name = "jackbauer"
- 1_player_username = "jackbauer"
- **player1_username = "jackbauer"**
- p1u = "jackbauer"

**Question 3:**
Which block of code will produce an error? For extra points, which type of error do you think it will produce?

- **time_until_midnight = "5"**
	**print("There are " + time_until_Midnight + " hours until midnight")**

- num hours = "5"
	print ("There are " + num hours + " hours until midniaht")

- time_until_midnight = "5"
	print("There are"+time_until_midnightt" hours until midnight")

**Explanation:**
There is a typo in the last line, it should be time_until_midnight not time_until_Midnight. Because when the name of the variable was used it was not spelt the same, you will get a name error.

# 11. Day 1 Project: Band Name Generator

1. Create a greeting for your program.
2. Ask the user for the city that they grew up in and store it in a variable.
3. Ask the user for the name of a pet and store it in a variable.
4. Combine the name of their city and pet and show them their band name.
