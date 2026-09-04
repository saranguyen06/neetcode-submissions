class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]: #current window already sorted
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: #left half sorted, search right
                l = m + 1
            else: #right half sorted, search left
                r = m - 1
        return res
        