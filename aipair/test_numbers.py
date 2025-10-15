import pytest
from aipair.numbers import isprime

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (29, True),
    (1, False),
    (0, False),
    (-1, False),
    (-7, False),
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (12, False),
    (15, False),
    (21, False),
    (25, False),
    (49, False),
])
def test_isprime(number, expected):
    assert isprime(number) == expected