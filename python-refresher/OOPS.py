"""
OOPS in Python
"""


class Dog:
    def __init__(self, name: str = "Tommy", age: int = 2) -> None:
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"


dog1 = Dog("Buddy", 3)
dog0 = Dog()
print(dog1.bark())  # Output: Buddy says Woof!
print(dog0.bark())  # Output: Tommy says Woof!
