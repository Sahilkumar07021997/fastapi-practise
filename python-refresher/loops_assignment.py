"""
For & While Loops Assignment
"""

arr = [1, 2, 3, 4, 5]

"""Using for loop to iterate through the list and print each element"""
for element in arr:
    print(element)

"""Using while loop to iterate through the list and print each element"""
while True:
    if not arr:
        break
    print(arr.pop(0))

"""Using for and range to iterate through the list and print each element"""
for x in range(3, 6):
    print(x)