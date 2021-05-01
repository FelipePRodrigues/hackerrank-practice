from alternating_characters_solution import alternatingCharacters

class TestAlternatingCharacters:
    def test_one(self):
        assert alternatingCharacters("AAAA") == 3

    def test_two(self):
        assert alternatingCharacters("ABAB") == 0

    def test_three(self):
        assert alternatingCharacters("AABB") == 2