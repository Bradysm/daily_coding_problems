
def find_max_stock_rev(prices, k):
    return fms_help(-1, 0, k, prices)

def fms_help(curr_min, i, trans_remaining, prices):
    if prices is None: return 0
    if i == len(prices) or trans_remaining == 0: return 0 # there is no more profit to be made
    
    # check to see if we update the current min
    if curr_min == -1: curr_min = prices[i]
    sell = (prices[i] - curr_min) if (prices[i] - curr_min) > 0 else 0
    return max(sell + fms_help(-1, i+1, trans_remaining-1, prices), fms_help(min(curr_min, prices[i]), i+1, trans_remaining, prices))

stock_prices = [5, 2, 4, 0, 1]
print (find_max_stock_rev(stock_prices, 2))

