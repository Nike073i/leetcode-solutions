# time: O(n)
# memory: O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        counter[s[0]] = 1
        l, r = 0, 0
        len_s = len(s)
        max_length = 1

        while l < len_s:
            main = counter.most_common(1)[0][1]
            window_length = r - l + 1
            other = window_length - main
            
            if other <= k:
                max_length = max(max_length, window_length)

            if r + 1 < len_s and other <= k:
                r += 1
                counter[s[r]] += 1
            else:
                counter[s[l]] -= 1
                l += 1

        return max_length
