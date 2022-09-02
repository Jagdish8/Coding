# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = version1.split(".")
        for i,j in enumerate(one):
            one[i] = int(j)
        two = version2.split(".")
        for i,j in enumerate(two):
            two[i] = int(j)
        # print(one,two)
        i = 0
        while(i<len(one) and i<len(two)):
            if(one[i] == two[i]):
                i += 1
            elif(one[i] > two[i]):
                return 1
            else:
                return -1
        # print(i)
        if(i<len(one)):
            while(i<len(one) and one[i] == 0):
                i += 1
            if(i<len(one)):
                return 1
        if(i<len(two)):
            while(i<len(two) and two[i] == 0):
                i += 1
            if(i<len(two)):
                return -1
        return 0
        
        