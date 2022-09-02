https://leetcode.com/problems/insert-interval/


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        index = 0
        n = len(intervals)
        ans = []
        
        while(index < n and newInterval[0] > intervals[index][0]):
            ans.append(intervals[index])
            index += 1
            
        # print(ans)
        
        if(ans and ans[-1][0] <= newInterval[0] <= ans[-1][1]):
            ans[-1][1] = max(ans[-1][1],newInterval[1])
        else:
            ans.append(newInterval)
            
        while(index < n):
            if(ans[-1][0] <= intervals[index][0] <= ans[-1][1]):
                ans[-1][1] = max(ans[-1][1],intervals[index][1])
            else:
                ans.append(intervals[index])
            index += 1
            
        return ans
            
# Intervals is already sorted,  O(N) O(N)