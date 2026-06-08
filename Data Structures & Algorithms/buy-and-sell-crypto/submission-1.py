class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = False
        buy=0
        profit = 0
        for ind, i in enumerate(prices):
            for j in range(ind+1, len(prices)):
                profit = max(profit, prices[j]-prices[ind])
        return profit

            

