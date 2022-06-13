# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Input: s = "ADOBECODEBANC", t = "ABC"
        # Output: "BANC"
        # Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
        
        h = {}
        for i in t:
            if(i not in h):
                h[i] = 0
            h[i] += 1
        i = j = 0
        n = len(s)
        count = len(h)
        start = 0
        end = len(s) + 1
        while(j<n):
            if(s[j] in h):
                h[s[j]] -= 1
                if(h[s[j]] == 0):
                    count -= 1
            if(count == 0):
                while(count == 0):
                    if(s[i] in h):
                        if(h[s[i]] == 0):
                            count += 1
                        h[s[i]] += 1
                    i += 1
                if(end-start>j-i):
                    # print(j,i)
                    end = j
                    start = i - 1
            if(count>0):
                j += 1
        if(end == len(s)+1):
            return ""
        return s[start:end+1]


# basic variable size sliding window 
# notes