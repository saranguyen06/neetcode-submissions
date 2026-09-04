class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window w/ hash map
        charMap = {} #track most recent index of each character
        left = 0
        maxSubstring = 0
        for right in range(len(s)):
            #omit duplicate chars if duplicate in window
            if s[right] in charMap:
                left = max(charMap[s[right]] + 1, left)
            charMap[s[right]] = right
            maxSubstring = max(maxSubstring, right-left+1)
        return maxSubstring
        