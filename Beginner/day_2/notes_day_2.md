# Overview

- Data types
- Numbers
- Operations
- Type Conversion
- f-Strings

# 14. Python Primitive Data Types

1. Strings
2. Integers
3. Floats
4. Booleans

## Subscripting

You can use positiv or negative index [-1]/[0]/[1]

```python
print("Hello"[0])
```

> [!output]
> H

## String

```python
print("123" + "345")
```

> [!output]
> 123456

## Integer = Whole number

```python
print(123 + 345)
```

> [!output]
> 468

## Large Integers

```python
print(123_456_789)
```

> [!output]
> 123456

## Float

```python
print(3.14159)
```

> [!output]
> 3.14159

## Boolean

```python
print(True)
print(False)
```

> [!output]
> True
> 

# Data Types Quiz

**Question 1:**
Which statement below is **incorrect**?

- 932 is an Integer
- **"False" is a Boolean**
- 857.25 is a Float
- "523" is a String

**Question 2:**
What is the data type of the `mystery` variable?
`mystery = 734_529.678`

- Integer
- String
- Qurtle
- **Float**

**Question 3:** 

I've put a spell on you. You are now a computer. If I give you the following code, what will you print out?
```python
street_name = "Abbey Road"
print(street_name[4] + street_name[7])
```

- eR
- "Abbey Road"
	"Abbey Road"
	"Abbey Road"
	"Abbey Road"
	"Abbey Road"
	"Abbey Road"
	"Abbey Road"
- en
- **yo**
- ya

# 15. Type Error, Type Checking and Type Conversion

## Type Error

```python
len(1234)
```

> [!output]
> TypeError

> [!tip]
> Check python documentation

## Check data type

```python
type("Hello")
```

> [!output]
> <class 'str'>

# Type Casting

```python
print(int("123") + int("456"))
```

> [!output]
> 579

> [!warning]
> You can't convert a str into a int

- int()
- float()
- str()
- bool()
 
> [!warning]
> You can't concatenate a str with a int

# 16. Mathematical Operations in Python

- Concatenation of Strings
- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Exponent
- Modulus

```python
print("My age: " + str(12))
print(123 + 456)
print(7 - 3)
print(3 * 2)
print(5 / 3)
print(5 // 3) # Floor Division
print(2**2) # Exponent
print(5 % 3) # Modulus
```

## PEMDAS
Order in which an expression is executed
- Parentesis
- Exponents
- Multiplications or Divisions
- Addition or Subtraction

# Coding Exercise 4: BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it: 

bmi is equal to the person's weight divided by the person's height squared.

Convert this sentence into code on line 6.

```python
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =

print(bmi)

```

## Solution

```python
height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height**2

print(bmi)

```

# 17. Number Manipulation and F Strings in Python

## Round

```python
bmi = 84 / 1.65**2
print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 2))
```

## Assignment

```python
score = 0

score += 1
print(score)
```

## f-strings

```python
score = 0
height = 1.0
is_winning = True

print(f"Your score is = {score}, your height is = {height}. Your winning status is = {is_winning}")

```

# Quiz 3: Mathematical Operations Quiz

**Question 1:**
You are a computer. What will this line of code print?
`print(6 + 4 / 2 - (1 * 2))`

- 3
- **6.0**
- 8.0
- 5

**Question 2:**
What is the data type of the result of the variable `a` in the following line of code:

`a = int("5") / int(2.7)`

- int
- **float**
- str
- bool

**Question 3:**
Which of these lines of code will give you an error?

- `name = input("What is your name?"`
	`print(f"Hello, {name})`

- `name = input("What is your name?"`
	`print("Hello, " + name)`

- `age = 12`
	`print(f"You are {age} years old")`

- **age = 12**
	**print("You are " + age " years old")**

**Explanation**
This will give you a Type Error. Age is an integer. You are trying to concatenate a String to an Integer.

# Day 2 Project: Tip Calculator

```python
#Day 2 Project: Tip Calculator
print("\nDay 2 Project: Tip Calculator ")
print("Welcome to the tip calculator")
bill = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? (Only int) "))
people = int(input("How many people to split the bill? "))

pay_per_person = round((bill * (1 + tip / 100)) / people, 3)

print(f"Each person should pay: {pay_per_person}")
```

