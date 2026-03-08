# time: O(n)
# memory: O(n)
# note: Список nums состоит из n строк. Строка X точно не будет в этом списке, если она отличается от каждой строки nums хотя бы в одной позиции.
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join([ '1' if nums[i][i] == '0' else '0' for i in range(len(nums)) ])
