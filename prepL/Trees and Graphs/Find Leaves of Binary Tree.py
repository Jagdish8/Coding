# Given the root of a binary tree, collect a tree's nodes as if you were doing this:

# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
# Example 2:

# Input: root = [1]
# Output: [[1]]


# https://leetcode.com/problems/find-leaves-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from logging.config import valid_ident


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.ans = {}
        
        def solve(root,height):
            
            if(not root):
                return height
            lh = solve(root.left,height)
            rh = solve(root.right,height)
            
            height = max(lh,rh)
            if(height not in self.ans):
                self.ans[height] = []
            self.ans[height].append(root.val)
            
            return height + 1
            
        solve(root,0)
        
        return self.ans.values()


Logical Thinking
# We define height of a node as its distance (1 based) to the leaves of BT. For example,

#           1
#          / \
#         2   3
#        / \     
#       4   5    
# height(4) = height(5) = height(3) = 1,
# height(2) = 2,
# height(1) = 3.

# the way we used to calculate height
# height is max(left,right)

# in height add the node.val

# then return height + 1

# dry run