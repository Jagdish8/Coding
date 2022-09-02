# https://leetcode.com/problems/sum-root-to-leaf-numbers/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if(not root):
            return 0
        self.res=[]
        def btr(root,com):
            if(not root.left and not root.right):
                self.res.append(com+str(root.val))
                return
            if(root.left):
                btr(root.left,com+str(root.val))
            if(root.right):
                btr(root.right,com+str(root.val))    
        btr(root,"")
        su=0
        for i in self.res:
            su+=int(i)
        return su