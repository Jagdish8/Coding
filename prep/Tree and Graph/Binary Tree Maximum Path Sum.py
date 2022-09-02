# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = - sys.maxsize
        
        def solve(root):
            
            if(not root):
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            
            self.ans = max(self.ans,root.val,root.val + left, root.val + right, root.val + left + right)
            
            return max(root.val, root.val + left , root.val + right)
        
        solve(root)
        
        return self.ans
        