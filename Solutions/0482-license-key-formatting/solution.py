class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        result = []
        count = (n - s.count("-")) % k or k

        for i, char in enumerate(s):
            if char == "-":
                continue
            result.append(char.upper())
            count -= 1

            if count == 0:
                count = k
                if i != n - 1:
                    result.append("-")

        return "".join(result).strip("-")
            
