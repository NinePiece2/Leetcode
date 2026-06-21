class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0

        for i, h in enumerate(height):
            while stack and h >= height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                
                min_hight = min(h, height[left]) - height[bottom]
                trapped += width * min_hight
            stack.append(i)
        
        return trapped
