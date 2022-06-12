https://leetcode.com/problems/hand-of-straights/

class Solution:
    def isNStraightHand(self, nums: List[int], groupSize: int) -> bool:
        if(len(nums)%groupSize):
            return False
        if(groupSize == 1):
            return True
        # nums = sorted(hand)
        h = {}
        for i in nums:
            if(i in h):
                h[i] += 1
            else:
                h[i] = 1
        # print(h)
        while(h):
            m = min(h.keys())
            n = groupSize
            # print(m)
            # print(h)
            while(n):
                # print(m)
                if(m+1 not in h.keys() and n != 1):
                    return False
                h[m] -= 1
                if(h[m] == 0):
                    del h[m]
                m = m+1
                n -= 1
                # print(n)
        return True
                