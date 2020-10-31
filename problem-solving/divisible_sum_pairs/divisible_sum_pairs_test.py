from divisible_sum_pairs_solution import divisibleSumPairs


class TestDivisibleSumPairs:
    def test_1(self):
        assert divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]) == 3

    def test_2(self):
        assert divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5
