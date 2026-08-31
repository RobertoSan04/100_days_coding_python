> [!summary]
> Randomisation and Python Lists
# 31. Random Module
## Random int
```python
import random

random_integer = random.randint(0,10)
print(random_integer)

```

## Random float
### Semi-open range [0, 1)

It only works with values between 0 - 1

Never includes the 1.


```python title=
import random

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

```
### Closed range [a, b]

it returns a float in the range **[a, b]**, but whether `b` is actually reachable depends on floating-point rounding.

So technically the interval is **[a, b]**, but treat `b` as "extremely rarely included" in practice.

```python title=
import random

random_float = random.uniform(1, 10)
```
## Create Module

```python title="my_module"
my_favourite_number = 3.14159
```

```python title="main.py"
import random
import my_module

random_integer = random.randint(0,10)
print(random_integer)

print(my_module.my_favourite_number)

```

## Heads or Tails

Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

```python title=
import random

random_heads_or_tails = random.randomint(0,1)
if random_heads_or_tails == 0:
	print("Heads")
else:
	print("Tails")

```

# 32. Understanding the Offset and Appending Items to Lists

## Lists

A list is a data structure

```python title=
fruits = [item1, item2]
```

```python title=
states_of_usa = ["Delaware" ,"Washington"]
print(states_of_usa[0])
```

> [!output]
> Delaware

```python title=
states_of_usa = ["Delaware" ,"Washington"]
print(states_of_usa[-1])
```

> [!output]
> Washington

```python title=
states_of_usa = ["Delaware" ,"Washington",]

states_of_usa[0] = "California"

#new states_of_usa = ["California" ,"Washington",]

print(states_of_usa[0])
```

> [!output]
> California

```python title=
states_of_usa = ["Delaware" ,"Washington", ...]

states_of_usa.append("California")

print(states_of_usa)
```

> [!output]
> ["Delaware" ,"Washington", California]

# 33. Who will pay the bill?

```python title=
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(f"{random.choice(friends)} need to pay")

```


```python title=
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(f"{friends[random.randint(0, len(friends)-1)]} need to pay")

```

# 34. IndexError and Working with nested Lists

```python title=
states_of_usa = ["Delaware" ,"Washington",]

print(states_of_usa[2])
```

> [!output]
> IndexError

## Nested Lists

```python title=

fruits = [Apple, Orange, ...]
vegtables =  [Brocoli, Asparagus]

dirty_dozen = [fruits, vegtables]
```

# Quiz 5: List and IndexError Quiz

**Question 1:**
Given the following list:

1. fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

Which line of code will give you `"Apples"`?

- fruits[3]
- fruits[4]
- fruits.Apples()
- **fruits[-5]**
- fruits[-4]

**Question 2:**
Given the code below:

1. fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
2. fruits[-1] = "Melons"
3. fruits.append("Lemons")
4. print(fruits)

What do you think will be printed?

![[Screenshot 2026-04-01 at 1.22.51 p.m..png]]


**Question 3:**
Given the code below:

```python title=
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
```
What will be printed?

**What's going on?**
This question combines several of the Python List concepts that we’ve seen in the previous lessons in isolation. If the code above is at all confusing, I recommend breaking down what’s going on using several print statements using repl.it. First, try printing out:

```python title=
# First, try printing out:
print(dirty_dozen)

# Then print out:
print(dirty_dozen[0])
print(dirty_dozen[1])

# To see what happens at the next stage print out:
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
```

I hope this helps clarify how nested lists work. 🙂

- "Spinach"
- "Strawberries"
- **"Kale"**
- ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
- "Nectarines"

# 35. Day 4 Project: Rock Paper Scissors

You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

```python title=
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

```

