# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.ans = []
        if(not root):
            return self.ans
        
        def check(root,target,com):
            if(not root):
                return
            if(not root.left and not root.right and root.val == target):
                self.ans.append(com+[root.val])
                return
            check(root.left,target-root.val,com+[root.val])
            check(root.right,target-root.val,com+[root.val])
        
        check(root,targetSum,[])
        return self.ans