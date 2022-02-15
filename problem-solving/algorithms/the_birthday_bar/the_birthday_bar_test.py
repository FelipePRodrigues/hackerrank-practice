from the_birthday_bar_solution import birthday


class TestTheBirthdayBar:
    def test_one(self):
        assert birthday([2, 2, 1, 3, 2], 4, 2
                        ) == 2

    def test_two(self):
        assert birthday([1, 2, 1, 3, 2], 3, 2
                        ) == 2

    def test_three(self):
        assert birthday([1, 1, 1, 1, 1, 1], 3, 2
                        ) == 0

    def test_four(self):
        assert birthday([4], 4, 1
                        ) == 1

    def test_five(self):
        assert birthday([3, 5, 4, 1, 2, 5, 3, 4, 3, 2, 1, 1, 2, 4, 2, 3, 4, 5, 3, 1, 2, 5, 4, 5, 4, 1, 1,
                         5, 3, 1, 4, 5, 2, 3, 2, 5, 2, 5, 2, 2, 1, 5, 3, 2, 5, 1, 2, 4, 3, 1, 5, 1, 3, 3, 5], 18, 6
                        ) == 10

    def test_six(self):
        assert birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7
                        ) == 3
