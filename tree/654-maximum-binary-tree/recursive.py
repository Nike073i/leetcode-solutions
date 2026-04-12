# time: O(n^2)
# memory: O(n)            
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def create_node(start, end):
            if start > end:
                return None

            max_ind = start
            for i in range(start, end + 1):
                if nums[i] > nums[max_ind]:
                    max_ind = i

            return TreeNode(
                nums[max_ind],
                create_node(start, max_ind - 1),
                create_node(max_ind + 1, end)
            )

        return create_node(0, len(nums) - 1)
