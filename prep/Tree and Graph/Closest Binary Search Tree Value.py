# https://leetcode.com/problems/closest-binary-search-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        self.dif = sys.maxsize
        self.ans = -1
        
        def solve(root):
            if(root):
                
                if(abs(root.val - target) < self.dif):
                    self.ans = root.val
                    self.dif = abs(root.val - target)
                
                if(target > root.val):
                    solve(root.right)
                else:
                    solve(root.left)
            
        
        solve(root)
        return self.ans