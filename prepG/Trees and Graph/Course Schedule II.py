# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:

# Input: numCourses = 1, prerequisites = []
# Output: [0]



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        al = {}
        for i,j in prerequisites:
            if(j not in al):
                al[j] = []
            al[j].append(i)
            
        vis = [False for i in range(numCourses)]
        dfs_vis = [False for i in range(numCourses)]
        self.flag = True
        path = []
        
        def solve(node):
            
            if(not self.flag):
                return
            
            vis[node] = True
            dfs_vis[node] = True

            
            if(node in al):
                for i in al[node]:
                    if(vis[i] and dfs_vis[i]):
                        self.flag = False
                        return
                    if(not vis[i]):
                        solve(i)
            
            dfs_vis[node] = False
            path.append(node)
            
        for i in range(numCourses):
            if(not vis[i]):
                solve(i)
                
        if(not self.flag):
            return []
        
        return path[::-1]


# similar to cycle detection, just added line 58 at last and reverse the path line 67