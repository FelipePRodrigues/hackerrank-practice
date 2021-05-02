def beautifulDays(starting, ending, divisor):
    count = 0

    for day in range(starting, ending+1):
        reverse = int(str(day)[::-1])
        total = (day - reverse)

        if total % divisor == 0:
            count = count + 1

    return count


class TestBeatifulDays:
    def test_1(self):
        assert beautifulDays(20, 23, 6) == 2

    def test_2(self):
        assert beautifulDays(13, 45, 3) == 33
