# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = {}
        self.min_column = sys.maxsize
        self.max_column = -sys.maxsize

        def DFS(node, row, column):
            if node is not None:
                
                if(column not in columnTable):
                    columnTable[column] = []
                columnTable[column].append((row, node.val))
                
                self.min_column = min(self.min_column, column)
                self.max_column = max(self.max_column, column)
                
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)
        print(columnTable)

        ret = []
        for col in range(self.min_column, self.max_column + 1):
            # sort first by 'row', then by 'value', in ascending order
            ret.append([val for row, val in sorted(columnTable[col])])

        return ret

# tricky line 30 is imp, that why we need row/level as well