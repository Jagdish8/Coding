# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

class Solution:
    def makesquare(self,matchsticks):
        if(len(matchsticks)<4):
            return False
        s = 0
        n = 0
        s = s//4
        vis = []
        for i in matchsticks:
            s = s + i
            n = n + 1
            vis.append('0')
        if(s%4):
            return False
        s = s//4
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
        return solve(0,0,4)
        