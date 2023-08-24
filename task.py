def add(): #Member 1
    pass
def subtract(): #Member 2
    pass
def multiply(): #Member 3
    pass
def divide(): #Member 4
    pass
def mod(): #Member 5
    pass

def divide(): 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")


