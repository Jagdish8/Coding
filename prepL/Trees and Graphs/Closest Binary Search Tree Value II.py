# Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]
# Example 2:

# Input: root = [1], target = 0.000000, k = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is n.
# 1 <= k <= n <= 104.
# 0 <= Node.val <= 109
# -109 <= target <= 109
 

# Follow up: Assume that the BST is balanced. Could you solve it in less than O(n) runtime (where n = total nodes)?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        
        self.h = []
        heapify(self.h)
        
        def solve(root):
            if(root):
                solve(root.left)
                # print(root.val,abs(target-root.val))
                heappush(self.h, [-abs(target-root.val),root.val])
                if(len(self.h)>k):
                    heappop(self.h)
                # print(self.h)
                solve(root.right)
        solve(root)
        return [j for i,j in self.h]
        
# using heap,
# time : O(n)
# space : O(k)

# using inorder:
# time: O(n)
# space : O(n)        