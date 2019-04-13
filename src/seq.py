from itertools import islice
from fractions import Fraction


def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


def weird_fib_seq():
    seq = [0, 1]
    yield seq[0]
    yield seq[1]
    head = 1
    while True:
        seq.append(seq[head-1] + seq[head])
        yield seq[-1]
        if head > 1:
            seq.append(seq[head])
            yield seq[-1]
        head += 1


def stern_brocot():
    y = 1
    for i, x in enumerate(weird_fib_seq()):
        if i == 0 or i == 1:
            continue
        yield Fraction(y, x)
        y = x
