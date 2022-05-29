https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = {}
        for i in t:
            if(i not in h):
                h[i] = 0
            h[i] += 1
        count = len(h)
        i = j = 0
        ans = len(s) + 2
        start = 0
        end = 0
        while(j<len(s)):
            if(count == 0):
                if(ans > j-i+1):
                    ans = j-i+1
                    start = i
                    end = j + 1
                if s[i] in h:
                    if h[s[i]] == 0:
                        count+=1
                    h[s[i]]+=1
                i+=1
                while i<len(s) and s[i] not in h:
                    i+=1
            else:
                if(s[j] in h):
                    h[s[j]] -= 1
                    if(h[s[j]] == 0):
                        count -= 1
            if(count != 0):
                j += 1
        return s[start:end]