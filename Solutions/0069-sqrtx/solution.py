class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while right > left:
            mid = (left + right + 1) // 2
            if mid > x // mid:
                right = mid - 1
            else:
                left = mid
        return left
