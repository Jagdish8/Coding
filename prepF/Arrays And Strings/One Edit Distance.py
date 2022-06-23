# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.
 

# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
 


from turtle import end_fill


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if(s == t):
            return False
        l1 = len(s)
        l2 = len(t)
        if(abs(l1-l2)>1):
            return False
        i = 0
        j = 0
        while(i<l1 and j<l2 and s[i] == t[j]):
            i += 1
            j += 1
        if(l1 > l2):
            if(j == l2):
                return True
            if(s[i+1:] == t[j:]):
                return True
            return False
        if(l1 < l2):
            if(i == l1):
                return True
            if(s[i:] == t[j+1:]):
                return True
            return False
        if(l1 == l2):
            if(s[i+1:] == t[j+1:]):
                return True
            return False
                



# Get the length of both s & t strings as l1 and l2

# If they differ more than 1, they are more than one edit distance apart, so straight return false.

# Have two pointers i and j, starting with 0th index in s & t strings respectively and
#  loop until they are same.

# Now we are at a point where both chars pointed by i and j are different or we 
# reach end of both strings.

# If l1 > l2,
    # check whether j has reached end
    #     if yes then True, since they differ by 1 lenght and all are same till l2 length
    # deletion ith from s and check whether s[i+1:] == t[j:] if yes return True
    # at last return False

# If l1 < l2,
    # check whether i has reached end
    #     if yes then True, since they differ by 1 lenght and all are same till l1 length
    # insertion at ith in s and check whether s[i:] == t[j+1:] if yes return True
    # at last return False

# If l1 == l2,
    # check whether s[i+1:] == t[j+1:] return True
    # else return False

