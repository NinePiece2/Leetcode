class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        last, lines = 0, 1
        for width in map(lambda x: widths[ord(x) - ord('a')], s):
            if last + width <= 100:
                last += width
            else:
                lines += 1
                last = width

        return [lines, last]
