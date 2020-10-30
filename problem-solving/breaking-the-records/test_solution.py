from solution import breakingRecords


class TestBreakingRecords:
    def test_one(self):
        assert breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == [4, 0]

    def test_two(self):
        assert breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]
