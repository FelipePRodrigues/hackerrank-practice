from forming_a_magic_square_solution import formingMagicSquare


class TestMagicSquare:
    def test_1(self):
        assert formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]) == 4

    def test_2(self):
        assert formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]) == 1

    def test_3(self):
        assert formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]) == 7
