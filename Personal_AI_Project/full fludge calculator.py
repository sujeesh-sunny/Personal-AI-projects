def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

c = input("Select the option: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if c == "1":
    result = addition(a, b)
elif c == "2":
    result = subtraction(a, b)
elif c == "3":
    result = multiplication(a, b)
elif c == "4":
    result = division(a, b)

print("Result:", result)
