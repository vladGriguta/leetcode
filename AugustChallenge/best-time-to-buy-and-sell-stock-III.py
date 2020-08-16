class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # insights:
        # the solution should also depend on the maximum number of transactions allowed: 2
        
        # delete duplcate consecutive numbers
        from itertools import groupby
        prices = [x[0] for x in groupby(prices)]
        
        # function that computes the maximum profit on a series where only one transaction is allowed
        def maxProfitOneTransaction(local_prices):
            if not local_prices:
                return 0
            local_maxProfit = 0
            local_minPrice = local_prices[0]
            for price in local_prices:
                local_minPrice = min(local_minPrice,price)
                local_maxProfit = max(local_maxProfit,price - local_minPrice)
            return local_maxProfit
        
        # main iteration that divides list in two lists and computes the maximum profit from each
        maxProfit = 0
        for i in range(len(prices)):
            # to make the iteration faster, ignore successive prices that are monotonically decreasing
            if (i+1<len(prices)) and prices[i] >= prices[i+1]:
                continue
            profit = maxProfitOneTransaction(prices[:i]) + maxProfitOneTransaction(prices[i:])
            maxProfit = max(profit,maxProfit)
        
        return maxProfit