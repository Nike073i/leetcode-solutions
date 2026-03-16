# time: O(n)
# memory: O(n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for k in range(1, rowIndex + 1):
            val = row[-1] * (rowIndex - k + 1) // k
            row.append(val)

        return row
