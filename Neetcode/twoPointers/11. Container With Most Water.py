https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        area=0
        i=0
        while(i<n):
            print(area,i,n)
            area=max(area,min(height[i],height[n-1])*(n-i-1))
            if(height[i]>height[n-1]):
                n-=1
            else:
                i+=1
        return area