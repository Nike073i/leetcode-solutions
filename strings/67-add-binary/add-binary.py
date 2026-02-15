# time: O(max(n, m)), где n - длина a, m - длина n
# memory: O(max(n, m))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a) - 1, len(b) - 1
        carry = 0

        result = []

        while p1 >= 0 or p2 >= 0 or carry > 0:
            f, s = 0, 0

            if p1 >= 0:
                f = ord(a[p1]) - ord('0')
                p1 -= 1
            
            if p2 >= 0:
                s = ord(b[p2]) - ord('0')
                p2 -= 1
            
            acc = f + s + carry
            carry = acc // 2
            result.append(chr(ord('0') + acc % 2))
            
        return "".join(reversed(result))
