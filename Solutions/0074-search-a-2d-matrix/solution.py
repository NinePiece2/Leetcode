class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while right > left:
            mid = (left + right) // 2
            val, remain = divmod(mid, n)
            if matrix[val][remain] >= target:
                right = mid
            else:
                left = mid + 1
        
        return matrix[left // n][left % n] == target
