import pytest

from extra_long_factorials import extraLongFactorials


def test_30():
    assert extraLongFactorials(30) == 265252859812191058636308480000000


def test_25():
    assert extraLongFactorials(25) == 15511210043330985984000000


def test_4():
    assert extraLongFactorials(4) == 24
