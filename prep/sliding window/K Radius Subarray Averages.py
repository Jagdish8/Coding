# https://leetcode.com/problems/k-radius-subarray-averages/


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        if(k >= n):
            return [-1]*n
        ans = [-1]*n
        og = k
        k = 2*k + 1
        
        
        s = 0
        i = j = 0
        
        while(j < n):
            
            if(j - i + 1 < k):
                s += nums[j]
                j += 1
                
            elif(j - i + 1 == k):
                s += nums[j]
                ans[j-og] = s//k
                j += 1
                
            else:
                s -= nums[i]
                i += 1
                
        return ans
        