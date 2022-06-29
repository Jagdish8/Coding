# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
# Example 2:


# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

# Constraints:

# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi



class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        self.ans = []
        self.flag = False
        
        def solve(source,path):
            
            if(self.flag):
                return
            
            # print(path)
            
            if(len(path) == len(tickets)+1):
                self.ans = path
                self.flag = True
                return
            
            if(source in self.h):
                for i in sorted(self.h[source]): 
                    # if(str(source)+str(i) not in vis):
                    self.h[source].remove(i)
                        # vis.add(str(source)+str(i))
                    solve(i,path+[i])
                    if(self.flag):
                        return
                        # vis.remove(str(source)+str(i))
                    self.h[source].append(i)

        
        self.h={}
        # vis = set()
        for i,j in tickets:
            if(i in self.h.keys()):
                self.h[i].append(j)
            else:
                self.h[i]=[j]
        solve("JFK",["JFK"])
        return self.ans


# we need to find the path such that all tickets are used and tha path should be in smaller lexical order
# reason for not using vis (line 54,56 and 60)
# there are multiple same tickets (So, it'll fail)