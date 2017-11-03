# Problem: https://leetcode.com/problems/target-sum/description/
class Solution(object):
    def findTargetSumWaysUtil(self, nums, S, i, sum, map):
        if i==len(nums) and sum == S:
            return 1
        if i==len(nums):
            return 0
        
        key = str(i)+','+str(sum)
        if key in map:
            return map[key]
        
        digit = nums[i]
        plus = self.findTargetSumWaysUtil(nums, S, i+1, sum - digit, map)
        minus = self.findTargetSumWaysUtil(nums, S, i+1, sum + digit, map)
        map[key] = plus + minus
        return plus + minus
    
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        
        map = {}
        return self.findTargetSumWaysUtil(nums, S, 0, 0, map)
