https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        i = j = 0
        ans = 0
        n = len(s)
        while(j<n):
            if(s[j] in h):
                h[s[j]] += 1
            else:
                h[s[j]] = 1
            if(j-i+1 == len(h)):
                # print(j,i,j-i+1,s[i:j+1])
                ans = max(ans,j-i+1)
                j += 1
                # print(ans)
            elif(j-i+1>len(h)):
                while(j-i+1 > len(h)):
                    h[s[i]] -= 1
                    if(h[s[i]] == 0):
                        del h[s[i]]
                    i += 1
                j += 1
        return ans
        