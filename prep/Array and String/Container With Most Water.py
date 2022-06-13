# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)-1
        area=0
        i=0
        while(i<=n):
            # print(area,i,n)
            area=max(area,min(height[i],height[n])*(n-i))
            if(height[i]>height[n]):
                n-=1
            else:
                i+=1
        return area


# start from  start and end
# between 2 pillars always the smallest is considered as the height


# eg : [1,8,6,2,5,4,8,3,7]  start = 1 end = 7
# area = (8-0+1)*min(1,7) = 9
# now, since start is min and if we move end to end-1, it doesn't same sense since again we will get
# start as minimum or end as minimum which will be even smaller than start(1)
# therefore, move the smaller one ahead , either start = start + 1

# and again same continues