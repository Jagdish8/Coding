# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        heapify(h)
        intervals = sorted(intervals)
        # Input: intervals = [[0,30],[5,10],[15,20]]
        # Output: 2
        res = 0
        for s,e in intervals:
            # print(res,s,e,h)
            if(not h):
                heappush(h,e)
            else:
                while(h and h[0] <= s):
                    heappop(h)
                heappush(h,e)
            res = max(res,len(h))
        return res