# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.ans = 0
        al = {}
        for i,j in edges:
            if(i not in al):
                al[i] = []
            if(j not in al):
                al[j] = []
            al[i].append(j)
            al[j].append(i)
            
        def solve(index):
            vis.add(index)
            if(index in al):
                for i in al[index]:
                    if(i not in vis):
                        solve(i)
        
        vis = set()
        for i in range(n):
            if(i not in vis):
                self.ans += 1
                solve(i)
        return self.ans
        