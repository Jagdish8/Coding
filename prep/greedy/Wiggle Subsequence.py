# https://leetcode.com/problems/wiggle-subsequence/

# using O(N**2) using dp

def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if(len(nums) < 2):
            return len(nums)
        
        down = [0]*len(nums)
        up = [0]*len(nums)
        
        for i in range(1,len(nums)): 
            for j in range(i):
                if(nums[i] > nums[j]): 
                    up[i] = max(up[i],down[j] + 1)
                elif(nums[j] > nums[i]):
                    down[i] = max(down[i], up[j] + 1)
        return max(up[-1],down[-1]) + 1


# optimising above to O(N)

down = [1]*len(nums)
up = [1]*len(nums)

for i in range(1,len(nums)): 
    if(nums[i] > nums[i-1]): 
        up[i] = down[i-1] + 1
        down[i] = down[i-1]   
    elif(nums[i-1] > nums[i]):
        down[i] = up[i-1] + 1
        up[i] = up[i-1] 
    else:
        up[i] = up[i-1]
        down[i] = down[i-1]        
return max(up[-1],down[-1])

# optimising above to O(1) space

down = up = 1
for i in range(1,len(nums)):
    if(nums[i] > nums[i-1]): 
        up = down + 1
    elif(nums[i-1] > nums[i]):
        down = up + 1
return max(up,down)