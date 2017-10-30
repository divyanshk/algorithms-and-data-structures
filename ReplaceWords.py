# Problem: https://leetcode.com/problems/replace-words/description/
class Solution(object):
    def replaceWords(self, roots, sentence):
        """
        :type roots: List[str]
        :type sentence: str
        :rtype: str
        """
        hashMap = {}
        words = sentence.split(' ')
        for word in words:
            for root in roots:
                if word.startswith(root):
                    if word not in hashMap:
                        hashMap[word] = []
                    hashMap[word].append(root)
        for key, value in hashMap.iteritems():
            hashMap[key] = sorted(value, key = lambda x: len(x))
        for i in xrange(len(words)):
            if words[i] in hashMap:
                words[i] = hashMap[words[i]][0]
        return ' '.join(words)
