# Problem: https://leetcode.com/problems/top-k-frequent-words/description/
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dictMap = {}
        for word in words:
            if word not in dictMap:
                dictMap[word] = 1
            else:
                dictMap[word] += 1
                
        return map(lambda (k,v): k, sorted(dictMap.iteritems(), key=lambda (k,v): (-v,k), reverse = True)[-k:][::-1])
