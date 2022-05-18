https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ans = 0
        self.d = {}
        def solve(did,i):
            if(i == len(prices)):
                return 0
            elif((did,i) in self.d):
                return self.d[(did,i)]
            elif(did == ""):
                self.d[(did,i)] = max(solve("",i+1),-prices[i]+solve("buy",i+1))
            elif(did == "buy"):
                self.d[(did,i)] = max(solve("buy",i+1),prices[i]+solve("sell",i+1))
            elif(did == "sell"):
                self.d[(did,i)] = solve("cooldown",i+1)
            elif(did == "cooldown"):
                self.d[(did,i)] = max(solve("",i+1),-prices[i]+solve("buy",i+1))
            return self.d[(did,i)]
        return solve("",0)