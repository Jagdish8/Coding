# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        h = {}
        i = 0
        while(i < len(s)):
            if(s[i] not in h):
                if t[i] in h.values():
                    return False
                h[s[i]] = t[i]
            else:
                # print(s[i],t[i],h)
                if(s[i] in h and h[s[i]] != t[i]):
                    return False
            i += 1
        return True
            
        