# Given a string s, determine if it is valid.

# A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

# Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
# Return true if s is a valid string, otherwise, return false.

 

# Example 1:

# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.
# Example 2:

# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.
# Example 3:

# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.
 

 class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) == 1 or len(s) == 2):
            return False
        st = []
        for i in s:
            if(len(st)>1 and st[-2] == 'a' and st[-1] == 'b' and i == 'c'):
                st.pop()
                st.pop()
            else:
                st.append(i)
        if(len(st)):
            return False
        return True