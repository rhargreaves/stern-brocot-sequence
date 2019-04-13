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


def stern_diatomic_seq():
    yield 0
    seq = [1, 1]
    for x in seq:
        yield x
    while True:
        seq.append(seq[0] + seq[1])
        yield seq[-1]
        seq.append(seq[1])
        yield seq[-1]
        seq.pop(0)


def stern_brocot():
    y = 1
    for i, x in enumerate(stern_diatomic_seq()):
        if i == 0 or i == 1:
            continue
        yield Fraction(y, x)
        y = x
