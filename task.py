def add(): #Member 1
    pass
def subtract(): #Member 2
    print("subtract 2 numbers")
    num1 =float(input("enter first number"))
    num2 =float(input("enter second number"))
    print(num1-num2)

def multiply(): #Member 3
    pass
def divide_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num2 != 0:
        result = num1 / num2
        print("The result of division is:", result)
    else:
        print("Error: Cannot divide by zero.")
divide_numbers()
def mod(): #Member 5
    num1 = int(input("Enter num:"))
    num2 = int(input("Enter num: "))
    print(num1 + " % " + num2 + " = " + str(num1 % num2))

subtract()