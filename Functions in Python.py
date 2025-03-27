#====================== Topic: Functions in Python ======================

# Introduction:
# Functions are reusable blocks of code that perform a specific task.
# Below are various examples demonstrating how functions are used in Python.

#------------------------------------------------------------------------

# 1. Basic Function to Calculate Sum

def calc_sum(a, b):
    sum = a + b
    print(f"Sum of {a} and {b}: {sum}")
    return sum

# Test the function
calc_sum(1, 2)
calc_sum(5, 7)
calc_sum(9, 7)

#------------------------------------------------------------------------

# 2. Function Returning Values

def calc_sum_return(a, b):
    return a + b

# Test the function
sum_result = calc_sum_return(1, 2)
print(f"Returned sum: {sum_result}")

#------------------------------------------------------------------------

# 3. Function to Calculate Average

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(f"Average of {a}, {b}, {c}: {avg}")
    return avg

# Test the function
calc_avg(1, 2, 3)

#------------------------------------------------------------------------

# 4. Function to Print the Length of a List

def print_length(lst):
    print(f"Length of list: {len(lst)}")

# Test the function
cities = ["Karachi", "Lahore", "Burgerabad", "Pindi"]
cartoons = ["Hagimaru", "Tom and Jerry", "Pink Panther"]

print_length(cities)
print_length(cartoons)

#------------------------------------------------------------------------

# 5. Function to Print Elements of a List in One Line

def print_list(lst):
    for item in lst:
        print(item, end=" ")
    print()  # To ensure the next print starts on a new line

# Test the function
print_list(cities)
print_list(cartoons)

#------------------------------------------------------------------------

# 6. Function with Default Arguments

def greet(name="Guest"):
    print(f"Hello, {name}!")

# Test the function
greet("Umair")
greet()  # Uses default argument

#------------------------------------------------------------------------

# 7. Function with Keyword Arguments

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Test the function
introduce(name="Umair", age=19)
introduce(age=25, name="Sara")

#------------------------------------------------------------------------

# 8. Function with Arbitrary Arguments

def list_fruits(*fruits):
    for fruit in fruits:
        print(fruit)

# Test the function
list_fruits("Apple", "Banana", "Cherry", "Mango")

#------------------------------------------------------------------------

# 9. Lambda Function (Anonymous Function)

# Lambda to calculate square of a number
square = lambda x: x * x

# Test the lambda function
print(f"Square of 5: {square(5)}")

#------------------------------------------------------------------------

# 10. Recursive Function to Calculate Factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the recursive function
print(f"Factorial of 5: {factorial(5)}")

#------------------------------------------------------------------------

# 11. Function to Calculate Sum of Numbers in Range (For Loop Example)

def sum_range(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum of numbers from 1 to {n}: {total}")
    return total

# Test the function
sum_range(5)

#------------------------------------------------------------------------

# 12. Function to Generate Multiplication Table of a Number (While Loop Example)

def multiplication_table(n):
    i = 1
    print(f"Multiplication table of {n}:")
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1

# Test the function
multiplication_table(3)

#------------------------------------------------------------------------

# 13. Function to Check for an Element in a List (Linear Search)

def search_element(lst, x):
    for i, element in enumerate(lst):
        if element == x:
            print(f"Element {x} found at index {i}")
            return i
    print(f"Element {x} not found in the list")
    return -1

# Test the function
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
search_element(numbers, 64)

#------------------------------------------------------------------------

# 14. Function to Calculate the Sum of All Elements in a List

def sum_of_list(lst):
    total = sum(lst)
    print(f"Sum of all elements in the list: {total}")
    return total

# Test the function
sum_of_list(numbers)

#------------------------------------------------------------------------

# 15. Pass Statement Example

def placeholder_function():
    pass  

for i in range(5):
    pass  # No action taken here

print("Pass statement demo complete.")

