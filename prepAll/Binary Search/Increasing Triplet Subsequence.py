# Variation of Longest Increasing Subsequence
# first do Longest Increasing Subsequence In same folder

Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        s = []
        for i in nums:
            if(not s):
                s.append(i)
            else:
                if(i>s[-1]):
                    s.append(i)
                else:
                    pos = self.findPos(i,s)
                    s[pos] = i
            if(len(s) > 2):
                return True
        return False
    
    
    def findPos(self,target,s):
        
        # find first number which is greater than target
        
        l = 0
        h = len(s)-1
        res = 0
        while(l <= h):
            m = l + (h-l)//2
            if(s[m] == target):
                return m
            elif(s[m] > target):
                res = m
                h = m - 1
            else:
                l = m + 1
        return res
                
                    
        

 