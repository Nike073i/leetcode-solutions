# time: (n*m)log(n*m)
# memory: n*m
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        points = []

        for row in wall:
            i = 0
            for brick in row:
                points += [ (i, + 1), (i + brick, -1) ]
                i += brick

        sorted_points = sorted(points)


        acc = len(wall)
        min_bricks = acc
        for point in sorted_points[len(wall):-len(wall)]:
            acc += point[1]
            min_bricks = min(min_bricks, acc)

        return min_bricks
