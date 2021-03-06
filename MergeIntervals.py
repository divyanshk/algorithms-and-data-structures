# Problem: https://leetcode.com/problems/merge-intervals/description/
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        res = []
        intervals.sort(key = lambda i: i.start)
        for i in xrange(len(intervals)):
            if res and res[-1].end >= intervals[i].start:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
