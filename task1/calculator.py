#This is a python calculating program

import math

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Sine (sin)")
    print("6. Cosine (cos)")
    print("7. Tangent (tan)")
    
    operation = input("Enter the operation you want to perform (+, -, *, /, sin, cos, tan): ").strip().lower()
    
    if operation in ['+', '-', '*', '/']:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
  
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is undefined.")
    elif operation in ['sin', 'cos', 'tan']:
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)

        if operation == 'sin':
            result = math.sin(radians)
            print(f"sin({angle}°) = {result}")

        elif operation == 'cos':
            result = math.cos(radians)
            print(f"cos({angle}°) = {result}")

        elif operation == 'tan':
            result = math.tan(radians)
            print(f"tan({angle}°) = {result}")

    else:
        print("Error: Invalid operation selected.")

calculator()
