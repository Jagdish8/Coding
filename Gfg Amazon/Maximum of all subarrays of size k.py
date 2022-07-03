# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        st = []
        ans = []
        i = j = 0
        while(j < n):

            while(st and st[-1] < arr[j]):
                st.pop()
            st.append(arr[j])
            
            if(j - i + 1 < k):
                j += 1
            else:
                ans.append(st[0])
                if(st[0] == arr[i]):
                    st.pop(0)
                i += 1
                j += 1
        return ans