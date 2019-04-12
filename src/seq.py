

def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq(n):
    a = 0
    b = 1
    yield a
    yield b
    for i in range(2, n+1):
        c = a + b
        yield c
        a = b
        b = c


def weird_fib_seq(n):
    index = 0
    a = 0
    b = 1
    yield a
    yield b
    while True:
        if index % 2 == 0 and index > 0:
            yield a
        else:
            c = a + b
            yield c
            a = b
            b = c
        index += 1


def stern_brocot(count):
    return []
