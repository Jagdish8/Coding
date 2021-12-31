# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c={}
        vis={}
        for i in s:
            if(i not in c.keys()):
                vis[i]=0
                c[i]=1
            else:
                c[i] = c[i] + 1
        res= []
        for i in s:
            if(not vis[i]):
                while(res and res[-1]>i and c[res[-1]]>0):
                    vis[res[-1]] = 0
                    res.pop()
                vis[i] = 1
                res.append(i)
            c[i] = c[i] - 1
        return "".join(res)