# time: O(n)
# memory: O(1)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        counts = [ sum([ 1 for c in s if c == 'a' ]), 0 ]
        
        min_removes = len(s)

        for c in s:
            min_removes = min(min_removes, sum(counts))
            if c == 'a':
                counts[0] -= 1
            else:
                counts[1] += 1

        min_removes = min(min_removes, sum(counts))

        return min_removes
            
