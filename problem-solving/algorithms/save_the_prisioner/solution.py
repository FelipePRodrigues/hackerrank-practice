def saveThePrisoner(prisoners, candies, first):
    positionsAhead = candies % prisoners

    if positionsAhead == 0:
        if first == 1:
            return prisoners
        else:
            return first - 1
    else:
        if (positionsAhead + first) > prisoners:
            result = positionsAhead + first - prisoners - 1
            if result == 0:
                return prisoners
            else:
                return result
        else:
            return first + positionsAhead - 1


# saveThePrisoner(499999999, 999999997, 2)


# def saveThePrisoner(prisionersCount, candyCount, firstPrisioner):
#     positionsAfter = (candyCount % prisionersCount - 1)

#     if (positionsAfter + firstPrisioner) > prisionersCount:
#         return positionsAfter + firstPrisioner - prisionersCount
#     else:
#         return firstPrisioner + positionsAfter
