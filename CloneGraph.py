# Problem: https://leetcode.com/problems/clone-graph/description/
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visitedMap = {}
    def clone(self, root):
        if not root:
            return None
        if root.label in self.visitedMap:
            return self.visitedMap[root.label]
        node = UndirectedGraphNode(root.label)
        self.visitedMap[root.label] = node
        for neighbor in root.neighbors:
            node.neighbors.append(self.clone(neighbor))
        return node
    def cloneGraph(self, node):
        return self.clone(node)
