from mark_and_toys_solution import maximumToys


class TestMarkAndToys:
    def test1(self):
        assert maximumToys([3, 4, 1, 5], 10) == 3

    def test2(self):
        assert maximumToys([1, 12, 5, 111, 200, 1000, 10], 50) == 4

    def test3(self):
        assert maximumToys([1, 2, 3, 4], 7) == 3

    def test4(self):
        assert maximumToys([3, 7, 2, 9, 4], 15) == 3
