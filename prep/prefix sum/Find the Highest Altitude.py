# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        n = len(gain)
        prefix = 0
        max_alti = 0
        
        for i in range(n):
            
            prefix += gain[i]
            max_alti = max(max_alti,prefix)
            
        return max_alti