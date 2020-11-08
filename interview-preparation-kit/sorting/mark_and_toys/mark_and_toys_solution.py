def maximumToys(prices, markMoney):
    maxToys = 0

    prices.sort()

    # for price in prices:
    #     for i in range(0, len(prices) - 1):
    #         if (prices[i] > prices[i + 1]):
    #             prices[i], prices[i + 1] = prices[i + 1], prices[i]

    total = 0
    for price in prices:

        if (total + price) <= markMoney:
            maxToys += 1
            total += price

    return maxToys
