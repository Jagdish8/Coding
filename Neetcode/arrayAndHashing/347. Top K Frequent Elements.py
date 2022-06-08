https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        # ans = []
        heapify(h)
        m = {}
        for i in nums:
            if(i in m):
                m[i] += 1
            else:
                m[i] = 1
        for i in m:
            # print(m[i],i)
            heappush(h,[m[i],i])
            if(len(h) > k):
                heappop(h)
        return [i[1] for i in h]