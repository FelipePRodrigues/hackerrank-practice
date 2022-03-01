from viral_advertising import viralAdvertising


class TestDayOfProgrammer:
    def test_1(self):
        assert viralAdvertising(1) == 2

    def test_2(self):
        assert viralAdvertising(3) == 9

    def test_3(self):
        assert viralAdvertising(5) == 24
