# time: O(n)
# memory: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
        
    def height(self, node):
        if not node:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1

        diff = abs(left_height - right_height)

        return -1 if diff > 1 else max(left_height, right_height) + 1
