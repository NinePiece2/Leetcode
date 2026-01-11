class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        result = 0
        for row in matrix:
            for j, val in enumerate(row):
                if val == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            result = max(result, self.lgstRecArea(heights))
        return result
    
    def lgstRecArea(self, heights : List[int]) -> int:
        n = len(heights)
        stk = []
        left, right = [-1] * n, [n] * n

        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        return max((right[i] - left[i] - 1) * h for i, h in enumerate(heights))

