from solution_number_line_jumps import kangaroo


class TestKangaroo:
    def test_one(self):
        assert kangaroo(0, 3, 4, 2) == 'YES'

    def test_two(self):
        assert kangaroo(0, 2, 5, 3) == 'NO'
