# Simple Calculator in Python

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    """Get modulus of two numbers"""
    if y == 0:
        return "Error! Modulus by zero."
    return x % y

def power(x, y):
    """Calculate x raised to the power of y"""
    return x ** y

def calculator():
    """Main calculator function"""
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit")
    
    while True:
        print("\n" + "=" * 40)
        choice = input("Enter choice (1-7): ")
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid input! Please enter a number between 1-7.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
        
        if choice == '1':
            result = add(num1, num2)
            operator = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operator = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operator = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operator = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            operator = '%'
        elif choice == '6':
            result = power(num1, num2)
            operator = '^'
        
        print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
