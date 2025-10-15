class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = (-1, 0, 1, 0, -1)
        original_colour = image[sr][sc]

        def dfs(i: int, j: int):
            image[i][j] = color
            for val1, val2 in pairwise(directions):
                x, y = i + val1, j + val2
                if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == original_colour:
                    dfs(x, y)
        
        if original_colour != color:
            dfs(sr, sc)
        return image
