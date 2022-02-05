# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

# Example 1:


# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Example 2:


# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.n = len(graph)
        self.vis = [False for i in range(self.n)]
        def solve(path,index):
            if(path[-1] == self.n-1):
                self.res.append(path)
                return
            if(not graph[index]):
                if(path[-1] ==self.n - 1):
                    self.res.append(path)
                return
            for i in graph[index]:
                if(not self.vis[i]):
                    self.vis[i] = True
                    solve(path + [i],i)
                    self.vis[i] = False
        solve([0],0)
        return self.res