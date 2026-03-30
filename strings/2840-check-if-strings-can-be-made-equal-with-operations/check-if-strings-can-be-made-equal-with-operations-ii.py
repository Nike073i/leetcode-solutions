# time: O(n), где n - длина строки
# memory: O(1)
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        freq = [0] * 52
        ord_a = ord('a')

        for i in range(len(s1)):
            off = (i & 1) * 26
            freq[ord(s1[i]) - ord_a + off] += 1
            freq[ord(s2[i]) - ord_a + off] -= 1

        return all(c == 0 for c in freq)
