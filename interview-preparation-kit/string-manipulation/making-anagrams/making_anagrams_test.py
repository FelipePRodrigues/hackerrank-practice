from making_anagrams_solution import makeAnagram


class TestMakeAnagram:
    def test_one(self):
        assert makeAnagram('cde', 'abc') == 4

    def test_two(self):
        assert makeAnagram('felipe', 'aline') == 5
