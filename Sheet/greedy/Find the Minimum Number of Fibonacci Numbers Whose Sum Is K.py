# # https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

# Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.

# The Fibonacci numbers are defined as:

# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 for n > 2.
# It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
 

# Example 1:

# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# Example 2:

# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# Example 3:

# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/2642423/2-solutions-python


# intuition
# extra space

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        arr = [1,1]
        while(arr[-1]+arr[-2] <= k):
            arr.append(arr[-1]+arr[-2])
        # print(arr)
        
        count = 0
        if(k in arr):
            return 1
        
        while(True):
            count += 1
            val = self.findMin(k,arr)
            # print(val)
            k -= val
            if(k == 0):
                return count
            
    def findMin(self,target,arr):
        
        # print(target,arr)
        low = 0
        high = len(arr)-1
        
        while(low <= high):
            mid = low + (high -low)//2
            if(arr[mid] == target):
                return target
            elif(arr[mid] >= target):
                high = mid - 1
            else:
                low = mid + 1
        if(high == len(arr)):
            return arr[-1]
        if(high == -1):
            return arr[0]
        return arr[high]



# greedy
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
            
        count = 0
        a = 1
        b = 1
        while(b + a <= k):
            temp = a
            a = b
            b = temp + b
        
        while(True):
            if(b <= k):
                count += 1
                k = k - b
                if(k == 0):
                    return count
            a = b - a  # tricky part
            b = b - a  # tricky part
            