"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} #avoid duplicates in copy, map old nodes to new nodes

        def dfs(node): #clone a node and its neighbors recursively
            if node in oldToNew: #already made a clone
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors: #dfs() returns copy of neighbor
                copy.neighbors.append(dfs(n)) #connect copy of neighbor
            return copy
        
        return dfs(node) if node else None

            
        