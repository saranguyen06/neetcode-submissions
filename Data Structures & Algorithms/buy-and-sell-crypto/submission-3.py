class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0] #lowest price so far = best day to buy
        maxP = 0 #current price today - lowest price

        for p in prices:
            minPrice = min(minPrice, p)
            maxP = max(maxP, p - minPrice)
        return maxP
        