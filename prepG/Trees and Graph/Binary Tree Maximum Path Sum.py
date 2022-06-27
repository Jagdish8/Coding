# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# there is not necesecity that the path has to pass via the root not the path has to start or end with leaf


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
        

# similar approach as diameter of the binary tree, some modifications