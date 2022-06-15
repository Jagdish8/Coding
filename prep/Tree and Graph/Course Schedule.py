# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        al = {}
        for i in prerequisites:
            if(i[1] not in al):
                al[i[1]] = []
            al[i[1]].append(i[0])
        
        def check_cycle(node):
            if(not self.ans):
                return
            vis[node] = True
            dfs_vis[node] = True
            if(node in al):
                for i in al[node]:
                    if(vis[i] and dfs_vis[i]):
                        self.ans = False
                        return
                    elif(not vis[i]):
                        check_cycle(i)
            dfs_vis[node] = False
                        
        self.ans = True
        vis = [False for i in range(numCourses)]
        dfs_vis = [False for i in range(numCourses)]
        for i in range(numCourses):
            if(not vis[i]):
                check_cycle(i)
        return self.ans


# so basically if there is a cycle in the graph then ans is False else True


# extra
# for finding whether there is a cycle in a undirected graph
# only one vis used
# if a perticular node a is already visited from a node b and a is not parent of b
    # then cycle is there is there


# In case of undirected graph two vis are used 
# one vis for keeping track of nodes which are already visited and don't need to 
# be processed again
# other dfs_vis for keeping tract of nodes which are coming in the current dfs path
# before the callback occurs dfs_vis[node] is set to False to tell that it might have come in
# some dfs path but it has not comed in the same dfs path which will be coming in the future
# but vis[node] is kept True because we don't want to again check cycle for same which we did earlier

# good explantion : https://www.youtube.com/watch?v=uzVUw90ZFIg