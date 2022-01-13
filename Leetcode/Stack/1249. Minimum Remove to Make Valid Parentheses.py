# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        st=[]
        for i in s:
            if(i == '('):
                count = count + 1
                st.append("(")
            elif(i == ')'):
                if(count == 0):
                    continue
                count = count - 1
                st.append(")")
            else:
                st.append(i)
        s = "".join(st)
        i = len(s)-1
        while(count):
            if(s[i] == '('):
                s = s[:i] + s[i+1:]
                count = count - 1
            i = i - 1
        return s