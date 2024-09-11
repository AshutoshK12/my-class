import art


def add(n1, n2):
    return n1 + n2

def multi(n1, n2):
    return n1 * n2

def divde(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

operations ={
    "+" : add,
    "-" : sub,
    "*" : multi,
    "/" : divde,
}


def calculator():
    print(art.logo)
    should_accumlate = True
    num1 = float(input("What is your first number...?\t"))
    while should_accumlate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick the operator..")
        num2 = float(input("What is your second number ..?\t"))
        answer = operations[operation_symbol](num1 , num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'Yes' is for continuing calculating {answer} or Type 'No' stop calculating " ).lower()


        if choice == 'yes':
            num1 = answer
        else:
            should_accumlate = False
            print("\n" * 10)
            calculator()


calculator()





