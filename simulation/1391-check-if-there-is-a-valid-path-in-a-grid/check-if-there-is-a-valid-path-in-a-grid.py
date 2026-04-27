# time: O(n * m)
# memory: O(n * m)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        moves = { 
            ("h", "r"): (0, 1),
            ("h", "l"): (0, -1),
            ("v", "u"): (-1, 0),
            ("v", "d"): (1, 0),
        }

        connections = {
            ("h", "r", 1): ("h", "r"),
            ("h", "r", 3): ("v", "d"),
            ("h", "r", 5): ("v", "u"),

            ("h", "l", 1): ("h", "l"),
            ("h", "l", 4): ("v", "d"),
            ("h", "l", 6): ("v", "u"),

            ("v", "u", 2): ("v", "u"),
            ("v", "u", 3): ("h", "l"),
            ("v", "u", 4): ("h", "r"),

            ("v", "d", 2): ("v", "d"),
            ("v", "d", 5): ("h", "l"),
            ("v", "d", 6): ("h", "r"),
        }

        possible_starts = {
            1: [("h", "r")],          
            2: [("v", "d")],          
            3: [("v", "d")],          
            4: [("h", "r"), ("v", "d")],
            5: [],                    
            6: [("h", "r")],          
        }

        start_type = grid[0][0]
        if start_type not in possible_starts or not possible_starts[start_type]:
            return False

        n, m = len(grid), len(grid[0])

        for start_side, start_dir in possible_starts[start_type]:
            i, j = 0, 0
            curr_side, curr_dir = start_side, start_dir
            visited = set()

            while (i, j) != (n - 1, m - 1):
                if (i, j) in visited:
                    break 
                visited.add((i, j))

                di, dj = moves[(curr_side, curr_dir)]
                ni, nj = i + di, j + dj

                if not (0 <= ni < n and 0 <= nj < m):
                    break

                key = (curr_side, curr_dir, grid[ni][nj])
                if key not in connections:
                    break

                curr_side, curr_dir = connections[key]
                i, j = ni, nj
            else:
                return True

        return False
