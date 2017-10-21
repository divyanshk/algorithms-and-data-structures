# Problem: https://leetcode.com/problems/4sum/description/
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 4Sum => 3Sum => 2Sum
        # check for duplicates at each level
        
        result = []
        nums.sort()
        i = 0
        while(i < len(nums)):
            target3 = target - nums[i]
            j = i+1
            while (j < len(nums)):
                target2 = target3 - nums[j]
                front = j+1
                back = len(nums)-1
                while (front < back):
                    if target2 > nums[front] + nums[back]:
                        front += 1
                    elif target2 < nums[front] + nums[back]:
                        back -= 1
                    else:
                        result.append([nums[i], nums[j], nums[front], nums[back]])
                        front += 1
                        back -= 1
                    
                        while(front < back and nums[front] == nums[front-1]):
                            front += 1

                        while(back > front and nums[back] == nums[back+1]):
                            back -= 1
                
                while(j+1 < len(nums) and nums[j] == nums[j+1]):
                    j += 1
                j += 1
            
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            i += 1
        return result
