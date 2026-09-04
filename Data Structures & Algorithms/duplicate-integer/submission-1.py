class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create hash set
        seenNums = set();
        #traverse nums list
        for i in nums:
            if i in seenNums:
                return True
            seenNums.add(i)
        return False
            
        