class Solution:
    def getLucky(self, s: str, k: int) -> int:
        createStr = ''

        for i in s:
            createStr += str(ord(i)- ord('a') + 1)
        
        for i in range(k):
            x = 0
            for j in createStr:
                x += int(j)
            createStr = str(x)

        return int(createStr)
        
