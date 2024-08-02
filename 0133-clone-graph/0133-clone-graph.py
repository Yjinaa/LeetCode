"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}

        if node is None:
            return None

        clone_map[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur_node = queue.popleft()
            for neighbor in cur_node.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_map[cur_node].neighbors.append(clone_map[neighbor])
                    
    
        return clone_map[node]
        