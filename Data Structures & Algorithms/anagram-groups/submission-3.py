class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hash map where every new key automatically defaults to a list
        anagramMap = defaultdict(list)
        #automatically initializes a key with empty list if 
        #it does not exist yet

        for s in strs:
            count = [0] * 26 #frequency array
            for char in s:
                count[ord(char) - ord('a')] += 1
            #key needs to be immutable
            anagramMap[tuple(count)].append(s)
        return list(anagramMap.values())