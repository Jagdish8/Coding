# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if(not root):
            return 0
        def solve(root,prev,ans):
            if not root:
                return

            if not prev or prev.val + 1 == root.val:
                ans += 1
            else:
                ans = 1

            self.ans = max(self.ans, ans)
            solve(root.left, root, ans)
            solve(root.right, root, ans)
            
        solve(root,None,0)
        return self.ans