# time: O(N * M), где N - длина word1, M - длина word2
# memory: O(N)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word1) + 1))

        for i in range(1, len(word2) + 1):
            curr = [i] * (len(word1) + 1)

            for j in range(1, len(curr)):
                curr[j] = min(
                    curr[j - 1] + 1,
                    prev[j] + 1,
                    prev[j - 1] + (0 if word1[j - 1] == word2[i - 1] else 1)
                )

            prev = curr

        return prev[-1]
