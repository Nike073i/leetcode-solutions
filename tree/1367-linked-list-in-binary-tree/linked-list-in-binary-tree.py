# time: O(n * m), где N - кол-во узлов в дереве, M - кол-во узлов в списке. От каждого узла дерева проверяем цепочку
# memory: O(1 + recursive_stack) ~= O(h+l), где h - глубина дерева, l - длина списка
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(treenode, listnode):
            if not listnode:
                return True
            if not treenode:
                return False
            if treenode.val != listnode.val:
                return False

            return dfs(treenode.left, listnode.next) or dfs(treenode.right, listnode.next)

        if not root:
            return False
        if dfs(root, head):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
