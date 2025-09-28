class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        while right > left:
            mid = (left + right) // 2
            if self.checker(matrix, mid, k, n):
                right = mid
            else:
                left = mid + 1
        return left
            
    
    def checker(self, matrix, mid, k, n):
        count = 0
        i, j = n - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count >= k
