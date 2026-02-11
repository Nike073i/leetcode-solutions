# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# memory: O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_tail, even_tail = head, head.next
        even_head = even_tail

        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next
            even_tail.next = even_tail.next.next
            even_tail = even_tail.next

        odd_tail.next = even_head
        return head
