# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "1 + 1"
# Output: 2
# Example 2:

# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        sum = 0
        i=0
        while i<len(s):
            val = s[i]
            if val.isdigit():
                n = ""
                while i < len(s) and s[i].isdigit():
                    n = n + s[i]
                    i = i + 1
                sum += sign * int(n)
                i-=1
            elif val in "+-":
                sign = [1,-1][val=="-"]
            elif val == "(":
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign = 1
            elif val == ")":
                sum = stack.pop() * sum
                sum += stack.pop()
            i+=1
        return sum