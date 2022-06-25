# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false



class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if(n==0):
            return True
        if(n==1 and len(flowerbed)==1 and flowerbed[0] == 0):
            return True
        if(n==1 and len(flowerbed)==1 and flowerbed[0] == 1):
            return False
        for i in range(len(flowerbed)):
            if(i == 0):
                if(flowerbed[i] == 0 and flowerbed[i+1]==0):
                    n = n - 1
                    flowerbed[i] = 1
            elif(flowerbed[i] == 0 and i == len(flowerbed)-1):
                if(flowerbed[i-1]==0):
                    n = n - 1
                    flowerbed[i] = 1
            else:
                if(flowerbed[i] == 0 and flowerbed[i-1]==0 and flowerbed[i+1] == 0):
                    n = n - 1
                    flowerbed[i] = 1
            if(n == 0):
                return True
        return False

# can be written in better way