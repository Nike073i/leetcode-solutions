# time: O(log(n))
# memory: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lessOrEqualThanTarget = lambda c: c <= target
        letters_count = len(letters)

        l, r = -1, letters_count

        while r - l > 1:
            m = l + (r - l) // 2

            if (lessOrEqualThanTarget(letters[m])):
                l = m
            else:
                r = m

        return letters[0] if r == letters_count else letters[r]
        
