https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        i = j = 0
        n = len(nums)
        ans = []
        while(j<n):
            while(l and nums[j] > l[-1]):
                l.pop()
            l.append(nums[j])
            if(j-i+1 < k):
                j += 1
            else:
                ans.append(l[0])
                if(l[0] == nums[i]):
                    l.pop(0)
                i += 1
                j += 1
            # print(l)
        return ans
                
        
        