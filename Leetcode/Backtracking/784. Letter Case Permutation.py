# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]
 
 class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        def solve(com,s):
            if(len(com) == n):
                ans.append(com)
                return
            for i in range(len(s)):
                if(s[i].isalpha()):
                    solve(com+s[i].lower(),s[i+1:])
                    solve(com+s[i].upper(),s[i+1:])
                else:
                    solve(com+s[i],s[i+1:])
        solve("",s)
        return ans
                