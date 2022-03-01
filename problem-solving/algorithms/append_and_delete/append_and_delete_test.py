import pytest

from append_and_delete import appendAndDelete


def test_1():
    initial = "abc"
    desired = "def"
    operations = 6
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_2():
    initial = "aba"
    desired = "aba"
    operations = 7
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_3():
    initial = "hackerhappy"
    desired = "hackerrank"
    operations = 9
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_4():
    initial = "ashley"
    desired = "ash"
    operations = 2
    assert appendAndDelete(initial, desired, operations) == "No"


def test_5():
    initial = ""
    desired = "test"
    operations = 4
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_6():
    initial = "test"
    desired = ""
    operations = 4
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_7():
    initial = "test"
    desired = "test"
    operations = 0
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_8():
    initial = "test"
    desired = "hello"
    operations = 0
    assert appendAndDelete(initial, desired, operations) == "No"


def test_9():
    initial = "y"
    desired = "yu"
    operations = 2
    assert appendAndDelete(initial, desired, operations) == "No"


def test_10():
    initial = "abcd"
    desired = "abcdert"
    operations = 10
    assert appendAndDelete(initial, desired, operations) == "No"


def test_11():
    initial = "aaaaaaaaaa"
    desired = "aaaaa"
    operations = 7
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_12():
    initial = "zzzzz"
    desired = "zzzzzzz"
    operations = 4
    assert appendAndDelete(initial, desired, operations) == "Yes"


def test_13():
    initial = "aaabb"
    desired = "aaabc"
    operations = 0
    assert appendAndDelete(initial, desired, operations) == "No"
