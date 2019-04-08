from fractions import Fraction


def stern_brocot(count):
    return []


def test_returns_first_5_items():
    seq = stern_brocot(5)
    assert seq == [
        Fraction(1, 1),
        Fraction(1, 2),
        Fraction(2, 1),
        Fraction(1, 3),
        Fraction(3, 2)
    ]
