class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxWater = 0

        while l < r:
            currentWater = min(heights[l], heights[r]) * (r-l)
            if maxWater < currentWater:
                maxWater = currentWater
            #move shorter wall; area is bottlenecked by shorter wall, 
            #only moving the shorter wall provides chance to find 
            #taller wall that can compensate for lost width
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        