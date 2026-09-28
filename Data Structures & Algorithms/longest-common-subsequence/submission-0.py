class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D Bottom-Up DP
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] #if match, look at diagonal
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) #look at l or r

        return dp[0][0]
        