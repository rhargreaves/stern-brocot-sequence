

def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq(n):
    for i in range(0, n+1):
        yield fibonacci(i)


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
            yield fibonacci(j)
            if yieldCount > n:
                break


def stern_brocot(count):
    return []
