https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        i = j = 0
        n = len(s)
        ans = 0
        while(j<n):
            if(s[j] in h):
                h[s[j]] += 1
            else:
                h[s[j]] = 1
                
            max_count = max(h.values())
            cells_count = j - i + 1
            temp = cells_count - max_count
            
            if(temp <= k):
                ans = max(ans,j-i+1)
            else:
                # while(len(h)>k):
                h[s[i]] -= 1
                if(h[s[i]] == 0):
                    del h[s[i]]
                i += 1
            j += 1
        return ans