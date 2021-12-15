# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def solve(s,i,j):
            if(i==j):
                return
            if(abs(j-i) == 1):
                s[i],s[j]=s[j],s[i]
                return
            s[i],s[j]=s[j],s[i]
            solve(s,i+1,j-1)
        solve(s,0,len(s)-1)