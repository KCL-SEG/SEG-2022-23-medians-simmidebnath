"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

count = len(numbers)
if(count % 2 == 0):
    number1 = numbers[int(count/2) - 1]
    number2 = numbers[int((count/2))]
    sum = number1 + number2
    print(sum/2)
else:
    print(numbers[int((count)/2)])