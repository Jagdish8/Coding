# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

# Example 1:

# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Explanation: One way to remove 5 stones is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,1].
# 2. Remove stone [2,1] because it shares the same column as [0,1].
# 3. Remove stone [1,2] because it shares the same row as [1,0].
# 4. Remove stone [1,0] because it shares the same column as [0,0].
# 5. Remove stone [0,1] because it shares the same row as [0,0].
# Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
# Example 2:

# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Explanation: One way to make 3 moves is as follows:
# 1. Remove stone [2,2] because it shares the same row as [2,0].
# 2. Remove stone [2,0] because it shares the same column as [0,0].
# 3. Remove stone [0,2] because it shares the same row as [0,0].
# Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
# Example 3:

# Input: stones = [[0,0]]
# Output: 0
# Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

# efficient solution at last

# Constraints:

# 1 <= stones.length <= 1000
# 0 <= xi, yi <= 104
# No two stones are at the same coordinate point.





class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        al = {}
        
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if(stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]):
                    if(i not in al):
                        al[i] = []
                    al[i].append(j)
                    if(j not in al):
                        al[j] = []
                    al[j].append(i)
                    
        print(al)
            
        def solve(index):
            
            self.vis[index] = True
            if(index in al): 
                for node in al[index]:
                    if(not self.vis[node]):
                        solve(node)
                    
        self.m = 0
        self.vis = [False for i in stones]
        
        for i in range(len(stones)):
            if(not self.vis[i]):
                self.m += 1
                solve(i)
        
        return len(stones) - self.m


# Problem:
# we can remove a stone if and only if,
# there is another stone in the same column OR row.
# We try to remove as many as stones as possible.

# first generate the adjacency list
# 

# Two stones are connected if they are in the same row or same col.
# Connected stones will build a connected graph.
# It's obvious that in one connected graph,
# we can't remove all stones.
# We have to have one stone left.

# We call a connected graph as an island.
# One island must have at least one stone left.
# The maximum stones can be removed = stones number - islands number

# The whole problem is transferred to:
# What is the number of islands?



# Above approach is O(N**2)
# since for generating the graph it is taking O(n**2)


# for generating O(n) approach

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        self.x = {}
        self.y = {}
        
        for i,j in stones:
            if(i not in self.x):
                self.x[i] = []
            self.x[i].append(j)
            if(j not in self.y):
                self.y[j] = []
            self.y[j].append(i)
            
            
        def solve(i,j):
            
            self.vis.add((i,j))
            
            for y in self.x[i]:
                if((i,y) not in self.vis):
                    solve(i,y)
                    
            for x in self.y[j]:
                if((x,j) not in self.vis):
                    solve(x,j)
                    
        self.m = 0
        self.vis = set()
        
        for i,j in stones:
            if((i,j) not in self.vis):
                self.m += 1
                solve(i,j)
        
        return len(stones) - self.m


# using 2 lists x and y for storing i,j all in stones
# then see dfs approach