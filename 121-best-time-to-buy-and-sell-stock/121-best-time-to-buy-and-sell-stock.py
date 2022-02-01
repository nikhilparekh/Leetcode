class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = prices[0]
        profit = 0
        for i in prices[1:]:
            if i<cmin:
                cmin=i
            else:
                profit = max(profit, i-cmin)
        return profit