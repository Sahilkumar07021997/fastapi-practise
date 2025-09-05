"""
tuples and sets in Python, two important data structures that offer unique features and benefits.
Tuples are ordered, immutable collections of items, defined using parentheses ().
Sets are unordered, mutable collections of unique items, defined using curly braces {} or the set() function.
"""

# Tuples
# Creating a tuple
person = ("Alice", 30, "Engineer")
print(person)  # Output: ('Alice', 30, 'Engineer')

# Accessing tuple items
print(person[0])  # Output: Alice (first item)
print(person[-1])  # Output: Engineer (last item)
print(person[1:3])  # Output: (30, 'Engineer') (slicing)
print(len(person))  # Output: 3 (number of items in the tuple)

# Tuples are immutable, so we cannot modify them directly
# person[1] = 31  # This will raise a TypeError
# However, we can create a new tuple by concatenation
updated_person = person[:1] + (31,) + person[2:]
print(updated_person)  # Output: ('Alice', 31, 'Engineer')

# Tuple methods
print(person.count("Alice"))  # Output: 1 (count occurrences of an item)
print(person.index(30))  # Output: 1 (index of the first occurrence of an item)

# Iterating through a tuple
for item in person:
    print(item)

# Nested tuples
nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)  # Output: (1, 2, (3, 4), (5, 6))
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3

# Sets
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (order may vary)
more_fruits = set(["date", "elderberry", "fig"])


