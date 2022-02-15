from bill_division_solution import bonAppetit


class TestBillDivision:
    def test_1(self):
        assert bonAppetit([3, 10, 2, 9], 1, 12) == '5'

    def test_2(self):
        assert bonAppetit([3, 10, 2, 9], 1, 7) == 'Bon Appetit'
