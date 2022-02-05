# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.n = len(nums)
        self.lock = False
        self.res = ""
        def solve(com):
            if(len(com) == self.n):
                if(com not in nums):
                    self.res = com
                    self.lock = True
                return
            # for i in:
            if(self.lock):
                return
            solve(com+"0")
            solve(com+"1")
        solve("")
        return self.res
                    
        