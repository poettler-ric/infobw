from sys import argv

def is_int(a):
    return a - int(a) == 0

def subtract(a, b):
    return a - b

def handle_args(args):
    if len(args) == 2:
        n0 = float(args[0])
        op = args[1]
    
        if op not in  operations:
            print("not implemented")
        else:
            print(operations[op](n0))
    else:
        n0 = float(args[0])
        op = args[1]
        n1 = float(args[2])
    
        if op not in  operations:
            print("not implemented")
        else:
            print(operations[op](n0, n1))
        
def modulo(a, b):
    if not is_int(a) or not is_int(b):
        print("need an int")
        return None
    else:
        return a % b
    
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a -1)

operations = {
    '-': subtract,
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
