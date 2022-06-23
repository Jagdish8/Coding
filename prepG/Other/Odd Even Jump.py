# # You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

# # You may jump forward from index i to index j (with i < j) in the following way:

# # During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
# # During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
# # It may be the case that for some index i, there are no legal jumps.
# # A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

# # Return the number of good starting indices.


# Example 1:

# Input: arr = [10,13,12,14,15]
# Output: 2
# Explanation: 
# From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
# From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
# From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
# From starting index i = 4, we have reached the end already.
# In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
# jumps.
# Example 2:

# Input: arr = [2,3,1,1,4]
# Output: 3
# Explanation: 
# From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
# During our 1st jump (odd-numbered), we first jump to i = 1 because arr[1] is the smallest value in [arr[1], arr[2], arr[3], arr[4]] that is greater than or equal to arr[0].
# During our 2nd jump (even-numbered), we jump from i = 1 to i = 2 because arr[2] is the largest value in [arr[2], arr[3], arr[4]] that is less than or equal to arr[1]. arr[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not i = 3
# During our 3rd jump (odd-numbered), we jump from i = 2 to i = 3 because arr[3] is the smallest value in [arr[3], arr[4]] that is greater than or equal to arr[2].
# We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
# In a similar manner, we can deduce that:
# From starting index i = 1, we jump to i = 4, so we reach the end.
# From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
# From starting index i = 3, we jump to i = 4, so we reach the end.
# From starting index i = 4, we are already at the end.
# In total, there are 3 different starting indices i = 1, i = 3, and i = 4, where we can reach the end with some
# number of jumps.
# Example 3:

# Input: arr = [5,1,3,4,2]
# Output: 3
# Explanation: We can reach the end from starting indices 1, 2, and 4.
 

# Constraints:

# 1 <= arr.length <= 2 * 104
# 0 <= arr[i] < 105



# here the 1st 2nd 3rd ..... are the jump order (not related to index nor value at the index)


#  [10,13,12,14,15]

# At index --> 0 value 10
# 1st jump, smallest value which is greater than 10 
#             we have 12 at index 2, jump to index 2
# 2nd jump, we're at index 2 value 12 , largest value which is smaller than 12
#             No such values, Therfore False

# At index --> 1 value 13
# 1st jump, smallest value which is greater than 13 
#             we have 14 at index 3, jump to index 3
# 2nd jump, we're at index 3 value 14 , largest value which is smaller than 14
#             No such values, Therfore False


# At index --> 2 value 12
# 1st jump, smallest value which is greater than 12 
#             we have 14 at index 3, jump to index 3
# 2nd jump, we're at index 3 value 14 , largest value which is smaller than 14
#             No such values, Therfore False

# At index --> 3 value 14
# 1st jump, smallest value which is greater than 14 
#             we have 15 at index 4, jump to index 4
#             4 is the last index: therfore index 3 is good
#     Count = 1

# At index 4 -- > value 15
#             4 is the last index: therfore index 4 is good
#     Count = 2

# ANSWER : 2


# USING MEMOIZATION:  (TLE 60/65)

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        if(len(arr) == 1):
            return 1
        if(len(arr) == 2):
            if(arr[0] <= arr[1]):
                return 2
            return 1
        h = {}
        count = 0
        def solve(index,value,flag):
            if(index == len(arr)-1):
                return True
            if(flag):
                flag = False
                ans = sys.maxsize
                temp = -1
                for j in range(index+1,len(arr)):
                    if(arr[j] < ans and arr[j] >= value):
                        temp = j
                        ans = arr[j]
                if(ans != sys.maxsize):
                    if((temp,ans,flag) in h):
                        h[(index,value,True)] = h[(temp,ans,flag)]
                        return h[(index,value,True)]
                    else:
                        h[(index,value,True)] = solve(temp,ans,flag)
                        return h[(index,value,True)]
                else:
                    h[(index,value,True)] = False
                    return False
            else:
                flag = True
                ans = -sys.maxsize
                temp = -1
                for j in range(index+1,len(arr)):
                    if(arr[j] > ans and arr[j] <= value):
                        temp = j
                        ans = arr[j]
                if(ans != -sys.maxsize):
                    if((temp,ans,flag) in h):
                        h[(index,value,False)] = h[(temp,ans,flag)]
                        return h[(index,value,False)]
                    else:
                        h[(index,value,False)] = solve(temp,ans,flag)
                        return h[(index,value,False)]
                else:
                    h[(index,value,False)] = False
                    return False
        for i,j in enumerate(arr):
            if((i,j,True) in h):
                if(h[(i,j,True)]):
                    count += 1
            else:
                if(solve(i,j,True)):
                    count += 1
        return count


