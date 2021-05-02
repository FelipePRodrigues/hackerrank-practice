def utopianTree(n):
    startingHeight = 1
    for n in range(0, n):
        if n % 2 == 0:
            startingHeight = startingHeight * 2
        else:
            startingHeight = startingHeight + 1

    return startingHeight


class TestUtopianTree:
    def test_1(self):
        assert utopianTree(0) == 1

    def test_1(self):
        assert utopianTree(1) == 2

    def test_1(self):
        assert utopianTree(4) == 7
