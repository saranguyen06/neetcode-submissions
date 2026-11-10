class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for c, pre in prerequisites:
            preMap[c].append(pre)

        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(c):
            if c in visitSet: #cycle detected
                return False
            if preMap[c] == []:
                return True

            visitSet.add(c)
            for pre in preMap[c]:
                if not dfs(pre): return False #if we find one course that can't be completed, return False for the whole function
            visitSet.remove(c)
            preMap[c] = []
            return True
            
        # loop through every course in case graph is not connected
        for c in range(numCourses):
            if not dfs(c): return False
        return True
        