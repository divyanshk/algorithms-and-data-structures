# Problem: https://leetcode.com/problems/gas-station/description/
# The problem statement isn't clear !
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum, total, start = [0,0,0]
        for i in xrange(len(gas)):
            sum += gas[i] - cost[i]
            if sum < 0:
                total += sum
                sum = 0
                start = i+1
        total += sum
        return -1 if total < 0 else start
