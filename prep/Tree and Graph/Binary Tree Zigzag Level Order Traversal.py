# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        ans = []
        q = [root]
        flag = False
        while(q):
            print(q,flag)
            temp_ans = []
            temp_q = []
            while(q):
                node = q.pop(0)
                temp_ans.append(node.val)
                if(node.left):
                    temp_q.append(node.left)
                if(node.right):
                    temp_q.append(node.right)
            if(flag):
                ans.append(temp_ans[::-1])
                flag = False
            else:
                ans.append(temp_ans)
                flag = True
            q = temp_q
        return ans
            
# simple using queue