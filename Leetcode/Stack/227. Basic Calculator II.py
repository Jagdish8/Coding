# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        if(not s):
            return 0
        st= []
        sign = '+'
        i = 0
        while(i<len(s)):
            if(s[i].isdigit()):
                value = ""
                while(i<len(s) and s[i].isdigit()):
                    value = value + s[i]
                    i+=1
                i = i - 1
                val = int(value)
                if(sign == '+'):
                    st.append(val)
                elif(sign == '-'):
                    b = val
                    st.append(-b)
                elif(sign == '*'):
                    st.append(st.pop()*val)
                else:
                    st.append(int(st.pop()/val))
            elif(s[i] != " "):
                sign = s[i]
            i = i + 1
        print(st)
        return sum(st)