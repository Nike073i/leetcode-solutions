# time: O(n)
# memory: O(n)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        
        for num in nums:
            node = TreeNode(num)
            last = None
            
            while stack and stack[-1].val < num:
                last = stack.pop()
            
            if stack:
                stack[-1].right = node
            
            node.left = last
            
            stack.append(node)
        
        return stack[0]
