class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        hash_table1 = {}
        hash_table2 = {}
        for val1, val2 in zip(pattern, words):
            if (val1 in hash_table1 and hash_table1[val1] != val2) or (val2 in hash_table2 and hash_table2[val2] != val1):
                return False
            hash_table1[val1] = val2
            hash_table2[val2] = val1

        return True
