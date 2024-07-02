num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /) ")
match operator:
    case '+':
        results = num1 + num2
        print(f"The result is {results}")
    case '-':
        results = num1 - num2
        print(f"The result is {results}")
    case '*':
        results = num1 * num2
        print(f"The result is {results}")
    case '/':
        if num2 != 0:
            results = num1 / num2
            print(f"The result is {results}")
        else:
            print("Cannot divide by zero.")
