# time: O(N + k)
# memory: O(1 + recursive) ~= O(N)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res:
                return
            
            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node
                return
            
            inorder(node.right)

        inorder(root)
        return self.res.val
