# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# using prefix sum O(n**2)
class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        s = nums[0]
        
        for i in range(1,n):
            s += nums[i]
            prefix[i] = prefix[i-1]+nums[i]
            
        # print(prefix)
        
        for i in range(n):
            for j in range(i+1,n):
                if(not (j-i) % 2):
                    # print(j,i)
                    s += prefix[j] - prefix[i] + nums[i]
        
        return s
                    
# greedy approach O(n)
# https://www.youtube.com/watch?v=J5IIH35EBVE
class Solution:
    def sumOddLengthSubarrays(self, nums: List[int]) -> int:
        
        res = 0
        n = len(nums)
        
        for i in range(n):
            total_count = (n-i)*(i+1)
            odd_count = math.ceil(total_count/2)
            res += odd_count * nums[i]
        
        return res
                    
                    