# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.



class Solution:
    def longestValidParentheses(self, s: str) -> int:

        max_length = 0
        l = r = 0
        for i in s:
            if(i == '('):
                l += 1
            else:
                r += 1
            if(l == r):
                max_length = max(max_length,2*l)
            if(r>l):
                l = r = 0
        
        l = r = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i] == '('):
                l += 1
            else:
                r += 1
            if(r == l):
                max_length = max(max_length,2*r)
            if(l>r):
                l = r = 0 
        return max_length



# The pseudo code for this approach:

# Increment left on hitting (.
# Increment right on hitting ).
# If left=right, then calculate the current substring length and update the max_length
# If right>left, then it means it's an invalid substring. So reset both left and right to 0.

# perform above algorithm once on original s and then on the reversed s.
# reverse because eg: "(()"