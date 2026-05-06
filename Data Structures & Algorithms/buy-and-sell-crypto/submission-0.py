class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101
        for price in prices:
            if price > minPrice:
                profit = price - minPrice
                maxProfit = max(maxProfit, profit)
            else:
                minPrice = price
        return maxProfit
