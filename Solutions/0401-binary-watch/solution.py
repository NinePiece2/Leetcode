class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(2 ** 10):
            hrs, mins = i >> 6, 0b111111 & i
            if hrs < 12 and mins < 60 and i.bit_count() == turnedOn:
                result.append('{:d}:{:02d}'.format(hrs, mins))

        return result
