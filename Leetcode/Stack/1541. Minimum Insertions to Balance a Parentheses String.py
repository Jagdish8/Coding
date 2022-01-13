# # Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

# # Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# # Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# # In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

# # For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# # You can insert the characters '(' and ')' at any position of the string to balance it if needed.

# # Return the minimum number of insertions needed to make s balanced.

# Example 1:

# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
# Example 2:

# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.
# Example 3:

# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

 class Solution:
    def minInsertions(self, s: str) -> int:
        st = []
        ans = 0
        i = 0
        n = len(s)
        while(i<n):
            if( s[i] == '('):
                st.append(s[i])
            else:
                if(not st):
                    if(i<n-1):
                        if(s[i+1] == ')'):
                            ans = ans + 1
                            i = i + 1
                        else:
                            ans = ans + 2
                    else:
                        ans = ans + 2
                else:
                    if(i<n-1):
                        if(s[i+1] == ')'):
                            st.pop()
                            i = i + 1
                        else:
                            st.pop()
                            ans = ans + 1
                    else:
                        st.pop()
                        ans = ans + 1
            i = i + 1
        return ans + len(st)*2
        