# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # number of unique characters available
        max_chars = len(set(s))
        n = len(s)
        ans = 0
        
        # for all char from 1 to max_chars 
        for available_char in range(1,max_chars+1):
            
            h = {}
            i = j = 0
            
            
            # simple sliding window approach
            while(j < n):
                
                if(s[j] not in h):
                    h[s[j]] = 0
                h[s[j]] += 1
                
                # if len of h is less than no of available chars
                if(len(h) < available_char):
                    j += 1
                    
                # if equal then check all have values >=k
                elif(len(h) == available_char):
                    count = 0
                    for x in h.values():
                        if(x >= k):
                            count += 1
                    if(count == available_char):
                        ans = max(ans,j - i + 1)
                    j += 1
                    
                # if greater than remove from starting
                else:
                    while(len(h) != available_char):
                        h[s[i]] -= 1
                        if(h[s[i]] == 0):
                            del h[s[i]]
                        i += 1
                    j += 1
            
        return ans
                    
            