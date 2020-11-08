from electronics_shop_solution import getMoneySpent


class TestMoneySpent:
    def test_1(self):
        assert getMoneySpent([4], [5], 5) == -1

    def test_2(self):
        assert getMoneySpent([3, 1], [5, 2, 8], 10) == 9

    def test_3(self):
        assert getMoneySpent([3, 5], [5, 10, 20], 15) == 15
