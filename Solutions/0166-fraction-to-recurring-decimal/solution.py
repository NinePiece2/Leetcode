class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        neg = (numerator < 0) != (denominator < 0)
        result = []
        if neg:
            result.append("-")

        num, denom = abs(numerator), abs(denominator)
        result.append(str(num // denom))
        num %= denom

        if num == 0:
            return "".join(result)
        result.append(".")

        hash_map = {}
        while num:
            hash_map[num] = len(result)
            num *= 10
            result.append(str(num // denom))
            num %= denom
            if num in hash_map:
                result.insert(hash_map[num], "(")
                result.append(")")
                break
        
        return "".join(result)
