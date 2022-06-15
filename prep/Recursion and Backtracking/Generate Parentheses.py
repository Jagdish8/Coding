# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if(n==0):
            return []
        self.a = []
        def solve(o,c,com):
            if(o==0 and c==0):
                self.a.append(com)
                return
            if(o == 0):
                solve(0,0,com+')'*c)
            elif(o==c and o):
                solve(o-1,c,com+'(')
            else:
                solve(o-1,c,com+'(')
                solve(o,c-1,com+')')
        solve(n,n,"")
        return self.a


# notes