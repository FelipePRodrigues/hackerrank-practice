from solution import circularArrayRotation

TEST_CASES = [
    [[3, 4, 5], 2, [2], [3]],
    [[3, 4, 5], 1, [2], [4]],
    [[1, 2, 3, 4, 5], 2, [3, 4], [2, 3]],
    [[1, 2, 3], 2, [0, 1, 2], [2, 3, 1]]
]


def test():
    for test in TEST_CASES:
        result = circularArrayRotation(test[0], test[1], test[2])

        if result != test[3]:
            print(f"ERROR -> {result} <> {test[3]}")
            print(test)
            return

    print("SUCCESS")


test()
