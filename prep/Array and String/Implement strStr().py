# Implement strStr().

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i =j = 0
        n = len(haystack)
        s = ""
        while(j<n):
            s += haystack[j]
            if(j-i+1<len(needle)):
                j += 1
            else:
                if(s == needle):
                    return i
                s = s[1:]
                i += 1
                j += 1
        return -1
                    

# simple sliding window approach