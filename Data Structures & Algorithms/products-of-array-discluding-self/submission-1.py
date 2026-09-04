class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1st pass: fill res[i] with product of all elements to
        # left of i (prefix product)
        #2nd pass: multiply each res[i] with product of all elements to 
        # right of i (postfix product)
        n = len(nums)
        res = [1] * n
        prefix = postfix = 1

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
