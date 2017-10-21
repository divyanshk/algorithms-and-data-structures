# Problem: https://leetcode.com/problems/repeated-dna-sequences/description/
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
	# try rolling hash for better hashing
        result = []
        dictMap = {}
        for i in xrange(10, len(s)+1):
            if s[i-10:i] not in dictMap:
                dictMap[s[i-10:i]] = 1
            elif dictMap[s[i-10:i]] == 1:
                dictMap[s[i-10:i]] += 1
                result.append(s[i-10:i])
            else:
                dictMap[s[i-10:i]] += 1
        return result
