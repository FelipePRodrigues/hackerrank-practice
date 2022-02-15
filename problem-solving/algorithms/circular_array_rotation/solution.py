def circularArrayRotation(array, rotations, queries):
    result = []
    rotations = rotations % len(array)

    for query in queries:
        if query >= rotations:
            result.append(array[query - rotations])
        else:
            result.append(array[len(array) - rotations + query])

    return result


# circularArrayRotation([3, 4, 5], 2, [2])
