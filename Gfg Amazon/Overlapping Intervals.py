# https://practice.geeksforgeeks.org/problems/8a644e94faaa94968d8665ba9e0a80d1ae3e0a2d/1/?page=1&difficulty[]=1&difficulty[]=2&company[]=Amazon&curated[]=1&sortBy=submissions#


class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		nums = sorted(Intervals)
		ans = [nums[0]]
		
		for i in range(1,len(nums)):
		    if(ans[-1][0] <= nums[i][0] <= ans[-1][1]):
		        ans[-1][0] = min(ans[-1][0],nums[i][0])
		        ans[-1][1] = max(ans[-1][1],nums[i][1])
		    else:
		        ans.append(nums[i])
		return ans
