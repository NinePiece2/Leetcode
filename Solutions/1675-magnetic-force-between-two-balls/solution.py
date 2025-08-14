class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def checker(check: int) -> bool:
            prev = -inf
            count = 0
            for curr in position:
                if curr - prev >= check:
                    prev = curr
                    count += 1
            return count < m

        position.sort()
        left, right = 1, position[-1]
        result = bisect_left(range(left, right + 1), True, key=checker)
        return result
