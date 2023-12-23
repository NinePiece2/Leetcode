class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = [[0,0]]

        for ch in path:
            c = list(coordinates[-1])
            if ch=='N':
                c[0] += 1
            
            elif ch=='S':
                c[0] -= 1
            
            elif ch=='E':
                c[1] += 1
            
            else:
                c[1] -= 1
            
            if c in coordinates:
                return True
            
            coordinates.append(c)
        return False


        
