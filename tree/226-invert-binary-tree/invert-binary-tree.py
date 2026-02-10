# time: O(n)
# memory: O(n)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
