from fractions import Fraction
import pytest


def fibonacci(index):
    if index == 0 or index == 1:
        return index
    return fibonacci(index-1) + fibonacci(index-2)


def fib_seq(n):
    for i in range(0, n+1):
        yield fibonacci(i)


def stern_brocot(count):
    return []


@pytest.mark.skip(reason="Will fail until implementation started")
def test_returns_first_5_items():
    seq = stern_brocot(5)
    assert seq == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)]


def test_fibonacci_seq_correct_for_zero():
    assert list(fib_seq(0)) == [0]


def test_fibonacci_seq_correct_for_one():
    assert list(fib_seq(1)) == [0, 1]


def test_fibonacci_seq_correct_for_n():
    assert list(fib_seq(7)) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_correct_for_zero():
    assert fibonacci(0) == 0


def test_fibonacci_correct_for_one():
    assert fibonacci(1) == 1


def test_fibonacci_correct_for_n():
    assert fibonacci(7) == 13