class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window w/ hash map
        charMap = {} #track most recent index of each character
        left, right = 0, 0
        maxSubstring = 0
        while right < len(s):
            #omit duplicate chars
            if s[right] in charMap and charMap[s[right]] >= left:
                left = charMap[s[right]] + 1
            charMap[s[right]] = right
            maxSubstring = max(maxSubstring, right-left+1)
            right += 1
        return maxSubstring
        