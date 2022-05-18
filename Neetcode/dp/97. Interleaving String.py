https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1)+len(s2)!=len(s3)):
            return False
        self.h = {}
        def solve(x,y,z):
            # print(x,y,z)
            if(x == len(s1) and y == len(s2) and z == len(s3)):
                return True
            if(x == len(s1)):
                if(s2[y:] == s3[z:]):
                    return True
                return False
            if(y == len(s2)):
                if(s1[x:] == s3[z:]):
                    return True
                return False
            if((x,y,z) in self.h):
                return self.h[(x,y,z)]
            if(s1[x] == s2[y] == s3[z]):
                self.h[(x,y,z)] = solve(x+1,y,z+1) or solve(x,y+1,z+1)
                return self.h[(x,y,z)]
            if(s1[x] == s3[z]):
                self.h[(x,y,z)] = solve(x+1,y,z+1)
                return self.h[(x,y,z)]
            if(s2[y] == s3[z]):
                self.h[(x,y,z)] = solve(x,y+1,z+1)
                return self.h[(x,y,z)]
            return False
        return solve(0,0,0)
        