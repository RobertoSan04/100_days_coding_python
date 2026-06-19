# 22. Control Flow with if / else and Conditional Operators

![[Pasted image 20260321222003.png]]

```python
if condition:
	do this
else:
	do this
```

**Exercise**
Replace tickets ride machien

```python
print("Welcome to the rollercoaster!)
height = int(input("What is your height in cm?"))

if height > = 120:
	print("You can ride the rollercoaster)
else:
	print("Sorry you have to grow taller before you can ride")
```


# 23. Introducing the Modulo

Modulo is used to get the reminding of the division


|        |      |      |      |      |      |      |      |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|        |      |      | 3    | .    | 3    | 3    | 3    |
|        | ____ | ____ | ____ | ____ | ____ | ____ | ____ |
| 3      | \|   | 1    | 0    | .    | 0    | 0    | 0    |
|        |      | __   | 1    | __   | 0    | __   | __   |
|        |      | __   | __   | __   | 1    | 0    | __   |
|        |      | __   | __   | __   | __   | 1    | 0    |
| Modulo |      | __   | __   | __   | __   | __   | 1    |

10 / 3 = 3.33
10 % 3 = 1

**Exercise**
Check odd or even

```python
num = int(input("What is the number you want to check?"))

if num % 2 == 0:
	print("The number is even)
else:
	print("The number is odd")
```

# 24. Nested if statements and elif statements

![[Pasted image 20260321222124.png]]
## Nested if/else

```python
if condition:
	if another condition:
		do this
	else:
		do this
else: 
	do this
```

**Example**

```python
print("Welcome to the rollercoaster!)
height = int(input("What is your height in cm?"))

if height > = 120:
	print("You can ride the rollercoaster)
	age = int(input("What is your age?"))
	if age < = 18:
		print("Please pay $7")
	else:
		print("Please pay $12")
else:
	print("Sorry you have to grow taller before you can ride")
```

## Elif

**Example**

```python
print("Welcome to the rollercoaster!)
height = int(input("What is your height in cm?"))

if height > = 120:
	print("You can ride the rollercoaster)
	age = int(input("What is your age?"))
	if age < = 12:
		print("Please pay $5")
	elif age < = 18:
		print("Please pay $7")
	else:
		print("Please pay $12")
else:
	print("Sorry you have to grow taller before you can ride")
```
# Coding Exercise 5: BMI Calculator with Interpretations

Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"

Refer to this graphic for help:

![](https://img-c.udemycdn.com/redactor/raw/coding_exercise_instructions/2024-07-16_08-47-01-cc3e87bef6eece9325bed5f52990234e.png)

```python
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
```

## Solution

```python
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
	print("underweight")
elif bmi >= 18.5 and bmi < 25:
	print("normal weight")
else: 
	print("overweight")

```

# 25. Multiple If Statements in Succession

![[Pasted image 20260321222214.png]]

```python
print("Welcome to the rollercoaster!)
height = int(input("What is your height in cm?"))
bill = 0

if height > = 120:
	print("You can ride the rollercoaster)
	age = int(input("What is your age?"))
	if age < = 12:
		print("Please pay $5")
		bill = 5
	elif age < = 18:
		print("Please pay $7")
		bill = 7
	else:
		print("Please pay $12")
		bill = 7
	
	wants_photo = input("Do you want to have a photo taken? Type y for Yes or n for N0")
	if wants_photo == "y":
		bill += 3
		
	
	print(f"Your final bill is {bill}")
	
else:
	print("Sorry you have to grow taller before you can ride")
```

# 26. Pizza Order Practice

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program

Based on a user's order, work out their final bill. Use the `input()` function to get a user's preferences and then add up the total to their order and tell them how much they have to pay

- Small Pizza: $15
- Medium Pizza: $20
- Large Pizza: $25
- Add pepperoni for small pizza (Y or N): +$2
- Add pepperoni for medium or large pizza (Y or N): +$3
- Add extra cheese for any size pizza (Y or N): +$1

```python

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
```

# 27. Logical Operator

- And
- Or
- Not


## And

```python
>>> a = 12
>>> a > 10 and a < 13
True
>>> a > 15 and a < 13
False
```

|       |       |       |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | False |
| False | True  | False |
| False | False | False |
## Or
```python
>>> a = 12
>>> a > 10 or a < 10
True
```

|       |       |       |
| ----- | ----- | ----- |
| True  | True  | True  |
| True  | False | True  |
| False | True  | True  |
| False | False | False |
## Not
```python
>>> not True
False
```

![[Pasted image 20260330123513.png]]
```python
print("Welcome to the rollercoaster!)
height = int(input("What is your height in cm?"))
bill = 0

if height > = 120:
	print("You can ride the rollercoaster)
	age = int(input("What is your age?"))
	if age < = 12:
		print("Please pay $5")
		bill = 5
	elif age < = 18:
		print("Please pay $7")
		bill = 7
	# New line
	elif age > = 45 and age < = 55:
	# elif 45 < = age > = 55:
		print("Everyting is going to be ok. Have a free ride with us!")
	# End of new line
	else:
		print("Please pay $12")
		bill = 7
	
	wants_photo = input("Do you want to have a photo taken? Type y for Yes or n for N0")
	if wants_photo == "y":
		bill += 3
		
	
	print(f"Your final bill is {bill}")
	
else:
	print("Sorry you have to grow taller before you can ride")
```

# Quiz 4: Logical Operators Quiz

**Question 1:**
What will the following code evaluate to?
`not 5 == 5`

- True
- **False**

**Question 2:**
What will the following code evaluate to?
`False or True or False`

- **True**
- False
- Syntax Error

Question 3:

What will the following code print?
```python
a = 5
b = 7
if a >= b and a != b:
	print("A")
elif not a >= b and a != b:
	print("B")
else:
	print("C")
```

- A
- **B**
- C

# 28. Day 3 Project: Treasure Island

Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart [linked here](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload) to create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!

![[Pasted image 20260330124433.png]]
```python
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
```