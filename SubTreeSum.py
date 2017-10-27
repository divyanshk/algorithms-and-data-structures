# Problem: https://leetcode.com/problems/most-frequent-subtree-sum/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        dictMap = {}
        
        def findFrequentTreeSumUtil(root):
            if not root:
                return 0

            sum = root.val + findFrequentTreeSumUtil(root.left) \
                            + findFrequentTreeSumUtil(root.right)
                
            if sum not in dictMap:
                dictMap[sum] = 0
            dictMap[sum] += 1
            return sum
        
        findFrequentTreeSumUtil(root)

        maxValue = max(dictMap.values())
        for k, v in dictMap.iteritems():
            if v == maxValue:
                res.append(k)
        
        return res
