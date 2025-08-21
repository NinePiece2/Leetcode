class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n

        while right > left:
            mid = (left + right + 1) // 2
            if (citations[n - mid] >= mid):
                left = mid
            else:
                right = mid - 1
        
        return left
