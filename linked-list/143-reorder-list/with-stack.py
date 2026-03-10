# time: O(n)
# memory: O(n)
# note: Можно заменить stack на reverse и будет O(1) по памяти
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        fast, slow = head, head
        stack = []

        while fast and fast.next:
            stack.append(slow)
            fast = fast.next.next
            slow = slow.next

        new_head = None
        if fast:
            next = slow.next
            slow.next = new_head
            new_head = slow
            slow = next
        
        while stack:
            slow_next = slow.next
            node = stack.pop()

            slow.next = new_head
            node.next = slow
            new_head = node

            slow = slow_next
            
        return new_head
