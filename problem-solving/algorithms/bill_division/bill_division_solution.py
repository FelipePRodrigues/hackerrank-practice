# AVAILABLE AT https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, itemNotEated, annaPart):
    newBillTotal = sum(bill) - bill[itemNotEated]
    eachPart = newBillTotal / 2

    if eachPart == annaPart:
        message = 'Bon Appetit'
    else:
        message = str(int(annaPart - eachPart))

    # print(message)
    return message
