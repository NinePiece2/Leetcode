class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        result = 0
        for val in nums:
            while stack and stack[-1] > val:
                result += 1
                stack.pop()
            if val and (not stack or stack[-1] != val):
                stack.append(val)
        result += len(stack)
        return result
