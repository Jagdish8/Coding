https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = {}
        print(s1,s2)
        for i in s1:
            if(i not in h):
                h[i] = 0
            h[i] += 1
        count = len(h)
        i = j = 0
        while(j<len(s2)):
            if(s2[j] in h):
                h[s2[j]] -= 1
                if(h[s2[j]] == 0):
                    count -= 1
            print(s2[j],i,j,h,count)
            if(j-i+1 < len(s1)):
                j += 1
            elif(j-i+1 == len(s1)):
                if(count == 0):
                    return True
                if(s2[i] in h):
                    if(h[s2[i]] == 0):
                        count += 1
                    h[s2[i]] += 1
                i += 1
                j += 1  
        if(count == 0):
            return True
        return False
            