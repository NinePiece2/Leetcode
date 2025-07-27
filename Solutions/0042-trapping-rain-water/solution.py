class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total = 0

        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                boundedHeight = min(height[i], height[left]) - height[bottom]
                total += width*boundedHeight
            stack.append(i)
        
        return total
