class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() #stop early when the sum exceeds the target

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target: #sum including nums[j] > target
                    return
                cur.append(nums[j]) #include current num
                dfs(j, cur, total + nums[j]) #maintain j to allow reuse of current num
                cur.pop() #backtrack

        dfs(0, [], 0)
        return res
        