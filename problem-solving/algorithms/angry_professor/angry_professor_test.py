def angryProfessor(threshold, arrivals):
    on_time = 0

    for arrival in arrivals:
        if arrival <= 0:
            on_time = on_time + 1

            if on_time >= threshold:
                return 'NO'

    return 'YES'


class TestAngryProfessor:
    def test_1(self):
        assert angryProfessor(3, [-1, -3, 4, 2]) == 'YES'

    def test_2(self):
        assert angryProfessor(2, [0, -1, 2, 1]) == 'NO'
