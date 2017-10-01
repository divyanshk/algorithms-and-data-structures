# Problem: https://leetcode.com/problems/restore-ip-addresses/description/
class Solution(object):
    def recurse(self, s, i, n, ip, res):
        if n == 0 and i == len(s):
            print ip
            res.append('.'.join(ip))
        if n > 0:
            for j in xrange(i, len(s)):
                if int(s[i:j+1]) >= 0 and int(s[i:j+1]) <= 255 and not (i != j and s[i] == '0'):
                    ip.append(str(s[i:j+1]))
                    self.recurse(s, j+1, n-1, ip, res)
                    ip.pop()
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        ip = []
        if len(s) < 4 or len(s) > 12:
            return []
        self.recurse(s, 0, 4, ip, res)
        return res
