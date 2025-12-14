class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result, count, last = 1, 0, 0
        for i, char in enumerate(corridor):
            if char == "S":
                count += 1
                if count > 2 and count % 2:
                    result = result * (i - last) % (10**9 + 7)
                last = i
        return result if count and count % 2 == 0 else 0
