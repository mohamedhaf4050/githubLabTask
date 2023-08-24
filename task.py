def add(a,b): #Member 1
    return a+b
def subtract(a, b): #Member 2
    return a - b  
def multiply(): #Member 3
    pass
def multiply(a,b): #Member 3
    return a*b
def divide():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

def mod(a , b):     #Member 5
    return a % b





#