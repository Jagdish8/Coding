https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start= 0
        n = len(s)
        maxl=0
        for i in range(1,n):
            low = i-1
            high = i
            while(low >= 0 and high < n and s[low]==s[high]):
                if(high-low+1 > maxl):
                    maxl = high-low+1
                    start = low
                low-=1
                high+=1
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