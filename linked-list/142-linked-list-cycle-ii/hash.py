# time: O(n)
# memory: O(n)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        tmp = head
        while tmp:
            if tmp in visited:
                return tmp
            visited.add(tmp)
            tmp = tmp.next

        return None
