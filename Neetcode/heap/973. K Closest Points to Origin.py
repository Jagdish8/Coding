https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = []
        heapify(l)
        for x,y in points:
            d = (x**2 + y**2)**0.5
            if(len(l) >= k):
                if(-d < l[0][0]):
                    continue
                heappop(l)
            heappush(l,(-1*d,[x,y]))
        res = []
        for i in l:
            res.append(i[1])
        return res