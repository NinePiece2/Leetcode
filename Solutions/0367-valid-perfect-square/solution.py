class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # left = bisect_left(range(1, num + 1), num, key=lambda x: x * x) + 1
        # return left * left == num

        left = 0
        right = num

        while left <= right:
            mid = (left + right) // 2
            temp = mid * mid
            if num == temp:
                return True
            elif temp < num:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
