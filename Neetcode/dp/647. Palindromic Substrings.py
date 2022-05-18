class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = len(s)
        for i in range(1,n):
            low = i-1
            high = i
            while(low>=0 and high<n and s[low]==s[high]):
                count = count + 1
                low-=1
                high+=1
            low = i-1
            high = i+1
            while(low>=0 and high<n and s[low]==s[high]):
                count = count + 1
                low-=1
                high+=1
            # print(s[i],count)
        return count
                
https://leetcode.com/problems/palindromic-substrings/