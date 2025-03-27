#Question: 01
#Write a Python program that prompts the user to enter a username and password. If both match predefined values (USERNAME = "admin" and PASSWORD = "admin123"), print "Login Successful!". If the username is incorrect, print "Invalid Username!". If the password is incorrect, print "Invalid Password!". Ensure that the program follows proper conditional logic to handle different cases correctly.

USERNAME = "admin"
PASSWORD = "admin123"
username = input("Enter Your Username: ")
user_password = input("Enter Your Password: ")

if username == USERNAME and user_password == PASSWORD:
    print("Login Successful!")
elif username != USERNAME:
    print("Invalid Username!")
elif user_password != PASSWORD:
    print("Invalid Password!")
else:
    print("Login Failed!")

# Question: 02
# Write a Python program that extracts and interprets details from a given roll number. The roll number format is YYYYMMX, where: YYYY represents the year of admission. MM represents the month (01 for January, 02 for February, etc.). X represents a class timing code (A, B, C, etc.).
# The program should:
# Prompt the user to enter their roll number. Extract and display the year and timing code from the roll number. Convert the month code to the corresponding month name and display it. Match the timing code to a predefined schedule and display the class timing. Handle invalid month and timing codes appropriately by displaying error messages.

print("Sample Roll-Number: 202407A")
user = input("Enter your Roll-Number: ")
year = user[0:4]    
month = user[4:6]  
timing = user[-1]

print("Year:", year)
print("Timing Code:", timing)

if month == "01":
    print("Month: January")
elif month == "02":
    print("Month: February")
elif month == "03":
    print("Month: March")
elif month == "04":
    print("Month: April")
elif month == "05":
    print("Month: May")
elif month == "06":
    print("Month: June")
elif month == "07":
    print("Month: July")
elif month == "08":
    print("Month: August")
elif month == "09":
    print("Month: September")
elif month == "10":
    print("Month: October")
elif month == "11":
    print("Month: November")
elif month == "12":
    print("Month: December")
else:
    print("Invalid Month!")

if timing == "A":
    print("Class Timings: 9-11 AM")
elif timing == "B":
    print("Class Timings: 11-1 PM")
elif timing == "C":
    print("Class Timings: 1-3 PM")
elif timing == "D":
    print("Class Timings: 3-5 PM")
elif timing == "E":
    print("Class Timings: 5-7 PM")
elif timing == "F":
    print("Class Timings: 7-9 PM")
else:
    print("Invalid Timing!")


# Question: 03

# Write a Python program for a restaurant ordering system. The program should: Display a menu with different food items and their prices. Allow the user to place an order by typing the name of the item. Continue taking orders until the user types "done".
# Add the price of each ordered item to the total bill. Handle cases where the user enters an item that is not on the menu by displaying an error message. Display the total bill amount at the end and thank the user.

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
