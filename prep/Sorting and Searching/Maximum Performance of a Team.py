# # https://leetcode.com/problems/maximum-performance-of-a-team/

# https://www.youtube.com/watch?v=vlZYnDtJayw

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        candidates = zip(efficiency,speed)
        candidates = sorted(candidates)
        
        h = []
        heapify(h)
        s = 0
        ans = 0
        
        for i in range(len(candidates)-1,-1,-1):
            
            s += candidates[i][1]
            heappush(h,candidates[i][1])
            if(len(h) > k):
                s -= heappop(h)
            ans = max(ans,s*candidates[i][0])
        
        return ans % (10**9 + 7)
                    
                