# # https://leetcode.com/problems/unique-binary-search-trees-ii/

# https://www.youtube.com/watch?v=qOItdXuTZGo

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:   
        return self.solve(1,n)
    def solve(self,start,end):
        if(start > end):
            return [None]
        ans = []
        for i in range(start, end+1):
            left = self.solve(start,i-1)
            right = self.solve(i+1,end)
            for l in left:
                for r in right:
                    root = TreeNode(i,l,r)
                    ans.append(root)
        return ans


# 2

# (1,2)
# i = 1
# left = (1,0) = [None]
# right = (2,2)

# (2,2)
# i = 2
# left = (2,1) = [None]
# right = (3,2) = [None]
# ans = [2{left = None,right=None ]

# (1,2)
# i = 1
# left = (1,0) = [None]
# right = (2,2) =  [2{left = None,right=None ]
# ans = [1{left = None,right = 2{left = None,right=None}]

# (1,2)
# i = 2
# left = (1,1)
# right = (3,2) = [None]

# (1,1)
# left = [None]
# right = [None]
# ans = [1{left=None.right=None}]

# (1,2)
# i = 2
# left = (1,1) = [1{left=None.right=None}]
# right = (3,2) = [None]
# ans = [1{left = None,right = 2{left = None,right=None},2{left = 1{left=None.right=None}, right = None}]

        