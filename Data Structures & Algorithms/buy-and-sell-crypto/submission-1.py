class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        minBuy = prices[0]

        for sell in prices:
            m = max(m, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return m
