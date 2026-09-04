class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break
            
            left = i + 1
            right = n - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1
        return res
        