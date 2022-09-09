# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums = sorted(nums)
        prefix = [nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1]+i)
            
        def bi(arr,target):
        
            if(target > arr[-1]):
                return len(arr)
            if(target < arr[0]):
                return 0
            
            low = 0
            high = len(arr)-1
            while(low <= high):
                mid = low + (high - low)//2
                if(arr[mid] <= target):
                    low = mid + 1
                else:
                    high = mid - 1
            return low
                    
        ans = []
        for i in queries:
            ans.append(bi(prefix,i))
        return ans