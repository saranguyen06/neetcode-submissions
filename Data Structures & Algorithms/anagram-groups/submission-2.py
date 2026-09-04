class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            if key not in anagramMap:
                anagramMap[key] = []
            
            anagramMap[key].append(str)
        return list(anagramMap.values())