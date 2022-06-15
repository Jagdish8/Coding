# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:


# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(not root):
            return True
        self.ans = True
        def solve(l,r):
            if(not self.ans):
                return
            if(not l and not r):
                return
            if(l and not r):
                self.ans = False
                return
            if(r and not l):
                self.ans = False
                return
            if(l.val != r.val):
                self.ans = False
                return
            solve(l.left,r.right)
            solve(l.right,r.left)
        solve(root.left,root.right)
        return self.ans

# simple recursion