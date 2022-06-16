# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start= 0
        n = len(s)
        maxl=0
        for i in range(1,n):
            # even
            low = i-1
            high = i
            while(low >= 0 and high < n and s[low]==s[high]):
                if(high-low+1 > maxl):
                    maxl = high-low+1
                    start = low
                low-=1
                high+=1

            #odd
            low = i-1
            high = i+1
            while(low >= 0 and high < n and s[low]==s[high]):
                if(high-low+1 > maxl):
                    maxl = high-low+1
                    start = low
                low-=1
                high+=1
        if(maxl == 0):
            return s[0]
        return s[start:start+maxl]