def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Choose the operation option to perform :")
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")

    choice = input("Enter choice (A/B/C/D): ")
    choice = choice.upper()
    if choice in ['A', 'B', 'C', 'D']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            return

        if choice == 'A':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 'B':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 'C':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 'D':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input! Please choose valid operation from the given options.")

if __name__ == "__main__":
    main()
