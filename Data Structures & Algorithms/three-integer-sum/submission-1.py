class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array, fix one num and search for other 2 using 2 pointer
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]: #skip duplicates for 1st num
                continue
            
            if n > 0: #all remaining numbers are positive, can't sum to 0
                break
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = n + nums[left] + nums[right]
                
                if threeSum == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif threeSum < 0: #increase sum
                    left += 1
                else: #decrease sum
                    right -= 1
        return res
        