class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            while j < len(prices):
                m = max(prices[j] - prices[i],m)
                j+=1
            i+=1
            
        return m
