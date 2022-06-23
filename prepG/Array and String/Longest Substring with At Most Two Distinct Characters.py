class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        h = {}
        m = -1
        i = 0
        j = 0
        n = len(s)
        while( j < n ):
            # print(h)
            if(s[j] not in h):
                h[s[j]] = 0
            h[s[j]] += 1
             
            if(len(h) <= 2):
                m = max(m,j-i+1)
                j += 1
            else:
                while(len(h) > 2):
                    h[s[i]] -= 1
                    if(h[s[i]] == 0):
                        del h[s[i]]
                    i += 1
                j += 1
                
        return m

# sliding window