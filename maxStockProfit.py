# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# If you think intuitively of this problem, at every index i, we want to subtract
# from that index, the smallest price before that number. This will be a running
# min that we will calculate. We then subtract that min from the current val
# and then update max_profit using the max function. Pretty simple, just need
# to see the concept and you'll get it.
# Ranked in the top 100 interview questions


def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    min_val = 0 if len(prices) == 0 else prices[0] # gets the min val
    for price in prices:
        min_val = min(min_val, price)
        max_profit = max(max_profit, price - min_val)
    return max_profit