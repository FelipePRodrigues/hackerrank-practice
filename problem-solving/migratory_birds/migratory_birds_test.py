from migratory_birds_solution import migratoryBirds


class TestMigratoryBirds:
    def test_1(self):
        assert migratoryBirds([1, 1, 2, 2, 3]) == 1

    def test_2(self):
        assert migratoryBirds([1, 4, 4, 4, 5, 3]) == 4

    def test_3(self):
        assert migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) == 3
