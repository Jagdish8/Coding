# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = j = 0
        n = len(s)
        ans = 0
        h = {}
        
        while(j < n):
            
            if(s[j] not in h):
                h[s[j]] = 0
            h[s[j]] += 1
            
            if(len(h) <= k):
                ans = max(ans,j-i+1)
                j += 1
            else:
                while(len(h) > k):
                    h[s[i]] -= 1
                    if(h[s[i]] == 0):
                        del h[s[i]]
                    i += 1
                j += 1
                
        return ans