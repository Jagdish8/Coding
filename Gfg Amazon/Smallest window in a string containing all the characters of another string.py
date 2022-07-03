# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        
        h = {}
        for i in p:
            if(i not in h):
                h[i] = 0
            h[i] += 1
            
        i = j = 0
        count = len(h)
        start = 0
        end = len(s) + 1
        while(j < len(s)):
            if(s[j] in h):
                h[s[j]] -= 1
                if(h[s[j]] == 0):
                    count -= 1
            if(count == 0):
                while(count == 0):
                    if(s[i] in h):
                        if(h[s[i]] == 0):
                            count += 1
                        h[s[i]] += 1
                    i += 1
                if(end-start > j - i +1 ):
                    # print(i-1,j,start,end)
                    start = i - 1
                    end = j
            
            j += 1
        
        if(end == len(s)+1):
            return "-1"
        return s[start:end+1]