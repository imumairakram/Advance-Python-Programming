# Topic: While Loop 
# Simple while loop to print "hello" 100 times
count = 1
while count <= 100:
    print("hello")
    count += 1

# Countdown using while loop
i = 5
while i >= 1:
    print(i)
    i -= 1
print("Loop ended")

# Print numbers 1 to 100 using while loop 
i = 1
while i <= 100:
    print(i)
    i += 1

# Print numbers 100 to 1 using while loop  
i = 100
while i >= 1:
    print(i)
    i -= 1

# Print the multiplication table of 3 
n = 1
while n <= 10:
    print(3 * n)
    n += 1

# Print multiplication table by user input 
n = int(input("Enter any number to print its table: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# Iterating through a list using while loop 
numbs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbs):
    print(numbs[i])
    i += 1

# Iterating through a list of heroes 
heros = ["Ironman", "Thor", "Spiderman", "Batman"]
i = 0
while i < len(heros):
    print(heros[i])
    i += 1

# break in while loop  
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("End Of Loop")

# Example: Search for an item in a tuple and break when found
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36)
x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("FOUND at idx", i)
        break
    else:
        print("finding..")
    i += 1
print("end of loop")

# continue in while loop  
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# For Loop 
list = [1, 2, 3, 4, 5]
for lis in list:
    print(lis)

# for Loop using else  
Animals = ["cat", "dog", "horse"]
for animal in Animals:
    print(animal)
else:
    print("End")

# For Loop Practice Question: Print list 
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for li in list:
    print(li)

# For Loop: Linear search in list  
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 64
for idx, lis in enumerate(list):
    if lis == x:
        print("number found at idx", idx)

# Range Function   
seq = range(10)
for i in seq:
    print(i)
else:
    print("end")

# Or using direct range
for i in range(10):  # range(stop)
    print(i)

for i in range(2, 10):  # range(start, stop)
    print(i)

for i in range(2, 10, 2):  # range(start, stop, step)
    print(i)

# Range Practice_Questions 
# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

# Print the multiplication table of a number n (user input)
n = int(input("Enter any number: "))
for i in range(1, 11):
    print(n * i)

#Pass statement
# Using pass statement in loop
for i in range(5):
    pass  # This is a placeholder where code will be written later

print("Hello World")

# Practice Questions
# Calculate sum of first n natural numbers
n = 5
sum = 0
for i in range(1, n + 1):
    sum += i
print("Total sum =", sum)

# Print all even numbers between 1 to 20
for i in range(2, 21, 2):
    print(i)

# Nested loops: Multiplication table for numbers from 1 to 5
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

# Fibonacci series up to n terms using while loop
n = int(input("Enter number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

