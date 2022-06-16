# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # using sort and extra space
        # O(nlogn)

        intervals = sorted(intervals)
        ans = [intervals[0]]
        # print(intervals)
        for s,e in intervals[1:]:
            if(ans[-1][0] <= s <= ans[-1][1]):
                ans[-1][1] = max(ans[-1][1],e)
                ans[-1][0] = min(ans[-1][0],s)
            else:
                ans.append([s,e])
        return ans
        

