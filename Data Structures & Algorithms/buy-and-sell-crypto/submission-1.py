class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxP = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxP = max(maxP, p - minPrice)
        return maxP
        