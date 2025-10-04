class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while right > left:
            height_cantidate = min(height[right], height[left])
            width = right - left
            max_area = max(max_area, height_cantidate * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
