# AVAILABLE AT https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n, k, ar):
    totalPairs = 0

    for idx, i in enumerate(ar):
        for j in ar[(idx + 1):]:
            if (i + j) % k == 0:
                totalPairs += 1

    return totalPairs
