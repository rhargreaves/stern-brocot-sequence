from fractions import Fraction
from src.seq import fibonacci, weird_fib_seq, fib_seq, stern_brocot
from src.graph import stern_brocot_graph
from itertools import islice
import pytest


def test_returns_first_5_numbers_of_stern_brocot():
    assert take(stern_brocot, 5) == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)]


@pytest.mark.skip(reason="WIP")
def test_returns_first_5_numbers_of_stern_brocot_via_graph():
    assert take(stern_brocot_graph, 5) == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)]


def test_fibonacci_weird_seq_appends_previous_fib_result():
    assert take(weird_fib_seq, 5) == [0, 1, 1, 2, 1]


def test_fibonacci_weird_seq_appends_previous_fib_result_for_higher_n():
    assert take(weird_fib_seq, 10) == [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]


def test_fibonacci_weird_seq_appends_previous_fib_result_for_much_higher_n():
    assert take(weird_fib_seq, 16) == [
        0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4]


def test_fibonacci_seq_correct_for_zero():
    assert take(fib_seq, 1) == [0]


def test_fibonacci_seq_correct_for_one():
    assert take(fib_seq, 2) == [0, 1]


def test_fibonacci_seq_correct_for_n():
    assert take(fib_seq, 8) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_correct_for_zero():
    assert fibonacci(0) == 0


def test_fibonacci_correct_for_one():
    assert fibonacci(1) == 1


def test_fibonacci_correct_for_n():
    assert fibonacci(7) == 13


def take(func, n):
    return list(islice(func(), n))
