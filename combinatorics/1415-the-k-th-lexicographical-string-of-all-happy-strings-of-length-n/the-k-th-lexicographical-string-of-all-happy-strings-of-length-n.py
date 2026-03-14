# time: O(min(k, 3 × 2^(n-1)))
# memory: O(1 + recursive-stack) ~= O(n)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0   
        result = '' 
        letters = [ 'a', 'b', 'c' ]

        def combo(prefix, current):
            nonlocal count
            nonlocal result

            prefix = prefix + current

            if len(prefix) == n:
                count += 1
                if count == k:
                    result = prefix
                return
                
            for l in letters:
                if l != current:
                    combo(prefix, l)
        
        combo('', '')

        return result
