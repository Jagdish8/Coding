https://www.hackerearth.com/problem/algorithm/connected-components-in-a-graph/

v,e = input().split(" ")
v,e = int(v),int(e)
al = {}
for _ in range(e):
    i,j = input().split(" ")
    i,j = int(i),int(j)
    if(i in al.keys()):
        al[i].append(j)
    else:
        al[i] = [j]
    if(j in al.keys()):
        al[j].append(i)
    else:
        al[j] = [i]
count = 0
vis = [False for i in range(v+1)]
def solve(vertice):
    vis[vertice] = True
    for i in al[vertice]:
        if(not vis[i]):
            solve(i)
for i in range(1,v+1):
    if(i not in al.keys()):
        count = count + 1
    elif(not vis[i]):
        count = count + 1
        solve(i)
print(count)