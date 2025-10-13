class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {val: idx for idx, val in enumerate(list2)}
        result = []
        min_val = float('inf')

        for i, word in enumerate(list1):
            if word in hash_map:
                j = hash_map[word]
                if i + j < min_val:
                    min_val = i + j
                    result = [word]
                elif i + j == min_val:
                    result.append(word)
        
        return result
