# time: O(n)
# memory: O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        dummy = ListNode(0, head)
        length = 0
        tail = dummy
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head

        tmp = dummy
        for i in range(length - k):
            tmp = tmp.next
        
        dummy.next = tmp.next
        tail.next = head
        tmp.next = None

        return dummy.next
