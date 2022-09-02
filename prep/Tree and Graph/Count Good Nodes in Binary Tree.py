# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 1
        
        if(not root):
            return 0
        
        def solve(root,val,max_value):
            if(not root):
                return
            if(root.val >= val and root.val >= max_value):
                max_value = root.val
                self.ans += 1
            solve(root.left,val,max_value)
            solve(root.right,val,max_value)
            
            
        solve(root.left,root.val,root.val)
        solve(root.right,root.val,root.val)
        return self.ans