class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        #two pointers from front and back
        s1, s2 = sentence1.split(), sentence2.split()

        if (len(s1) > len(s2)):
            s1, s2 = s2, s1

        i, j = 0, 0

        while (i < len(s1) and i < len(s2) and s1[i] == s2[i]):
            i += 1

        while (j < len(s2) and j < len(s1) and  s1[-(j+1)] == s2[-(j+1)]):
            j += 1

        return i + j >= len(s1)
