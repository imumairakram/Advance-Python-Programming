try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[3])
except ZeroDivisionError:
    print("Division by zero error!")
except IndexError:
    print("Index out of range error!")

while True:
    try:
        n = int(input("enter number: "))
        break
    except:
        print("enter valid number")
        continue 


try:
    num1 = int(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = int(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Error!")
        
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")
