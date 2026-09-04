class Solution:
    def findMin(self, nums: List[int]) -> int:
        #min element is first element of rotated portion
        l = 0
        r = len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2 #prevent integer overflow
            if nums[m] < nums[r]: #min lies in left half (including mid)
                r = m
            else: #min lies in right half (excluding mid)
                l = m + 1
        #l points to smallest element
        return nums[l]
        