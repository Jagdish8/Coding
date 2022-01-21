# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 


 class Solution:
    def __init__(self):
        self.h = {}
    def isMatch(self,s, p):
        if((s,p) in self.h):
            return self.h[(s,p)]
        if(not p):
            if(not s):
                self.h[(s,p)] = True
                return True
            self.h[(s,p)] = False
            return False
        if(not s):
            if(p[0] != '*'):
                self.h[(s,p)] = False
                return False
            else:
                a = self.h[(s,p)] = self.isMatch(s,p[1:])
                return a
        if(p[0] == '*'):
            a = self.h[(s,p)] = (self.isMatch(s[1:],p) or self.isMatch(s[1:],p[1:]) or self.isMatch(s,p[1:]))
            return a
        else:
            if(s and (s[0] == p[0] or p[0] == '?')):
                a = self.h[(s,p)] = self.isMatch(s[1:],p[1:])
                return a
            self.h[(s,p)] = False
            return False
        return self.h[(s,p)]