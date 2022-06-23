# You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

# Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"
# Example 2:

# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.
 

# Constraints:

# -109 <= lower <= upper <= 109
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        l = []
        if not nums:
            if(upper == lower):
                return [str(upper)]
            return [str(lower)+"->"+str(upper)]
        if(nums[0]>lower):
            if(nums[0] == lower+1):
                l.append(str(lower))
            else:
                l.append(str(lower)+"->"+str(nums[0]-1))
        for i in range(1,len(nums)):
            if(nums[i-1] == nums[i]-1):
                continue
            elif(nums[i-1] == nums[i]-2):
                l.append(str(nums[i]-1))
            else:
                l.append(str(nums[i-1]+1)+"->"+str(nums[i]-1))
        if(nums[-1]<upper):
            if(nums[-1] == upper - 1):
                l.append(str(upper))
            else:
                l.append(str(nums[-1]+1)+"->"+str(upper))
        return l
                
                        
# use