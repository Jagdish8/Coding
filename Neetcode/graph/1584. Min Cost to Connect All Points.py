https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def minkey(key,vis):
            mi = sys.maxsize
            mindex = 0
            for i in range(v):
                if(not vis[i] and key[i] < mi):
                    mi = key[i]
                    mindex = i
            return mindex
        v = len(points)
        g = [[0 for i in range(v)] for j in range(v)]
        for i in range(v):
            for j in range(v):
                if(i != j):
                    g[i][j] = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        key = [sys.maxsize for i in range(v)]
        key[0] = 0
        vis = [False for i in range(v)]
        for count in range(v-1):
            u = minkey(key,vis)
            vis[u] = True
            for i in range(v):
                if(g[u][i] and not vis[i] and g[u][i]<key[i]):
                    key[i] = g[u][i]
        return sum(key)