# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    s = ''
    digitLetterMap = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    def letterCombinationsUtil(self, digits, i, res):
        if i == len(digits):
            res.append(self.s)
            return
        for l in self.digitLetterMap[int(digits[i])]:
            self.s += l
            self.letterCombinationsUtil(digits, i+1, res)
            self.s = self.s[:-1]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        self.letterCombinationsUtil(digits, 0, res)
        return res
