# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# https://www.youtube.com/watch?v=w36ekZYq-Ms

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while(low <= high):
            
            mid = low + (high-low)//2
            
            count = 0
            for i in range(len(matrix)):
                count += self.findCount(matrix[i],mid)
            
            if(count < k):
                low = mid + 1
            else:
                high = mid - 1
        
        return low
                
    def findCount(self,arr,x):
        
        low = 0
        high = len(arr)-1
        while(low <= high):
            
            mid = low + (high - low)//2
            
            if(arr[mid] > x):
                high = mid - 1
            else:
                low = mid + 1
        
        return low