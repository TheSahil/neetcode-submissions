class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        l,r = 0,1

        while r < len(prices):
            if prices[r] > prices[l]:
                m = max(prices[r] - prices[l], m)
                print(m)
            else:
                l = r
            r += 1

        return m
