# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if(numRows == 1):
            return [[1]]
        if(numRows == 2):
            return ans
        for i in range(3,numRows+1):
            temp = []
            for j in range(len(ans[-1])):
                if(j == 0):
                    temp.append(1)
                else:
                    temp.append(ans[-1][j-1] + ans[-1][j])
            # print(temp,i)
            ans.append(temp + [1])
        return ans 
        