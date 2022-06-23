# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def toNumber(s):
            n = 0
            j = 0
            for i in s[::-1]:
                n += int(i) * (2**j)
                j += 1
            return n
        def toBinary(n):
            s = ""
            while(n):
                s += str(n%2)
                n = n // 2
            return s[::-1]
        if(a == '0' and b == '0'):
            return "0"
        n1 = toNumber(a)
        n2 = toNumber(b)
        return toBinary(n1+n2)
                