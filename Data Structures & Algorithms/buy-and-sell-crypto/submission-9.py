class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                profit = prices[j] - prices[i]
                j += 1
                res = max(profit, res)
        
        return res