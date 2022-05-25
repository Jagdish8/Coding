https://www.codingninjas.com/codestudio/problems/graph-valid-tree_1376618?leftPanelTab=0

def checkgraph(edges, n, m):
    h = {}
    for i,j in edges:
        if(i in h.keys()):
            h[i].append(j)
        else:
            h[i] = [j]
        if(j in h.keys()):
            h[j].append(i)
        else:
            h[j] = [i]
    vis = [False for i in range(n)]
    def solve(vertice,parent):
        vis[vertice] = True
        for i in h[vertice]:
            if(not vis[i]):
                if(solve(i,vertice)):
                    return True
            elif(i != parent):
                return True
        return False
    if(solve(0,-1)):
        return False
    for i in range(n):
        if(not vis[i]):
            return False
    return True