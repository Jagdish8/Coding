Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

# https://leetcode.com/problems/count-univalue-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def solve(root):
            if(not root):
                return None
            left = solve(root.left)
            right = solve(root.right)
            if(not left and not right):
                self.ans +=1
                return root
            elif(not left):
                if(right.val == root.val):
                    self.ans += 1
                    return root
                else:
                    root.val = sys.maxsize
                    return root
            elif(not right):
                if(left.val == root.val):
                    self.ans += 1
                    return root
                else:
                    root.val = sys.maxsize
                    return root
            elif(left.val == right.val == root.val):
                self.ans += 1
                return root
            else:
                root.val = sys.maxsize
                return root
        solve(root)
        return self.ans