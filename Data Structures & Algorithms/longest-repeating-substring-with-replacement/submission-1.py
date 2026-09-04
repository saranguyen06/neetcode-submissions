class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hash map to store frequencies of each unique char
        l = 0
        maxFreq = 0
        maxLen = 0
        #replacements needed = window length - max freq
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            #window requires more than k replacements, shrink
            while (r-l+1) - maxFreq > k:  
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen
        