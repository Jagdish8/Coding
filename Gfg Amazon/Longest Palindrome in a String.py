# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#

class Solution:
    def longestPalin(self, S):
        # code here
        s = 0
        e = 0
        for i in range(1,len(S)):
            start = i - 1
            end = i
            while(start >= 0 and end < len(S) and S[start]==S[end]):
                if(end-start > e-s):
                    s = start
                    e = end
                start -= 1
                end += 1
            start = i - 1
            end = i + 1
            while(start >= 0 and end < len(S) and S[start]==S[end]):
                if(end-start > e-s):
                    s = start
                    e = end
                start -= 1
                end += 1
        return S[s:e+1]

# O(n**2)