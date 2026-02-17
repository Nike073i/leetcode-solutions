# time: O(1)
# memory: O(1)
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        ones = [0] * 60

        for i in range(len(ones)):
            count = 0
            digit = i

            while digit > 0:
                if (digit & 1) == 1:
                    count += 1
                
                digit >>= 1

            ones[i] = count

        result = []

        for h in range(12):
            h_ones = ones[h]
            for m in range(60):
                m_ones = ones[m]

                if h_ones + m_ones == turnedOn:
                    result.append(f"{h}:{m:02d}")

        return result
