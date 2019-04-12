from fractions import Fraction
from src.seq import fibonacci, weird_fib_seq, fib_seq, stern_brocot
from itertools import islice
import pytest


def take(func, n):
    return list(islice(func(n), n+1))


@pytest.mark.skip(reason="Will fail until implementation started")
def test_returns_first_5_items():
    seq = stern_brocot(5)
    assert seq == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)]


def test_fibonacci_weird_seq_appends_previous_fib_result():
    assert take(weird_fib_seq, 4) == [0, 1, 1, 2, 1]


def test_fibonacci_weird_seq_appends_previous_fib_result_for_higher_n():
    assert take(weird_fib_seq, 9) == [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]


def test_fibonacci_weird_seq_appends_previous_fib_result_for_much_higher_n():
    assert take(weird_fib_seq, 15) == [
        0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4]


def test_fibonacci_seq_correct_for_zero():
    assert take(fib_seq, 0) == [0]


def test_fibonacci_seq_correct_for_one():
    assert take(fib_seq, 1) == [0, 1]


def test_fibonacci_seq_correct_for_n():
    assert list(fib_seq(7)) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_correct_for_zero():
    assert fibonacci(0) == 0


def test_fibonacci_correct_for_one():
    assert fibonacci(1) == 1


def test_fibonacci_correct_for_n():
    assert fibonacci(7) == 13
