def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount = 0
    orangesCount = 0

    for apple in apples:
        appleLocation = apple + a

        if appleLocation >= s and appleLocation <= t:
            applesCount += 1

    for orange in oranges:
        orangeLocation = orange + b

        if orangeLocation >= s and orangeLocation <= t:
            orangesCount += 1

    return [applesCount, orangesCount]


TESTS = [
    {
        'i': [7, 10, 4, 12, [2, 3, -4], [3, -2, -4]],
        'o': [1, 2]
    },
    {
        'i': [7, 11, 5, 15, [-2, 2, -1], [5, -6]],
        'o': [1, 1]
    }
]

for test in TESTS:
    input = test['i']
    result = countApplesAndOranges(
        input[0], input[1], input[2], input[3], input[4], input[5])

    if result == test['o']:
        print('Passed')
    else:
        print('Failed -> ' + str(result) + ' - ' + str(test['o']))
