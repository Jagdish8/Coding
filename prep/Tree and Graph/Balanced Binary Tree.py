# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def check(root):
            
            if(not self.ans):
                return 0
            
            if(root):
                left = check(root.left)
                right = check(root.right)
            
                if(abs(right-left)>1):
                    self.ans = False
                    return 0
            
                return 1 + max(left,right)
            return 0
        
        check(root)
        return self.ans
        