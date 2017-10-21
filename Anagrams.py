# Problem: https://leetcode.com/problems/group-anagrams/description/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # try this without sorting
        map = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in map:
                map[ss] = []
            map[ss].append(s)
        return map.values()
