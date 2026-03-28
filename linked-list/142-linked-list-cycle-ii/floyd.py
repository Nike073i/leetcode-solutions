# time: O(n)
# memory: O(1)
# notes:
# - Расстояние от начала до цикла - x1
# - Расстояние от цикла до места пересечения - х2
# - Расстояние от места пересечения до начала цикла - x3
# - В момент пересечения медленный прошел x1 + x2. 
# - В момент пересечения быстрый прошел x1 + x2 + x3 + x2
# - Быстрый движется в два раза быстрее -> 2 * (x1 + x2) = x1 + x2 + x3 + x2 -> 2 * x1 = x1 + x3 -> x3 = x1
# - Если x1 равен x3, то при равном темпе через x1 шагов они окажутся в точке x2 (в точке пересечения) 
class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        slow = head

        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    return None
