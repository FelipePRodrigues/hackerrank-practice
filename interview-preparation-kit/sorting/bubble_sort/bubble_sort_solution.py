# AVAILABLE AT https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(array):
    swapNum = 0

    for i in range(0, len(array)):
        for j in range(0, len(array) - 1):
            if (array[j] > array[j + 1]):
                swapNum += 1
                aux = array[j + 1]
                array[j + 1] = array[j]
                array[j] = aux

    # print('Array is sorted in {} swaps.'.format(swapNum))
    # print('First Element: {}'.format(array[0]))
    # print('Last Element: {}'.format(array[len(array) - 1]))

    return [swapNum, array[0], array[len(array) - 1]]
