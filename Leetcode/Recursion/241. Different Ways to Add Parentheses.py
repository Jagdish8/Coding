# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.m={}
        def check(inp):
            if(inp in self.m.keys()):
                return self.m[inp]
            if(not inp):
                return []
            res = []
            for i in range(len(inp)):
                if(inp[i] == '+' or inp[i] == '-' or inp[i] == '*'):
                    preRes = check(inp[0:i])
                    sufRes = check(inp[i+1:])
                    for x in preRes:
                        for y in sufRes:
                            if(inp[i] == '+'):
                                res.append(x+y)
                            elif(inp[i] == '-'):
                                res.append(x-y)
                            else:
                                res.append(x*y)
            if(len(res)==0):
                res.append(int(inp)) 
            self.m[inp] = res
            return res
        return check(expression)