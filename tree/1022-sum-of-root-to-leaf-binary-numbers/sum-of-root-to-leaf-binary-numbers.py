# time: O(n)
# memory: O(n)
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.get_sum(0, root)

    def get_sum(self, prefix, node):
        if not node:
            return 0

        prefix = (prefix << 1) + node.val
        
        if not node.left and not node.right:
            return prefix
        
        return self.get_sum(prefix, node.left) + self.get_sum(prefix, node.right)
