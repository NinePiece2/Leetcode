class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)
        while right > left:
            mid = (left + right + 1) // 2
            if sum(min(val, mid) for val in batteries) >= n * mid:
                left = mid
            else:
                right = mid - 1
        return left
