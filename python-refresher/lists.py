"""
Lists in Python are ordered, mutable collections of items. They can hold items of different data types,
 including other lists.
Lists are defined using square brackets [] and items are separated by commas.
"""

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing list items
print(fruits[0])  # Output: apple (first item)
print(fruits[-1])  # Output: cherry (last item)

# Modifying list items
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
fruits.append("date")  # Adding an item to the end of the list
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing items from a list
fruits.remove("apple")  # Remove by value
print(fruits)  # Output: ['blueberry', 'cherry', 'date']
popped_fruit = fruits.pop()  # Remove and return the last item
print(popped_fruit)  # Output: date
print(fruits)  # Output: ['blueberry', 'cherry']

# List methods
fruits.sort()  # Sort the list in ascending order
print(fruits)  # Output: ['blueberry', 'cherry']
fruits.reverse()  # Reverse the list
print(fruits)  # Output: ['cherry', 'blueberry']
print(len(fruits))  # Output: 2 (number of items in the list)
# Checking for existence
print("cherry" in fruits)  # Output: True
print("apple" in fruits)  # Output: False

# Iterating through a list
for fruit in fruits:
    print(fruit)

# Nested lists
nested_list = [1, 2, [3, 4], [5, 6]]
print(nested_list)  # Output: [1, 2, [3, 4], [5, 6]]
print(nested_list[2])  # Output: [3, 4]
print(nested_list[2][0])  # Output: 3

# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Combining lists
more_fruits = ["elderberry", "fig", "grape"]
all_fruits = fruits + more_fruits
print(all_fruits)  # Output: ['cherry', 'blueberry', 'elderberry', 'fig', 'grape']

# Slicing lists
print(all_fruits[1:4])  # Output: ['blueberry', 'elderberry', 'fig']
print(all_fruits[:3])  # Output: ['cherry', 'blueberry', 'elderberry']
print(all_fruits[2:])  # Output: ['elderberry', 'fig', 'grape']

# Clearing a list
all_fruits.clear()
print(all_fruits)  # Output: []

# Copying a list
copied_fruits = fruits.copy()
print(copied_fruits)  # Output: ['cherry', 'blueberry']
print(copied_fruits is fruits)  # Output: False (different objects)

# Extending a list
fruits.extend(["honeydew", "kiwi"])
print(fruits)  # Output: ['cherry', 'blueberry', 'honeydew', 'kiwi']
# Inserting an item at a specific position
fruits.insert(1, "avocado")
print(fruits)  # Output: ['cherry', 'avocado', 'blueberry', 'honeydew', 'kiwi']
# Finding the index of an item
index_of_blueberry = fruits.index("blueberry")
print(index_of_blueberry)  # Output: 2

# Counting occurrences of an item
count_of_cherry = fruits.count("cherry")
print(count_of_cherry)  # Output: 1
# Converting a string to a list
sentence = "Hello world"
words = sentence.split()  # Default split by whitespace
print(words)  # Output: ['Hello', 'world']
# Converting a list to a string
joined_sentence = " ".join(words)
print(joined_sentence)  # Output: Hello world

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Using enumerate to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Using zip to combine two lists
colors = ["red", "green", "blue"]
combined = list(zip(fruits, colors))
print(combined)  # Output: [('cherry', 'red'), ('avocado', 'green'), ('blueberry', 'blue')]

# List unpacking
first, second, *rest = fruits
print(first)  # Output: cherry
print(second)  # Output: avocado
print(rest)  # Output: ['blueberry', 'honeydew', 'kiwi']

# Using map to apply a function to all items in a list
upper_fruits = list(map(str.upper, fruits))
print(upper_fruits)  # Output: ['CHERRY', 'AVOCADO', 'BLUEBERRY', 'HONEYDEW', 'KIWI']

# Using filter to filter items in a list
long_fruits = list(filter(lambda x: len(x) > 5, fruits))
print(long_fruits)  # Output: ['blueberry', 'honeydew']

# List comprehension with nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Flattening a nested list using list comprehension
nested = [[1, 2, 3], [4, 5], [6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# Using all() and any() with lists
all_positive = all(x > 0 for x in [1, 2, 3, 4])
print(all_positive)  # Output: True
any_negative = any(x < 0 for x in [1, -2, 3, 4])
print(any_negative)  # Output: True

# Finding the maximum and minimum values in a list
numbers = [10, 20, 5, 30]
max_number = max(numbers)
min_number = min(numbers)
print(max_number)  # Output: 30
print(min_number)  # Output: 5






