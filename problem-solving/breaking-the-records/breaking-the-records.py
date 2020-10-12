def breakingRecords(scores):
    breakMin = 0
    breakMax = 0
    min = scores[0]
    max = scores[0]

    for score in scores:
        if score > max:
            breakMax += 1
            max = score

        if score < min:
            breakMin += 1
            min = score

    return [breakMax, breakMin]


tests = [
    {
        'input': [3, 4, 21, 36, 10, 28, 35, 5, 24, 42],
        'output': [4, 0],
    },
    {
        'input': [10, 5, 20, 20, 4, 5, 2, 25, 1],
        'output': [2, 4],
    }
]

for test in tests:
    input = test['input']
    output = test['output']
    result = breakingRecords(input)

    if result == output:
        print('Passed')
    else:
        print('Failed -> ' + str(result) + ' - ' + str(output))
