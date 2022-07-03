# https://practice.geeksforgeeks.org/problems/rearrange-characters4649/1/?page=2&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions


class Solution :
    def rearrangeString(self, str):
        
        max_count = 0
        max_count_char = ""
        count = [0 for i in range(26)]
        for i in str:
            count[ord(i)-ord("a")] += 1
            if(count[ord(i)-ord("a")] > max_count):
                max_count = count[ord(i)-ord("a")]
                max_count_char = i
        
        n = len(str)
        
        # important negative condition
        if(max_count > (n+1)//2):
            return ""
        
        res = [None]*n
        index = 0
        while(max_count != 0):
            res[index] = max_count_char
            max_count -= 1
            index += 2
            
        count[ord(max_count_char)-ord("a")] = 0
             
        for i in range(26):
            while(count[i] > 0):
                if(index >= n):
                    index = 1
                res[index] = chr(i + ord('a'))
                index += 2
                count[i] -= 1
                
        return "".join(res)