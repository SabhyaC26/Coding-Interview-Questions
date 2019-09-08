# best time to buy and sell stock
def maxProfit(prices):
    if not prices:
        return 0
    minPrice = float('inf')
    maxProft = 0
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)
    return maxProfit
