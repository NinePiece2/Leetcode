class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            result += 1
            numBottles += 1
            
        return result
