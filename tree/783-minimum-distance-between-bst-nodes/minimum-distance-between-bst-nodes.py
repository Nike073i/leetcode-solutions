# time: O(n)
# memory: O(n)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_distance = math.inf
        self.last = None

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            if self.last is not None:
                self.min_distance = min(self.min_distance, abs(node.val - self.last.val))

            self.last = node

            inorder(node.right)

        inorder(root)

        return self.min_distance        
