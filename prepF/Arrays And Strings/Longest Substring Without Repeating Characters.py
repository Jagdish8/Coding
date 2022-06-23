# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abcabcbb"
         # Longest Substring Without Repeating Characters
        h = {}
        i = 0
        j = 0
        n = len(s)
        maxl = 0
        while(j<n):
            if(s[j] not in h):
                h[s[j]] = 0
            h[s[j]] += 1
            if(len(h) == j-i+1):
                maxl = max(maxl,j-i+1)
                j += 1
            else:
                h[s[i]] -= 1
                if(h[s[i]] == 0):
                    del h[s[i]]
                i += 1
                j += 1
        return maxl
                
            