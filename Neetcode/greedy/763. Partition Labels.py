https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h = {}
        for i,j in enumerate(s):
            h[j] = i
        i = 0
        m = 0
        ans = []
        # print(h)
        while(i<len(s)):
            m = max(m, h[s[i]])
            # print(m,i)
            if(h[s[i]] > i):
                i += 1
            elif(h[s[i]] == i):
                if(h[s[i]] == m):
                    if(ans):
                        ans.append(i+1-sum(ans))
                    else:
                        ans.append(i+1)
                del h[s[i]]
                i += 1
        # res = [ans[0]]
        # for i in range(len(ans)-1):
        #     res.append()
        return ans
                    