class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # This is the promary use case of Rabin-Karp?
        count = Counter()
        result = []
        for i in range(len(s) - 9): # len(s) - 10 + 1
            tmp = s[i:i + 10]
            count[tmp] += 1
            if count[tmp] == 2:
                result.append(tmp)
        
        return result
