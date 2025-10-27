class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = last = 0
        for row in bank:
            if (current := row.count("1")) > 0:
                result += current * last
                last = current
        
        return result
