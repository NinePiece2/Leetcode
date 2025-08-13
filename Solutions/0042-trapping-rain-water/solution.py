class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1

                height_check = min(height[left], h) - height[bottom]
                water += width * height_check
            stack.append(i)
        
        return water
