#-----------------Integers: Whole numbers
#-----------------Floats: Numbers with decimals
#-----------------Strings: Sequence of characters
#-----------------Boolean: True or False
#-----------------Casting: Changing from one data type to another
#-----------------Input: Getting data from the user
#-----------------Output: Printing information to the user
#-----------------Operators: Math symbols ( + - * / % // ** )



# Print statements
print("Hello World!")

print("My name is Umair, and I am a student.")
print(f"23 + 33 = {23 + 33}")


# Variables
name = "Umair"
age = 20
gender = "male"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")


# Additional examples
print("My name is Umair, and I am a student.")
print(f"23 + 33 = {23 + 33}")


# Variable types
name = "Umair"
age = 20
gender = "male"
price = 25.65
a = None

print(f"Type of 'a': {type(a)}")
print(f"Type of 'name': {type(name)}")
print(f"Type of 'age': {type(age)}")
print(f"Type of 'gender': {type(gender)}")
print(f"Type of 'price': {type(price)}")


#String Functions

# len(): Returns the length of the string.
s = "Hello"
print(len(s))  


#lower(): Converts all characters in a string to lowercase.
s = "Hello"
print(s.lower()) 


#upper(): Converts all characters in a string to uppercase.
s = "Hello"
print(s.upper())  


#strip(): Removes leading and trailing whitespace characters from a string.
s = "   Hello   "
print(s.strip()) 


#replace(): Replaces a specified substring with another substring in a string.
s = "Hello, World!"
print(s.replace("World", "Universe")) 


#split(): Splits a string into a list of substrings based on a specified delimiter.
s = "apple,banana,orange"
print(s.split(",")) 


#join(): Joins the elements of an iterable (such as a list) into a single string, using a specified separator.
fruits = ['apple', 'banana', 'orange']
print(','.join(fruits))  


#find(): Returns the index of the first occurrence of a specified substring within a string. If the substring is not found, it returns -1.
s = "Hello, World!"
print(s.find("World"))  


s = "Hello, World!"
print(s.startswith("Hello"))
# Output: True
print(s.endswith("!"))  
# Output: True


# Practice Work
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = a + b
print(c)


# Type Casting
a = int("4")
b = 7
print(a + b)

a, b = 2, "4.3"
c = float(b)
sum = a + c
print(sum)


# ---- Logical Operator ----
a = input("Enter a number: ")
b = input("Enter a number: ")
# Comparing values
print(f"Is {a} equal to {b}? {a == b}")
print(f"Is {a} not equal to {b}? {a != b}")
print(f"Is {a} greater than {b}? {a > b}")
print(f"Is {a} less than {b}? {a < b}")
print(f"Is {a} greater than or equal to {b}? {a >= b}")
print(f"Is {a} less than or equal to {b}? {a <= b}")


# Getting user's name
name = input("What is your name? ")
print(f"Hello, {name}!")


# Arithmetic Operations
A, B = 12, 5
C = A / B
print(f"Division result of {A} and {B}: {C}")


# Floor division
C = A // B  
print(f"Floor division result of {A} and {B}: {C}")
print(f"Expression A + B * C result: {A + B * C}")


# Simple arithmetic operations
a, b = 3, 32
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division: {a / b}")
