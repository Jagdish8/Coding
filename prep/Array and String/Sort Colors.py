# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # usual way

        # c1 = c2 = c3 = 0
        # for i in nums:
        #     if(i == 0):
        #         c1 += 1
        #     elif(i == 1):
        #         c2 += 1
        #     else:
        #         c3 += 1
        # # print(c1,c2,c3)
        # index = 0
        # while(c1):
        #     nums[index] = 0
        #     index += 1
        #     c1 -= 1
        # while(c2):
        #     nums[index] = 1
        #     index += 1
        #     c2 -= 1
        # while(c3):
        #     nums[index] = 2
        #     index += 1
        #     c3 -= 1
            

        # in one pass
        p0 = cur = 0
        p2 = len(nums) - 1
        
        while(cur <= p2):
            
            if(nums[cur] == 0):
                nums[cur],nums[p0] = nums[p0],nums[cur]
                p0 += 1
                cur += 1
            elif(nums[cur] == 1):
                cur += 1
            else:
                nums[cur],nums[p2] = nums[p2],nums[cur]
                p2 -= 1