class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = -inf

        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for h in range(n):
                    nums[h] += matrix[j][h]
                
                temp_sum = 0
                sorted_set = SortedSet([0])
                for val in nums:
                    temp_sum += val
                    l = sorted_set.bisect_left(temp_sum - k)
                    if l != len(sorted_set):
                        result = max(result, temp_sum - sorted_set[l])
                    sorted_set.add(temp_sum)
        
        return result
