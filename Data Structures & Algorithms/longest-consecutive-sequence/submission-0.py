class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = {nums[i] for i in range(len(nums))}
        longestSeq = 0

        for n in numSet:
            if (n-1) not in numSet: #check if n is start of a sequence
                current = n
                currentSeq = 1
                while (current+1) in numSet:
                    current += 1
                    currentSeq += 1
                longestSeq = max(longestSeq, currentSeq)

        return longestSeq
        