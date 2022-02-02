# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

# You may return the answer in any order.

 

# Example 1:

# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ans = []
        def solve(com):
            if(len(com) == n):
                self.ans.append(int(com))
                return
            for i in range(10):
                if(not com and i == 0):
                    continue
                if(not com or abs(int(com[-1])-int(i)) == k):
                    solve(com+str(i))
        solve("")
        return self.ans
                    
                
        