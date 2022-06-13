# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if(i in "([{"):
                st.append(i)
            else:
                if(i == ')'):
                    if(st and st[-1] == '('):
                        st.pop()
                    else:
                        return False
                if(i == ']'):
                    if(st and st[-1] == '['):
                        st.pop()
                    else:
                        return False
                if(i == '}'):
                    if(st and st[-1] == '{'):
                        st.pop()
                    else:
                        return False
        if(st):
            return False
        return True

# easy using stack