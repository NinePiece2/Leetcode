class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                right = i
                left = stack[-1] if stack else -1
                width = right - left - 1
                area = width*height
                maxArea = max(maxArea, area)
            stack.append(i)
        return maxArea
