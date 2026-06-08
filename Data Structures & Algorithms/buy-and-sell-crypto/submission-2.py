class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        bought = False
        for i in range(len(prices)):
            buy_price = min(prices[:i+1])
            sell_price = max(prices[i:])
            profit = max(profit , sell_price-buy_price)


        return profit

            

