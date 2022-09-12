# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# TLE O(2**N)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        
        self.ans = 0
        def solve(prices,k,s,choice):
            
            if(k == 0 or not prices):
                self.ans = max(self.ans,s)
                return self.ans
            if(choice == ""):
                return max(solve(prices[1:],k,s,""),solve(prices[1:],k-1,s-prices[0],"buy"))
            elif(choice == "buy"):
                return max(solve(prices[1:],k,s,"buy"),solve(prices[1:],k-1,s+prices[0],"sell"))
            else:
                return max(solve(prices[1:],k,s,""),solve(prices[1:],k-1,s-prices[0],"buy"))
            
        return solve(prices,k*2,0,"")

# TLE
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        self.h = {}
        def solve(index,k,s,choice):
            
            if((index,k,s,choice) in self.h):
                # print("hi")
                return self.h[(index,k,s,choice)]
            
            if(k == 0 or index == len(prices)):
                self.h[(index,k,s,choice)] = s
                return s
            
            if(choice == ""):
                ans = max(solve(index + 1,k,s,""),solve(index + 1,k-1,s-prices[index],"buy"))
                self.h[(index,k,s,choice)] = ans
                return ans
            
            elif(choice == "buy"):
                ans = max(solve(index + 1,k,s,"buy"),solve(index + 1,k-1,s+prices[index],"sell"))
                self.h[(index,k,s,choice)] = ans
                return ans
            
            else:
                ans = max(solve(index + 1,k,s,""),solve(index + 1,k-1,s-prices[index],"buy"))
                self.h[(index,k,s,choice)] = ans
                return ans
            
        return solve(0,k*2,0,"")

# TLE
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.h = {}
        def solve(index,k,s,choice):
            
            if((index,k,s,choice) in self.h):
                return self.h[(index,k,s,choice)]
            
            if(k == 0 or index == len(prices)):
                self.h[(index,k,s,choice)] = s
                return s
            
            if(choice == "buy"):
                ans = max(solve(index + 1,k,s,"buy"),solve(index + 1,k-1,s-prices[index],"sell"))
                self.h[(index,k,s,choice)] = ans
                return ans
            
            else:
                ans = max(solve(index + 1,k,s,"sell"),solve(index + 1,k-1,s+prices[index],"buy"))
                self.h[(index,k,s,choice)] = ans
                return ans
            
        return solve(0,k*2,0,"buy")

# Accepted O(n*k)
class Solution: 
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.h = {}
        def solve(index,k,choice):
            
            if((index,k,choice) in self.h):
                return self.h[(index,k,choice)]
            
            if(k == 0 or index == len(prices)):
                return 0
            
            if(choice == "buy"):
                ans = max(solve(index + 1,k,"buy"),-prices[index] + solve(index + 1,k-1,"sell"))
                self.h[(index,k,choice)] = ans
                return ans
            
            else:
                ans = max(solve(index + 1,k,"sell"),prices[index] + solve(index + 1,k-1,"buy"))
                self.h[(index,k,choice)] = ans
                return ans
            
        return solve(0,k*2,"buy")
    
# just because of the one parameter it got accepted, just removed sum from the solve parameter