# https://leetcode.com/problems/lemonade-change/description/
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = {'5':0, '10':0, '20':0}
        for bill in bills:
            if bill == 5:
                wallet['5'] += 1
            elif bill == 10:
                wallet['10'] += 1
                if not wallet['5'] >= 1:
                    return False
                else:
                    wallet['5'] -= 1
            elif bill == 20:
                wallet['20'] += 1
                if not (wallet['10'] >= 1 and wallet['5'] >= 1):
                    if not (wallet['5'] >= 3):
                        return False
                    else:
                        wallet['5'] -= 3
                else:
                    wallet['10'] -= 1
                    wallet['5'] -= 1
        return True
