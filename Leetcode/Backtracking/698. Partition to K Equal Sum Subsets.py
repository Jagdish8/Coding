# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

# Example 1:

# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:

# Input: nums = [1,2,3,4], k = 3
# Output: false
 

 class Solution:
    def canPartitionKSubsets(self, matchsticks: List[int], k: int) -> bool:
        s = 0
        n = 0
        vis = []
        for i in matchsticks:
            s = s + i
            n = n + 1
            vis.append('0')
        if(s%k):
            return False
        s = s//k
        matchsticks.sort(reverse = True)
        if(matchsticks[0] > s):
            return False
        h = {}
        def solve(index,cur_sum,k):
            val = "".join(vis)
            if(val in h):
                return h[val]
            if(k==0):
                h[val] = True
                return True
            if(cur_sum == s):
                t = solve(0,0,k-1)
                h[val] = t
                return t
            for i in range(index,n):
                if(vis[i] != '1' and not (cur_sum + matchsticks[i] > s)):
                    vis[i] = '1'
                    val = "".join(vis)
                    t = solve(index+1,cur_sum + matchsticks[i],k)
                    h[val] = t
                    if(t):
                        return True
                    vis[i] = '0'
            h[val] = False
            return False
        return solve(0,0,k)
        