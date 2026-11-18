class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            #if same prefix, just the prefix should come before
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen): #find first differing char
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} #False = visited, True = current path, not in dict = not visited at all
        res = []

        def dfs(c): #if returns True, cycle detected
            if c in visit:
                return visit[c]
                #if visited, return False, if in current path, return True
            
            visit[c] = True #visited and in current path

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False #no longer in current path
            res.append(c) #post-order DFS

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
