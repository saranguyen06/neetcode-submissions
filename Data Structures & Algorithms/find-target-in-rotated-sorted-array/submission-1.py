class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r: #find pivot/min number
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        l, r = 0, len(nums) - 1
        #if target in between nums[pivot] and last element, search right half
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else: #search left half
            r = pivot - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

        