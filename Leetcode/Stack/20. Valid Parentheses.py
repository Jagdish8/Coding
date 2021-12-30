# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:
# # 
# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        def opening(paran):
            if(paran == '(' or paran == '[' or paran == '{'):
                return True
        def check(paran):
            if(paran == ')'):
                return '('
            elif(paran == '}'):
                return '{'
            else:
                return '['
        if (not s):
            return True
        if(len(s)%2):
            return False
        if(s[0] == ')' or s[0] == ']' or s[0] == '}'):
            return False
        st = [s[0]]
        for i in range(1,len(s)):
            if(opening(s[i])):
                st.append(s[i])
            else:
                if(not st):
                    return False
                if(check(s[i]) == st[-1]):
                    st.pop()
                else:
                    return False
        if(st):
            return False
        return True