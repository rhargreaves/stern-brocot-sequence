from fractions import Fraction
import pytest


def fibonacci(index):
    if index == 0:
        return 0


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


def test_fibonacci_returns_zero():
    assert fibonacci(0) == 0
