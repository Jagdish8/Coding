# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if(not temperatures):
            return temperatures
        n = len(temperatures)
        st = [(temperatures[-1],n-1)]
        ans = [0]
        for i in range(n-2,-1,-1):
            while(st and st[-1][0] <= temperatures[i]):
                st.pop()
            if(st):
                ans.append(st[-1][1]-i)
            else:
                ans.append(0)
            st.append((temperatures[i],i))
        return ans[::-1]