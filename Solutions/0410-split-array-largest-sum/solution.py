class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def checker(max_val):
            sum_val = inf
            count = 0
            for val in nums:
                sum_val += val
                if sum_val > max_val:
                    sum_val = val
                    count += 1
            return count <= k

        left, right = max(nums), sum(nums)
        # return left + bisect_left(range(left, right + 1), True, key=checker)
        while right > left:
            mid = (left + right) // 2
            if checker(mid): # Can split the array
                right = mid
            else:
                left = mid + 1
        
        return left
