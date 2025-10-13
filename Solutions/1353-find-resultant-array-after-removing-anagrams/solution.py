class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def check_ana(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return True
            count = Counter(s1)
            for char in s2:
                count[char] -= 1
                if count[char] < 0:
                    return True
            return False

        return [words[0]] + [word2 for word1, word2 in pairwise(words) if check_ana(word1, word2)]

        # return [next(word) for _, word in groupby(words, sorted)]
