# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if(not root):
            return root
        
        def solve(root):
            if(not root):
                return
            
            root.left, root.right = root.right, root.left
            solve(root.left)
            solve(root.right)
            
        solve(root)
        return root