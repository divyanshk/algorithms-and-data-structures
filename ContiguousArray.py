# Problem: https://leetcode.com/problems/contiguous-array/description/
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = 0
        hashMap = {}
        totalCount = [[0]*2 for i in xrange(len(nums))]
        for i, digit in enumerate(nums):
            totalCount[i][digit] = 1 + totalCount[i-1][digit]
            totalCount[i][digit^1] = totalCount[i-1][digit^1]
            diff = totalCount[i][0] - totalCount[i][1]
            if diff not in hashMap:
                hashMap[diff] = []
            if len(hashMap[diff]) == 0:
                hashMap[diff].append(i)
            else:
                hashMap[diff][0] = i if i < hashMap[diff][0] else hashMap[diff][0]
        for i in xrange(len(nums)-1, -1, -1):
            diff = totalCount[i][0] - totalCount[i][1]
            length = (i - hashMap[diff][0]) if diff else i+1
            maximum = length if length > maximum else maximum
        return maximum
