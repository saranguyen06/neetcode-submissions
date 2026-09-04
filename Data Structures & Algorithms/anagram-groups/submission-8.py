class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash map where every new key automatically defaults to a list
        anagramMap = defaultdict(list)
        #automatically initializes a key with empty list if 
        #it does not exist yet
        for s in strs:
            sortedS = ''.join(sorted(s)) #sorted character array is key
            anagramMap[sortedS].append(s)
        return list(anagramMap.values())