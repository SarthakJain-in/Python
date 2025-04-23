operations = """+
-
*
/"""

def calculation(num1):
    print(operations)
    pick_operation = input("Pick an operation : ")
    next_num = float(input("What's the next number? : "))
    
    if pick_operation == "+":
        result = num1 + next_num
    elif pick_operation == "-":
        result = num1 - next_num
    elif pick_operation == "*":
        result = num1 * next_num
    elif pick_operation == "/":
        result = num1 / next_num
    else:
        print("Invalid operator.")
        calculation(num1)

    print(f"{num1} {pick_operation} {next_num} = {result}")

    cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'end' to close the calculator : ").lower()

    if cont == "y":
        calculation(result)
    elif cont == "n":
        calculator()
    elif cont == "end":
        print("Calculator closed.")
        return 0

def calculator():
    first_num = float(input("What's the first number? : "))
    calculation(first_num)

calculator()