class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        sum_val = sum(item[2] ** 2 for item in squares)
        left, right = 0, max(item[1] + item[2] for item in squares)
        tolerance = 10**-5

        def checker(y1):
            tmp = 0
            for _, y, l in squares:
                if y < y1:
                    tmp += min(y1 - y, l) * l
            return tmp >= sum_val / 2
        
        while right - left > tolerance:
            mid = (left + right) / 2
            if checker(mid):
                right = mid
            else:
                left = mid
                
        return right 
