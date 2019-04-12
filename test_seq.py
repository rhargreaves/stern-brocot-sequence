from fractions import Fraction
from src.seq import fibonacci, weird_fib_seq, fib_seq, stern_brocot
import pytest


@pytest.mark.skip(reason="Will fail until implementation started")
def test_returns_first_5_items():
    seq = stern_brocot(5)
    assert seq == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)]


def test_fibonacci_weird_seq_skips_zero():
    assert list(weird_fib_seq(2)) == [1, 1, 2]


def test_fibonacci_weird_seq_appends_previous_fib_result():
    assert list(weird_fib_seq(3)) == [1, 1, 2, 1]


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
