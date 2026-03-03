# time: O(n^2). Обход n узлов и сравнение строк длинной n на каждом уровне
# memory: O(n^2). Хранение суффиксов в очереди
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        queue = deque()

        smallest = "{"

        queue.append((root, ""))

        while queue:
            node, suffix = queue.popleft()

            suffix = chr(97 + node.val) + suffix

            if not node.left and not node.right:
                smallest = min(smallest, suffix)

            if node.left:
                queue.append((node.left, suffix))

            if node.right:
                queue.append((node.right, suffix))

        return smallest
