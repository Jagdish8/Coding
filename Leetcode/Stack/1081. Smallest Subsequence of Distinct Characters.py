# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if(not s or len(s) == 1):
            return s
        h = {}
        vis = {}
        for i in s:
            if(i not in h):
                h[i] = 1
                vis[i] = False
            else:
                h[i] = h[i] + 1
        st = []
        for i in s:
            if(not vis[i]):
                while(st and st[-1]>i and h[st[-1]]>0):
                    vis[st.pop()] = False
                vis[i] = True
                st.append(i)
            h[i] = h[i] - 1
        return "".join(st)
        