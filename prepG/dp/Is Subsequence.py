# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # self.h = {}
        def common_subsequence(s,t):
            
            dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
            
            for i in range(len(s)+1):
                for j in range(len(t)+1):
                    if(i == 0):
                        dp[i][j] = 0
                    elif(j == 0):
                        dp[i][j] = 0
                    elif(s[i-1] == t[j-1]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
            return dp[i][j]
            
        return True if(common_subsequence(s,t) == len(s)) else False