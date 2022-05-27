https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapify(h)
        for i in stones:
            # print(i)
            heappush(h,-i)
        while(len(h)!=1):
            a = heappop(h)*-1
            b = heappop(h)*-1
            heappush(h,-(a-b))
        return -1*heappop(h)
        