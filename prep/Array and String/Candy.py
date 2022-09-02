# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)

        #using two arays 
        # one pass from left side and one pass from right side

#         left = [1]*n
#         right = [1]*n
        
#         for i in range(1,n):
#             if(ratings[i] <= ratings[i-1]):
#                 left[i] = 1
#             elif(ratings[i] > ratings[i-1]):
#                 left[i] = left[i-1] + 1

#         for i in range(n-2,-1,-1):
#             if(ratings[i] <= ratings[i+1]):
#                 right[i] = 1
#             elif(ratings[i] > ratings[i+1]):
#                 right[i] = right[i+1] + 1

#         print(left,right)
#         ans = []
#         for i,j in zip(left,right):
#             ans.append(max(i,j))
#         return sum(ans)


        # using one array
        # two passes, one from left side and one from right side 
        ans = [1]*n
        for i in range(1,n):
            if(ratings[i] <= ratings[i-1]):
                ans[i] = 1
            elif(ratings[i] > ratings[i-1]):
                ans[i] = ans[i-1] + 1

        for i in range(n-2,-1,-1):
            if(ratings[i] <= ratings[i+1]):
                ans[i] = max(1,ans[i])
            elif(ratings[i] > ratings[i+1]):
                ans[i] = max(ans[i+1] + 1,ans[i])
        return sum(ans)
                
# simple logic

# first we go from left and compare the values of current index with previous index
# if greater than we increament it to previous ans + 1
# # else change it to 1

# we have to it from right side as well because of the example [1,2,87,87,87,2,1]
# if we only do it from left the ans would be [1,2,3,1,2,2,1]
# but correct ans is [1,2,3,1,3,2,1]

# thats why when we do it from right we get [1,2,2,1,3,2,1]

# now from both left and right choose the max and return sum

# can be efficient with one array, done in code