def kangaroo(x1, v1, x2, v2):
    kangaroo1 = [x1, v1]
    kangaroo2 = [x2, v2]
    impossibleToReach = False
    longerJumper = 1 if v1 > v2 else 2

    while(not impossibleToReach):
        kangaroo1[0] += v1
        kangaroo2[0] += v2

        if kangaroo1[0] == kangaroo2[0]:
            return 'YES'

        kangarooAhead = 1 if kangaroo1[0] > kangaroo2[0] else 2
        impossibleToReach = longerJumper == kangarooAhead

    return 'NO'
