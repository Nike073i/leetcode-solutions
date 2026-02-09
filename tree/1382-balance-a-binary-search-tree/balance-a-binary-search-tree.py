# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n)
# memory: O(n)
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        self.traverse(values, root)

        return self.buildTree(values, 0, len(values) - 1)

    def buildTree(self, values, l, r):
        if l > r:
            return None
        
        m = l + (r - l) // 2
        
        return TreeNode(
            values[m], 
            self.buildTree(values, l, m - 1), 
            self.buildTree(values, m + 1, r)
        )
    
    def traverse(self, values, node):
        if not node:
            return
        self.traverse(values, node.left)
        values.append(node.val)
        self.traverse(values, node.right)
    
