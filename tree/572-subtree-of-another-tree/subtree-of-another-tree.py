# time: O(n*m), где n - кол-во элементов в дереве root, m - кол-во элементов в дереве subRoot
# memory: O(n)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a or not b:
                return a is b  
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
        
        def subtree(a, b):
            if not a:
                return False
            return same(a, b) or subtree(a.left, b) or subtree(a.right, b)
        
        return subtree(root, subRoot)
