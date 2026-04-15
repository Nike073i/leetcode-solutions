# time: O(n)
# memory: O(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        letters = list(s)

        while left < right:
            if not letters[left].isalpha():
                left += 1
            elif not letters[right].isalpha():
                right -= 1
            else:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
        
        return "".join(letters)
