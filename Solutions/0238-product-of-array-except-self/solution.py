class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left = right = 1

        for i, val in enumerate(nums):
            answer[i] = left
            left *= val

        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer
