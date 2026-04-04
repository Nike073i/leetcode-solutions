# time: O(n)
# memory: O(n)
class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        text_len = len(encodedText)
        cols = text_len // rows
        offset = cols + 1

        letters = []
        for j in range(cols):
            i = 0
            while j + i * offset < text_len:
                letters.append(encodedText[j + i * offset])
                i += 1
        
        result = "".join(letters)
        return result.rstrip()
