"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_table = {}

        def dfs(node):
            if node is None:
                return None
            if node in hash_table:
                return hash_table[node]
            
            clone = Node(node.val)
            hash_table[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
            
