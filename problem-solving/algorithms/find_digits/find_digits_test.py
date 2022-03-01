import pytest

from find_digits import findDigits


def test_124():
    assert findDigits(124) == 3


def test_111():
    assert findDigits(111) == 3


def test_10():
    assert findDigits(10) == 1
