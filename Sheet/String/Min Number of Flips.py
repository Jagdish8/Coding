# https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1

# Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.

# Example 1:

# Input:
# S = "001"
# Output: 1
# Explanation: 
# We can flip the 0th bit to 1 to have
# 101.


# Example 2:

# Input:
# S = "0001010111" 
# Output: 2
# Explanation: We can flip the 1st and 8th bit 
# bit to have "0101010101"
# 101.


class Solution:
    
    def flip(self, ch):
        return '1' if (ch == '0') else '0'
        
    def getFlipWithStartingCharcter(self, str, expected):
 
        flipCount = 0
        for i in range(len( str)):
             
            # if current character is not expected,
            # increase flip count
            if (str[i] != expected):
                flipCount += 1
     
            # flip expected character each time
            expected = self.flip(expected)
        return flipCount
        
    def minFlips(self, S):
        return min(self.getFlipWithStartingCharcter(S, '0'),
            self.getFlipWithStartingCharcter(S, '1'))
        