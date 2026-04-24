# time: O(n)
# memory: O(1)
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counter = {
            'L': 0,
            'R': 0,
            '_': 0,
        }

        for c in moves:
            counter[c] += 1

        return abs(counter['L'] - counter['R']) + counter['_']
