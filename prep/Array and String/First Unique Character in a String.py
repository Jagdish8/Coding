# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for i,j in enumerate(s):
            if(j in h):
                h[j] = -1
            else:
                h[j] = i
        for i in h:
            if(h[i] != -1):
                return h[i]
        return -1

# ok