# time: O(n^2)
# memory: O(1)
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_dummy = ListNode()

        while current:
            node = current
            head = head.next

            tmp = sorted_dummy
            while tmp.next and tmp.next.val < node.val:
                tmp = tmp.next

            node.next = tmp.next
            tmp.next = node

        return sorted_dummy.next
