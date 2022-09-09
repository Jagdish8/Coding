# https://practice.geeksforgeeks.org/problems/largest-rectangular-sub-matrix-whose-sum-is-0/1?page=1&category[]=prefix-sum&sortBy=submissions


# code gives wrong ans but idea is correct
# https://www.youtube.com/watch?v=xbA4E70kcKE
class Solution:
    def sumZeroMatrix(self, a : List[List[int]]) -> List[List[int]]:
        # code here
        m = len(a)
        n = len(a[0])
        start_row = end_row = start_col = end_col = 0
        ans_j = 0
        final_max_len = 0
        for cstart in range(n):
            temp = [0]*m
            for cend in range(cstart,n):
                for x in range(m):
                    temp[x] += a[x][cend]
                max_len, ending_row = self.findSum(temp)
                # print(max_len,ending_row)
                if(max_len > final_max_len):
                    final_max_len = max_len
                    start_row = max_len - ending_row - 1
                    end_row = ending_row
                    start_col = cstart
                    end_col = cend
        ans = []
        for i in range(start_row,end_row+1):
            temp = []
            for j in range(start_col,end_col+1):
                temp.append(a[i][j])
            ans.append(temp)
        return ans
            
                
    def findSum(self,arr):
        h = {0:-1}
        prefix_sum = 0
        max_len = 0
        end = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if(prefix_sum in h):
                if(max_len < i - h[prefix_sum]):
                    end = i
                    max_len = i - h[prefix_sum]
            else:
                h[prefix_sum] = i
        return [max_len,end]
                