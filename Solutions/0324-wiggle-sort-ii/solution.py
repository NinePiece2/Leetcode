class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = sorted(nums)
        n = len(temp)
        i, j = (n - 1) >> 1, n - 1
        for k in range(n):
            if k % 2 == 0:
                nums[k] = temp[i]
                i -= 1
            else:
                nums[k] = temp[j]
                j -= 1
