https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for k in range(len(nums)):
            i = k+1
            j = len(nums)-1
            while(i<j):
                if(nums[i]+nums[j]+nums[k] == 0):
                    ans.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
                elif(nums[i]+nums[j]+nums[k] > 0):
                    j -= 1
                else:
                    i += 1
        return ans