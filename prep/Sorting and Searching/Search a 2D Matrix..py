# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m - 1
        ans = -1
        
        if(not n):
            return False
        
        if(m == 1 and n == 1):
            if(matrix[0][0] == target):
                return True
            return False
        
        while(low <= high):
            mid = low + (high - low)//2
            # print(low,high,mid)
            if(matrix[mid][0] <= target <= matrix[mid][-1]):
                ans = mid
                break
            elif(matrix[mid][-1] > target):
                high = mid - 1
            else:
                low = mid + 1
                
        if(ans == -1):
            return False
        
        low = 0
        high = n - 1
        while(low <= high):
            mid = low + (high - low)//2
            if(matrix[ans][mid] == target):
                return True
            elif(matrix[ans][mid] > target):
                high = mid - 1
            else:
                low = mid + 1
        return False


# Intuition, since the rows are sorted, columns are sorted as well, thus we can do 2 binary search to locate the exact position of target
# First, handle special cases. e.g. [], [[]]
# Second, binary search on rows, to locate row number
# If not found, return False
# Third, once we have row number, binary search on columns
# If not found, return False, else return True
# Time Complexity O(lgm + lgn) == O(lg(mn))