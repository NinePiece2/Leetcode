class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for val in nums:
            trie.insert(val)

        return max(trie.search(val) for val in nums)

class Trie:
    def __init__(self):
        self.children: List[Trie | None] = [None, None]
    
    def insert(self, ins: int):
        node = self
        for i in range(30, -1, -1):
            val = ins >> i & 1
            if node.children[val] is None:
                node.children[val] = Trie()
            node = node.children[val]
    
    def search(self, sear: int):
        node = self
        result = 0
        for i in range(30, -1, -1):
            val = sear >> i & 1
            if node.children[val ^ 1]:
                result |= 1 << i
                node = node.children[val ^ 1]
            else:
                node = node.children[val]
        return result

