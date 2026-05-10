# Basic Calculator in Python

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Answer =", num1 + num2)

elif op == "-":
    print("Answer =", num1 - num2)

elif op == "*":
    print("Answer =", num1 * num2)

elif op == "/":
    print("Answer =", num1 / num2)

else:
    print("Invalid Operator")