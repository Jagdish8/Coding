# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        
        heap = []
        heapify(heap)
        
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                heappush(heap,[grid[i][j],[i,j]])
        
        row_max = [0]*r
        col_max = [0]*c
        
        while(heap):
            
            val,path = heappop(heap)
            i,j = path[0],path[1]
            ans = max(row_max[i],col_max[j]) + 1
            grid[i][j] = ans
            row_max[i] = ans
            col_max[j] = ans
            
        return grid
            
            

# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/discuss/2413832/Java-%3A%3A-Explained-with-pictures-Priority-Queue-or-O(mn-log(mn))-ttt
# good explaination
            