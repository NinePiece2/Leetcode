class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return nlargest(k, nums)[-1]

        nums = [-num for num in nums]
        result = 0
        heapify(nums)
        while k > 0:
            result = -heappop(nums)
            k -= 1
        return result
