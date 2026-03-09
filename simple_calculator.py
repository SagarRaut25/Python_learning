# Simple Calculator in Python


print("Welcome to Python Simple Calculator!")
print("You can perform: Addition, Subtraction, Multiplication, Division")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2 = float(num2)

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter operation symbol (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)
    
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation! Please enter +, -, *, or /")

print("Thank you for using Simple Calculator!")