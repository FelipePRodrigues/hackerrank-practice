def hurdleRace(k, height):
    return 0 if height >= max(k) else max(k) - height


class TestTheHurdleRace:
    def test_1(self):
        assert hurdleRace([1, 6, 3, 5, 2], 4) == 2

    def test_2(self):
        assert hurdleRace([2, 5, 4, 5, 2], 7) == 0

    def test_3(self):
        assert hurdleRace([1, 2, 3, 3, 2], 1) == 2
