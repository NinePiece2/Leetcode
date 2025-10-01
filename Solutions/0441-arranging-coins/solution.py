class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while right > left:
            mid = (left + right + 1) // 2

            if (mid + 1) * mid // 2 <= n:
                left = mid
            else:
                right = mid - 1
        return right
