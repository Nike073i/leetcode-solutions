# time: O(1)
# memory: O(1)
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def check_position(i):
            return (
                (s1[i] == s2[i] and s1[i + 2] == s2[i + 2]) or 
                (s1[i + 2] == s2[i] and s2[i + 2] == s1[i])
            )
        
        return check_position(0) and check_position(1)
