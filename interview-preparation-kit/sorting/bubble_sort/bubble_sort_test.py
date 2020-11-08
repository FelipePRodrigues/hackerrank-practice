from bubble_sort_solution import countSwaps


class TestBubbleSort:
    def test_1(self):
        assert countSwaps([1, 2, 3]) == [0, 1, 3]

    def test_2(self):
        assert countSwaps([4, 2, 3, 1]) == [5, 1, 4]

    def test_3(self):
        assert countSwaps([3, 2, 1]) == [3, 1, 3]

    def test_4(self):
        assert countSwaps([1, 2, 3, 4, 5]) == [0, 1, 5]
