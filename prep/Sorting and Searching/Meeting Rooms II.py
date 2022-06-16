# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1
 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key = lambda l:(l[0]))
        print(intervals)
        h = []
        heapify(h)
        ans = 0
        res = -1
        for s,e in intervals:
            if(not h):
                ans += 1
                heappush(h,e)
            else:
                if(h and h[0] <= s):
                    while(h and h[0] <= s and ans):
                        ans -= 1
                        heappop(h)
                    ans = ans + 1
                    heappush(h,e)
                else:
                    heappush(h,e)
                    ans += 1
            res = max(res,ans)
            # print(ans,s,e,h)
        return res

# usage of min heap
# works for duplicate intervals as well

# we will be storing the end in the heap
# at top we'll be having the minimum end time which will be ending first

# check code will understand
                
        
        