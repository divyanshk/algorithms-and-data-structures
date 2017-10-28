# Problem: https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not str:
            return ""
        return ' '.join(filter(lambda x: x != '', s.strip().split(' ')[::-1])).strip()
