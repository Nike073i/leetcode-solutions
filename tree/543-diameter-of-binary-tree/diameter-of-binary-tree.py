# time: O(n)
# memory: O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def traverse(node):
            nonlocal maxDiameter

            if node is None:
                return 0

            leftHeight = traverse(node.left)
            rightHeight = traverse(node.right)
            maxDiameter = max(maxDiameter, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1

        traverse(root)
        return maxDiameter
