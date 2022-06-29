# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def solve(x,y):
            # print(x,y)
            isConnected[x][y] = 0
            isConnected[y][x] = 0
            for node in range(len(isConnected[x])):
                if(isConnected[x][node] == 1):
                    solve(x,node)
            for i in range(len(isConnected)):
                if(isConnected[i][y] == 1):
                    solve(i,y)
        
        ans = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if(isConnected[i][j]):
                    # print(i,j,isConnected)
                    ans += 1
                    solve(i,j)
        return ans
        
# adjacency matrix is given
# same logic as number of islands