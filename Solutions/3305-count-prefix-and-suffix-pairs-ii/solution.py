class Trie:
    def __init__(self):
        self.count = 0
        self.children = {}

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        trie = Trie()
        for word in words:
            node = trie
            for cantidate in zip(word, reversed(word)):
                if cantidate not in node.children:
                    node.children[cantidate] = Trie()
                node = node.children[cantidate]
                result += node.count
            node.count += 1
        
        return result
