# time: O(n + k log k), где k ≤ 62 — количество уникальных символов. Фактически = O(n)
# memory: O(n + k) → O(n).
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = { }
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        sorted_chars = sorted(freq.keys(), key=lambda c: -freq[c])

        return ''.join(c * freq[c] for c in sorted_chars)
