

def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq(n):
    a = 0
    b = 1
    for i in range(0, n+1):
        if i == 0:
            yield a
        elif i == 1:
            yield b
        else:
            c = a + b
            yield c
            a = b
            b = c


def weird_fib_seq(n):
    yieldCount = 0
    j = 0
    for i in range(1, n+2):
        yieldCount += 1
        yield fibonacci(i)
        if yieldCount > n:
            break
        if i > 2:
            j += 1
            yieldCount += 1
            yield list(weird_fib_seq(j))[-1]
            if yieldCount > n:
                break


def stern_brocot(count):
    return []
