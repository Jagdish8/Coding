# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        minimum_value = sys.maxsize
        prefix_sum = 0
        
        for i in nums:
            
            prefix_sum += i
            minimum_value = min(minimum_value,prefix_sum)
        
        if(minimum_value < 1):
            return (- minimum_value) + 1
        return 1