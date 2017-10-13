# Problem: https://leetcode.com/problems/generate-parentheses/description/
class Solution(object):
    s = ''
    def generateParenthesisUtil(self, n, openParen, closeParen, res):
        if openParen == 0:
            self.s += ')'*closeParen
            res.append(self.s)
            self.s = self.s[:-closeParen]
            return
        if openParen > 0:
            self.s += '('
            self.generateParenthesisUtil(n, openParen-1, closeParen, res)
            self.s = self.s[:-1]
            if openParen < closeParen:
                self.s += ')'
                self.generateParenthesisUtil(n, openParen, closeParen-1, res)
                self.s = self.s[:-1]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisUtil(n, n, n, res)
        return res
