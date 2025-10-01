class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        cantidate = float('-inf')
        stack = []
        for num in nums[::-1]:
            if num < cantidate:
                return True
            while stack and stack[-1] < num:
                cantidate = stack.pop()
            stack.append(num)
        
        return False
