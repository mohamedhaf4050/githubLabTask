def add(a,b): #Member 1
    return a+b
def subtract(): #Member 2
    pass  
def multiply(a,b): #Member 3
    return a*b
def divide(): #Member 4
    pass
def mod(a , b): #Member 5
    return a % b

def divide():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")




