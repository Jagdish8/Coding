# https://leetcode.com/problems/word-pattern/description/

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if(len(pattern) != len(s.split(" "))):
            return False
        h = {}
        for i,j in zip(s.split(" "), pattern):
            if(j in h):
                if(i != h[j]):
                    return False
            elif(i in h.values()):
                return False
            else:
                h[j] = i
        print(h)
        return True

        