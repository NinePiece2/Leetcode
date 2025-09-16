class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for val in nums:
            stack.append(val)
            while len(stack) > 1:
                x, y = stack[-2:]
                denom = gcd(x, y)
                if denom == 1:
                    break
                stack.pop()
                stack[-1] = (x * y) // denom
        return stack
