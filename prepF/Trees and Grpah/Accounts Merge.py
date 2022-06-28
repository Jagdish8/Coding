# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Example 2:

# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

# Constraints:

# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        
        em_to_name = {}
        em_graph = {}
        
        for acc in accounts:
            name = acc[0]
            
            # making a graph of common connected gmail
            # all acc the gamil start with 1 index
            for email in acc[1:]:
                
                # connect 1st to 2nd email
                if(acc[1] not in em_graph):
                    em_graph[acc[1]] = set()
                em_graph[acc[1]].add(email)
                
                #connect 2nd to 1st email
                if(email not in em_graph):
                    em_graph[email] = set()
                em_graph[email].add(acc[1])
                
                # create a hashmap
                # it help us to find the email owners
                em_to_name[email] = name
                
        # print(em_graph)
        # print(em_to_name)
    
        seen = set()
        ans = []
        
        # dfs function
        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            self.component.append(s)
            for nei in em_graph[s]:
                if nei not in seen :
                    dfs(nei)
        
        # here we use loop to traverse all unconnected
        # components of the graph
        for email in em_graph:
            if email not in seen:
                self.component = []
                dfs(email)
                ans.append([em_to_name[email]] + sorted(self.component))
                
        return ans   



# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
#                   ["John","johnsmith@mail.com","john00@mail.com"],
#                   ["Mary","mary@mail.com"],
#                   ["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#         ["Mary","mary@mail.com"],'
#         ["John","johnnybravo@mail.com"]]



# em_graph = {} containing set in it
# em_to_name = {}

# all acc the gamil start with 1 index (1st mail)

# for i = 0 : ["John","johnsmith@mail.com","john_newyork@mail.com"]
#         em_graph["johnsmith@mail.com"] = ("johnsmith@mail.com","john_newyork@mail.com")
#         em_graph["john_newyork@mail.com"] = ("johnsmith@mail.com")
#         em_to_name["john_newyork@mail.com"] = "John"
#         em_to_name["johnsmith@mail.com"] = "John"

# for i = 1 : ["John","johnsmith@mail.com","john00@mail.com"]
#         em_graph["johnsmith@mail.com"] = ("johnsmith@mail.com","john_newyork@mail.com","john00@mail.com")
#         em_graph["john00@mail.com"] = ("johnsmith@mail.com")
#         em_to_name["john00@mail.com"] = "John"

# for i = 2 : ["Mary","mary@mail.com"]
#         em_graph["mary@mail.com"] = ("mary@mail.com")
#         em_to_name["mary@mail.com"] = "Mary"

# for i = 3 : ["John","johnnybravo@mail.com"]
#         em_graph["johnnybravo@mail.com"] = ("johnnybravo@mail.com")
#         em_to_name["johnnybravo@mail.com"] = "John"
        

# now using normal dfs, connected component in one name and add them in seen 


