# https://leetcode.com/problems/find-original-array-from-doubled-array/

# An integer array original is transformed into a doubled array changed by appending twice
#  the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not
#  a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# Example 2:

# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
# Example 3:

# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
 

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if(len(changed) % 2):
            return []
        
        changed = sorted(changed)
        h = {}
        
        for i in changed:
            if(i not in h):
                h[i] = 0
            h[i] += 1

        ans = []
        for i in changed:
            
            if(i == 0):
                if(h[i]%2):
                    return []
                else:
                    count = h[0]//2
                    while(count):
                        count -= 1
                        ans.append(0)
                    h[0] = 0
                    
            elif(i * 2 in h):
                while(h[i] > 0 and h[i*2] > 0):
                    ans.append(i)
                    h[i] -= 1
                    h[i*2] -= 1
                if(h[i] > 0):
                    return []

                    
        if(len(ans) != len(changed)//2):
            return []
        
        return ans
        
        