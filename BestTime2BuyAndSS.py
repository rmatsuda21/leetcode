# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

"""
:type prices: List[int]
:rtype: int
"""
def maxProfit(prices):
    maxProf = 0
    curMin = prices[0]
    for i in range(1,len(prices)):
        if prices[i] - curMin > maxProf:
            maxProf = prices[i] - curMin
        
        if prices[i] < prices[i-1] and prices[i] < curMin:
            curMin = prices[i]

    return maxProf

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(maxProfit(prices))