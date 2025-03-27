# ---- Simple Calculator ---- #
print("This is a simple calculator.")
print("What do you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("For exiting the program, enter 0")

# Getting user choice
choice = int(input("Enter Your Choice In Number: "))

if choice == 1:
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    print("The sum of the two numbers is:", num1 + num2)
    print("Thank you for using the calculator")

elif choice == 2:
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    print("The subtraction of the two numbers is:", num1 - num2)
    print("Thank you for using the calculator")

elif choice == 3:
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    print("The multiplication of the two numbers is:", num1 * num2)
    print("Thank you for using the calculator")

elif choice == 4:
    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    print("The division of the two numbers is:", num1 / num2)
    print("Thank you for using the calculator")

elif choice == 0:
    print("Thank you for using the calculator")

# ---- QR Restaurant Menu ---- #
print("Welcome to QR Restaurant, Here's the menu")
print("1. Pizza, Price: 700")
print("2. Burger, Price: 300")
print("3. Fries, Price: 200")
print("4. Sandwich, Price: 150")
print("5. Pasta, Price: 500")
print("6. Cold Drink, Price: 100")
print("7. Ice cream, Price: 200")
print("8. Cake, Price: 1000")

order_total = 0

# Loop for taking orders
while True:
    choose = input("What would you like to order? (Type 'done' to finish order) ").capitalize()

    if choose == "Done":
        break

    if choose == "Pizza":
        print("You ordered a Pizza, the price is 700")
        order_total += 700
    elif choose == "Burger":
        print("You ordered a Burger, the price is 300")
        order_total += 300
    elif choose == "Fries":
        print("You ordered Fries, the price is 200")
        order_total += 200
    elif choose == "Sandwich":
        print("You ordered a Sandwich, the price is 150")
        order_total += 150
    elif choose == "Pasta":
        print("You ordered Pasta, the price is 500")
        order_total += 500
    elif choose == "Cold Drink":
        print("You ordered a Cold Drink, the price is 100")
        order_total += 100
    elif choose == "Ice cream":
        print("You ordered Ice cream, the price is 200")
        order_total += 200
    elif choose == "Cake":
        print("You ordered Cake, the price is 1000")
        order_total += 1000
    else:
        print("Sorry, we don't have that")

print(f"Your total order price is: Rs/{order_total}")
print("Thanks for your order.")

# ---- Conditional Statements ---- #
food = input("Name the food that the people of Karachi eat mostly on Friday?: ")
eat = "Yes" if food == "Biryani" else "No"
print(eat)

# Fee calculation based on age and gender
A = int(input("Age: "))
G = input("M/F: ")
if (A == 1 or A == 2) and G == "M":
    print("Fee is 100")
elif (A == 3 or A == 4 or G == "F"):
    print("Fee is 200")
elif A == 5 and G == "M":
    print("Fee is 300")
else:
    print("No fee")

# Traffic light example
light = input("Enter the color of the traffic light: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Light is broken")

# ---- If statement examples ---- #
age = int(input("What is your age?\nPlease Enter Your Age Here: "))
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

# Traffic light example (repeated)
light = input("Enter the color of the traffic light: ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Light is broken")

# ---- End of Conditional Statements ---- #
