class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if(prices[left] > prices[right]):
                left = right
            right += 1
        return profit