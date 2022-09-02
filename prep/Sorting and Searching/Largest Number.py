# https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            
            length = len(nums)//2
            
            l = merge_sort(nums[:length])
            r = merge_sort(nums[length:])
            return merge(l,r)
        
        def merge(l,r):
            # print(l,r)
            result = []
            i= 0
            j= 0
            while i<len(l) and j<len(r):
                if int(str(l[i])+str(r[j])) >int(str(r[j])+str(l[i])):
                    result.append(l[i])
                    i+=1
                else:
                    result.append(r[j])
                    j+=1
            while i<len(l):
                result.append(l[i])
                i+=1
            while j<len(r):
                result.append(r[j])
                j+=1
            return result
        
        new_nums = merge_sort(nums)
        return str(int("".join(map(str,new_nums)))) 

# merge sort
# clean