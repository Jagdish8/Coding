# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # O(nlogn) O(1)
#         nums.sort()

#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i-1]:
#                 if nums[i] == nums[i-1]+1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1

#         return max(longest_streak, current_streak)


        # O(n) O(n)
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
# For those who got confused by if the last solution is O(n^2) or O(n),
#  please take a close look at the entering of the logic: if(!num_set.contains(num-1)).
            
# That means, for example, 6,5,4,3,2,1 input,
#  only the value 1 is valid for the loop(all other values have its value - 1 in the set),
#  that is O(n).

# Another corner example, 2, 5, 6, 7, 9, 11.
#  All of these numbers are the "entrance" for the logic but the while loop doesn't run much.
#  That is O(n) as well.