# https://leetcode.com/problems/range-addition/

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        ans = [0]*length
        
        for i,j,inc in updates:
            ans[i] += inc
            if(j+1 < length):
                ans[j+1] -= inc
        
        for i in range(1,length):
            ans[i] = ans[i] + ans[i-1]
        
        return ans

# whatever