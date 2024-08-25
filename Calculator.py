def add(x, y):
    return x + y

def subract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y!=0:
        return x/y
    else:
        return "Error! Division by zero"

def calculator():
    print("Select OPeration")
    print("1. Add")
    print("2. subract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice=input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. please enter number only")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            if choice == '2':
                print(f"{num1} + {num2} = {subract(num1, num2)}")
            if choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            if choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Please enter a valid choice")

if __name__ == "__main__":
    calculator()
