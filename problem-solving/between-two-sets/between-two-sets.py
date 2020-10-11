# AVAILABLE AT https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    maxIndex = min(b)
    minIndex = min(a)
    result = 0

    for index in range(minIndex, maxIndex + 1):
        satisfiesA = True
        satisfiesB = True

        for indexA in a:
            if index % indexA != 0:
                satisfiesA = False
                break

        if satisfiesA:
            for indexB in b:
                if indexB % index != 0:
                    satisfiesB = False
                    break

        if satisfiesA and satisfiesB:
            result += 1

    return result


tests = [
    {
        'input': [[2, 4], [16, 32, 96]],
        'output': 3
    },
    {
        'input': [[2, 6], [24, 36]],
        'output': 2
    }
]

for test in tests:
    input = test['input']
    output = test['output']
    result = getTotalX(input[0], input[1])

    if result == output:
        print('Passed')
    else:
        print('Failed -> ' + str(result) + ' - ' + str(output))
