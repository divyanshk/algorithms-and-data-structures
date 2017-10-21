# Problem: https://leetcode.com/problems/fraction-to-recurring-decimal/description/
class Solution(object):
    def fractionToDecimal(self, num, denom):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if num%denom == 0:
            # no decimal
            return str(num/denom)
        
        res, i, decimal = [], 0, []
        # pre decimal
        if (num*denom < 0):
            res.append('-')
        res.append(str(abs(num)/abs(denom)))
        res.append('.')
        rem = abs(num)%abs(denom)
        map = {}
        while(rem):
            if rem not in map:
                map[rem] = i
                decimal.append(str((rem*10)/abs(denom)))
                i += 1
            else:
                break
            rem = (rem*10)%abs(denom)
        if rem:
            decimal.insert(map[rem], '(')
            decimal.insert(len(decimal),')')
        res.append(''.join(decimal))
        return ''.join(res)
