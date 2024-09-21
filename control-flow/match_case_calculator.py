# Simple Calculator using Match Case in Python

# Prompt the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter the second number: "))

# Ask the user to choose the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match case to perform the operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot be divided by zero.")
  