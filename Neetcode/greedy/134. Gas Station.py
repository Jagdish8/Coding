https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        s = 0
        re = 0
        for i in range(len(gas)):
            re = re + gas[i] - cost[i]
            if(re<0):
                s = i + 1
                re = 0
        return s