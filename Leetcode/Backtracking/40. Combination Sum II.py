# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 


 class Solution:
    def combinationSum2(self, candidates: List[int], target: int):
        if(sum(candidates)<target):
            return []
        if(len(set(candidates)) == 1 and candidates[0]==1):
            return [[1 for i in range(target)]]
        self.a = []
        candidates = sorted(candidates)
        def solve(c,ans):
            # print(c,ans)
            if(not c and sum(ans) != target):
                return
            if(sum(ans) == target and ans not in self.a):
                self.a.append(ans)
                return
            if(sum(ans)>target):
                return
            for i in range(len(c)):
                solve(c[i+1:],ans+[c[i]])
        solve(candidates,[])
        return self.a