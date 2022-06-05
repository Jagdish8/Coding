https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def bins(self,nums,target):
        # print(nums)
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = low + (high-low)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        index = self.findMinIndex(nums)
        one = self.bins(nums[:index],target)
        two = self.bins(nums[index:],target)
        if(one != -1):
            return one
        if(two == -1):
            return -1
        return index + two
    def findMinIndex(self,nums):
        if(nums[0]<=nums[-1]):
            return 0
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low)//2
            if(nums[mid] > nums[mid+1]):
                return mid+1
            elif(nums[low]<=nums[mid]):
                low = mid + 1
            else:
                high = mid - 1
            
                