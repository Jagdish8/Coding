# # Given a binary tree where node values are digits from 1 to 9.
# #  A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node
# #  values in the path is a palindrome.

# # Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        
        # TLE
#         def solve(root,path):
            
#             #def (TLE)
#             if(not root.left and not root.right):
#                 path = path + str(root.val)
#                 if(self.isPal(path)):
#                     self.count += 1
#                 return 
#             if(root.left):
#                 solve(root.left,path+str(root.val))
#             if(root.right):
#                 solve(root.right,path+str(root.val))
            
#             # bfs (TLE)
#             q = deque([[root,""]])
#             while(q):
#                 n = len(q)
#                 for i in range(n):
#                     node,path = q.popleft()
#                     if(not node.left and not node.right):
#                         path = path + str(node.val)
#                         if(self.isPal(path)):
#                             self.count += 1
#                         continue
#                     if(node.left):
#                         q.append([node.left,path + str(node.val)])
#                     if(node.right):
#                         q.append([node.right,path + str(node.val)])
                
        def solve1(root,dic):

            if(root.val not in dic):
                dic[root.val] = 0
            dic[root.val] += 1
            if(not root.left and not root.right):
                if(self.isPal(dic)):
                    self.count += 1
                # return    (should not do this because line 64 won't run then :-) )
            if(root.left):
                solve1(root.left,dic)
            if(root.right):
                solve1(root.right,dic)
            dic[root.val] -= 1
            
        # solve(root,"")
        solve1(root,{})
        return self.count
    
    def isPal(self,h):

        count_odd = 0
        for i in h.values():
            if(i % 2):
                count_odd += 1
            if(count_odd > 1):
                return False

        return True
        
        