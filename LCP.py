# Problem: https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        minimumLength = min(map(lambda s: len(s), strs))
        for i in xrange(minimumLength):
            for j in xrange(1, len(strs)):
                if strs[j][i] == strs[j-1][i]:
                    continue
                else:
                    return strs[j][:i]
        return strs[0][:minimumLength]
