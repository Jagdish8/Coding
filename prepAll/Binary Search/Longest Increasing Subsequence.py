# DP solution : T: O(n**2) and  S: O(n)


# Using binary search
# T : O(n log n) S: O(n)

# only works for getting length


# Approach:


# eg  : [1,7,8,4,5,6,-1,9]

# at 1
# add 1 to subsequence
# s = [1]

# at 7
# 7 > 1 add
# s = [1,7]

# at 8
# 8 > 7 add
# s = [1,7,8]

# at 4
# 4 > 8 False
# now subsequence can be
# s1 = [1,7,8]
# s2 = [1,4]

# at 5
# 5 > 8 False
# 5 > 4 add
# s1 = [1,7,8]
# s2 = [1,4,5]

# at 6
# 6 > 8 False
# 6 > 5 add
# s1 = [1,7,8]
# s2 = [1,4,5,6]

# at -1
# -1 > 8 False
# -1 > 6 False
# s1 = [1,7,8]
# s2 = [1,4,5,6]
# s3 = [-1]

# at 9
# 9 > 8 add
# 9 > 6 add
# 9 > -1 add
# s1 = [1,7,8,9]
# s2 = [1,4,5,6,9]
# s3 = [-1,9]

# Longest is s2 with len = 5

# Above is the intuition how it can be done, Instead of creating new subsequence we find the position in
# s where the element can be replaced

# Approach:

# [1,7,8,4,5,6,-1,9]

# at 1
# add 1 to subsequence
# s = [1]

# at 7
# 7 > 1 add
# s = [1,7]

# at 8
# 8 > 7 add
# s = [1,7,8]

# at 4
# 4 > 8 False
# Find the position in s where 4 can be replaced (Binary Search)
# find the index of first element which is greater than 4 in s
# now subsequence will be
# s = [1,4,8]

# at 5
# 5 > 8 False
# Find position
# s = [1,4,5]

# at 6
# 6 > 5 add
# s = [1,4,5,6]

# at -1
# -1 > 6 False
# find position
# s2 = [-1,4,5,6]

# at 9
# 9 > 6 add
# s = [-1,4,5,6,9]


# Here 2 is not the longest increasing subsequence but lenght of s gives the answer


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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
        return len(s)
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