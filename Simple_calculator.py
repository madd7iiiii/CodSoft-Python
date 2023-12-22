# TASK 2 SIMPLE CALCULATOR
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!= 0:
        return x/y
    
    else:
        print("Error: Division by zero")

def calculator():
    print("*********Simple Calculator*********")
    print("1. Additon")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")

    a = input("Enter choice (1/2/3/4): ")

    if a in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if a == '1':
            result = add(num1,num2)
            print(f"{num1} + {num2} = {result}")

        elif a == '2':
            result = subtract(num1,num2)
            print(f"{num1} - {num2} = {result}")

        elif a == '3':
            result = multiply(num1,num2)
            print(f"{num1} * {num2} = {result}")

        elif a == '4':
            result = divide(num1,num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid Input. Please enter a valid choice (1/2/3/4).")

calculator()


