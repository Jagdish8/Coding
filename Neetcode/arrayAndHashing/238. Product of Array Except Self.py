https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        s = 1
        c = 0
        for i in nums:
            if(i == 0):
                c += 1
            else:
                s *= i
        if(c > 1):
            return [0 for i in nums]
        for i in nums:
            if(c > 0):
                if(i != 0):
                    ans.append(0)
                else:
                    ans.append(s)
            else:
                ans.append(s//i)
        return ans