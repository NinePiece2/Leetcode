class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        absX_Z = abs(x - z)
        absY_Z = abs(y -z)
        if absX_Z == absY_Z:
            return 0
        elif absX_Z < absY_Z:
            return 1
        else:
            return 2

