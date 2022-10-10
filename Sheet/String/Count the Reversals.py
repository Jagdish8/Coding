# https://practice.geeksforgeeks.org/problems/count-the-reversals/0

# Given a string S consisting of only opening and closing curly brackets '{' and '}', find out the minimum number of reversals required to convert the string into a balanced expression.
# A reversal means changing '{' to '}' or vice-versa.

# Example 1:

# Input:
# S = "}{{}}{{{"
# Output: 3
# Explanation: One way to balance is:
# "{{{}}{}}". There is no balanced sequence
# that can be formed in lesser reversals.

# Example 2:

# Input: 
# S = "{{}{{{}{{}}{{"
# Output: -1
# Explanation: There's no way we can balance
# this sequence of braces.


def countRev (s):
    # your code here
    if(len(s) % 2):
        return -1
    count = 0
    temp = 0
    
    for i in s:
        if(i == '{'):
            temp += 1
        else:
            if(temp == 0):
                temp += 1
                count += 1
            else:
                temp -= 1
    return count + (temp//2)