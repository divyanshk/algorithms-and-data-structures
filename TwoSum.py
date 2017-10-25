# Problem: https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
	# can use the map instead of sorting
        res = []
        first = 0
        last = len(nums)-1
        for k, v in enumerate(nums):
            nums[k] = [k, v]
        nums.sort(key = lambda x: x[1])
        while first < last:
            if nums[first][1] + nums[last][1] == target:
                res.extend([nums[first][0], nums[last][0]])
                return res
            elif nums[first][1] + nums[last][1] > target:
                last -= 1
            else:
                first += 1
        return []
