def extraLongFactorials(n):
    count = 1
    for idx in range(1, n+1):
        count = count * idx

    print(count)
    return count
