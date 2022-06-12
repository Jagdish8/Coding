https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if(len(arr)==1):
            return 0
        if(arr[0]==arr[-1]):
            return 1
        n = len(arr)-1
        h = {}
        for i in range(len(arr)):
            if(arr[i] in h):
                h[arr[i]].append(i)
            else:
                h[arr[i]] = [i]
        vis = [False for i in arr]
        vis[0] = True
        q = collections.deque()
        q.append(0)
        steps = 0
        while(q):
            for i in range(len(q)):
                index = q.popleft()
                if(index == n):
                    return steps
                if(index-1 >= 0 and not vis[index-1]):
                    q.append(index-1)
                    vis[index-1] = True
                if(index+1 <= n and not vis[index+1]):
                    q.append(index+1)
                    vis[index+1] = True
                if(arr[index] in h):
                    for i in h[arr[index]]:
                        if(not vis[i]):
                            q.append(i)
                    del h[arr[index]]
            steps += 1
        return steps