from day_of_programmer_solution import dayOfProgrammer


class TestDayOfProgrammer:
    def test_1(self):
        assert dayOfProgrammer(1800) == "12.09.1800"

    def test_2(self):
        assert dayOfProgrammer(2017) == "13.09.2017"

    def test_3(self):
        assert dayOfProgrammer(2016) == "12.09.2016"

    def test_4(self):
        assert dayOfProgrammer(1918) == "26.09.1918"
