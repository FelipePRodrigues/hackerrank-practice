from picking_numbers_solution import pickingNumbers


class TestMagicSquare:
    def test_1(self):
        assert pickingNumbers([4, 4, 4, 4, 1, 1, 2, 2, 2]) == 5

    def test_2(self):
        assert pickingNumbers([1, 2, 4, 4, 1, 1, 2, 6, 6, 5, 5]) == 5

    def test_3(self):
        assert pickingNumbers([4, 6, 5, 3, 3, 1]) == 3

    def test_4(self):
        assert pickingNumbers([1, 2, 2, 3, 1, 2]) == 5
