# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        # top-down
        h = {}
        
        def solve(root,parent_robbed):
            
            if(not root):
                return 0
            if((root,parent_robbed) in h):
                    return h[(root,parent_robbed)]
            if(parent_robbed):
                res = solve(root.left,False)+solve(root.right,False)
                h[(root,parent_robbed)] = res
                return res
            else:
                rob = root.val + solve(root.left,True)+solve(root.right,True)
                noRob = solve(root.left,False)+solve(root.right,False)
                res = max(rob,noRob)
                h[(root,parent_robbed)] = res
                return res
            
        return solve(root,False)
                
                
        
        # bottom up
        
#         def solve(root):
#             if(not root):
#                 return [0,0]
#             left = solve(root.left)
#             right = solve(root.right)
            
#             rob = root.val+left[1]+right[1]
#             noRob = max(left) + max(right)
#             return [rob,noRob]
            
#         return max(solve(root))
