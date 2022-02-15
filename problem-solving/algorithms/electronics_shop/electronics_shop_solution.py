def getMoneySpent(keyboards, drives, budget):
    impossibleToBuy = min(keyboards) + min(drives) > budget
    if impossibleToBuy:
        return -1

    maxBill = 0
    for keyboard in keyboards:
        for drive in drives:
            currentbill = keyboard + drive

            if currentbill == budget:
                return currentbill

            elif currentbill > maxBill and currentbill < budget:
                maxBill = currentbill

    return maxBill
