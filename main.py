def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

import art
non_stop = True

while non_stop:
    continue_to_compute = True
    print(art.logo)
    first_num = float(input("What is the first number?: "))

    while continue_to_compute:
        for operator in operation:
            print(operator)
        sign = input("Pick an operation: ")
        second_num = float(input("What is the next number?: "))
        result = operation[sign](first_num, second_num)
        print(f'{first_num} {sign} {second_num} = {result}')

        next_action = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or type 'e' to exit calculator: ").lower()
        if next_action == 'y':
            first_num = result
        elif next_action == 'n':
            continue_to_compute = False
            print("\n" * 100)
        else:
            continue_to_compute = False
            non_stop = False
            print("Good bye!")