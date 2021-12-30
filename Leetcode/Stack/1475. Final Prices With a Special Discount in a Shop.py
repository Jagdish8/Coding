# Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

# Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

 

# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount at all.
# Example 3:

# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if(not prices):
            return []
        st=[(prices[-1],len(prices)-1)]
        ans = [(prices[-1],len(prices)-1)]
        for i in range(len(prices)-2,-1,-1):
            if(st[-1][0] <= prices[i]):
                ans.append(st[-1])
            else:
                while(st and st[-1][0] > prices[i]):
                    st.pop()
                if(st):
                    ans.append(st[-1])
                else:
                    ans.append((prices[i],i))
            st.append((prices[i],i))
        ans = ans[::-1]
        print(ans)
        res=[]
        for i in range(len(ans)):
            if(ans[i][0] == prices[i]):
                if(ans[i][1] != i):
                    res.append(prices[i]-ans[i][0])
                else:
                    res.append(ans[i][0])
            else:
                res.append(prices[i]-ans[i][0])
        return res