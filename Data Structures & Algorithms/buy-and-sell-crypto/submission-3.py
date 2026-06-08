class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
   
        buy_price = float('inf')

        for i in prices:
            buy_price = min(i, buy_price)
            profit = max(profit ,  i-buy_price)

        return profit

            

