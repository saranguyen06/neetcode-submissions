class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        # LIS[i] is length of the LIS starting at index i
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    # extend subsequence starting at j
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

        