https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums):
            l = 0
            h = len(nums)-1
            while(l <= h):
                m = l + (h-l)//2
                if(nums[m] == target):
                    return True
                elif(nums[m]>target):
                    h = m - 1
                else:
                    l = m + 1
            return False
        for i in matrix:
            if(i[0]<= target and i[-1]>=target):
                return search(i)