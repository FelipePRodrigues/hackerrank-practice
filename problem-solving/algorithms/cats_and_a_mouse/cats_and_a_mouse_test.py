from cats_and_a_mouse_solution import catAndMouse


class TestCatAndMouse:
    def test_1(self):
        assert catAndMouse(1, 2, 3) == 'Cat B'

    def test_2(self):
        assert catAndMouse(1, 3, 2) == 'Mouse C'
