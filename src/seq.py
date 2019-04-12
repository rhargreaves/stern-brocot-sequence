

def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq(n):
    for i in range(0, n+1):
        yield fibonacci(i)


def weird_fib_seq(n):
    for i in range(1, n+2):
        yield fibonacci(i)


def stern_brocot(count):
    return []
