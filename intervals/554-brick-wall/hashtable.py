# time: O(n * m)
# memory: O(w), где w - ширина стены
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        for row in wall:
            i = 0
            for brick in row[:-1]:
                i += brick
                edges[i] += 1

        return len(wall) if len(edges) == 0 else len(wall) - max(edges.values())
