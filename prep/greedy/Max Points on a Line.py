# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        h = {}
        n = len(points)
        ans = -sys.maxsize
        
        if(not points):
            return 0
        
        if(len(points) == 1):
            return 1
        
        for i in range(n-1):
            for j in range(i+1,n):
                
                if((points[j][0] - points[i][0]) == 0):
                    slope = 99.99
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                if(slope not in h):
                    h[slope] = [points[j],points[i]]
                else:
                    if(points[j] not in h[slope]):
                        h[slope].append(points[j])
                    if(points[i] not in h[slope]):
                        h[slope].append(points[i])
            
            # print(h)
            for i in h.values():
                ans = max(ans,len(i))
            h = {}
        
        return ans