from drawing_book_solution import pageCount


class TestPageCount:
    def test_1(self):
        assert pageCount(5, 4) == 0

    def test_2(self):
        assert pageCount(6, 2) == 1

    def test_3(self):
        assert pageCount(5, 3) == 1

    def test_4(self):
        assert pageCount(6, 5) == 1

    def test_5(self):
        assert pageCount(2, 1) == 0
