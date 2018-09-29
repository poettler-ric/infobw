from sys import argv, exit

def is_float(a):
    """Checks whether a string is a float."""
    try:
        float(a)
        return True
    except ValueError:
        return False

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("division by zero")
        exit()
    return a / b

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def modulo(a, b):
    if not a.is_integer() or not b.is_integer():
        print("need integer for modulo")
        exit()
    return a % b

def factorial(a):
    if not a.is_integer():
        print("need integer for factorial")
        exit()
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)

def handle_args(s):
    if len(s) == 2:
        # checking parameters
        if not is_float(s[0]):
            print("need float")
            exit()

        # cast parameters to needed types
        n1 = float(s[0])
        op = s[1]

        # execute operation
        if op not in operations:
            print("not implemented")
        else:
            print(operations[op](n1))
    else:
        # checking parameters
        if not is_float(s[0]) or not is_float(s[2]):
            print("need float")
            exit()

        # cast parameters to needed types
        n1 = float(s[0])
        op = s[1]
        n2 = float(s[2])

        # execute operation
        if op not in operations:
            print("not implemented")
        else:
            print(operations[op](n1, n2))

operations = {
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    '%': modulo,
    '!': factorial,
}

if __name__ == '__main__':
    if '-f' in argv:
        with open(argv[2]) as f:
            for l in f:
                handle_args(l.split())
    else:
        handle_args(argv[1:])
