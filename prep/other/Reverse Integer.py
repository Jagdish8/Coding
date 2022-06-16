# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if(x == 0):
            return 0
        flag = False
        if(x<0):
            flag = True
        x = abs(x)
        val = 0
        while(x):
            val = (val*10) + (x % 10)
            x = x // 10
            # print(val)
        if(-2**31 > val or val > (2**31) - 1):
            return 0
        if(flag):
            return -val
        return val

# simple reversing