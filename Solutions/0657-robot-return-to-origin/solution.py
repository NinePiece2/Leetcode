class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for char in moves:
            match char:
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case "L":
                    x += 1
                case "R":
                    x -= 1
        return y == 0 and x == 0
