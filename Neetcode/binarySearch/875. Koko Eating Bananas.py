https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high
        while(low <= high):
            m = low + (high-low)//2
            time = 0
            for i in piles:
                time += math.ceil(i/m)
            if(time<=h):
                res = min(res,m)
                high = m - 1
            else:
                low = m + 1
        return res