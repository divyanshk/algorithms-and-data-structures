/*
    Problem: https://leetcode.com/problems/3sum-closest/description/
*/
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0]+nums[1]+nums[2];
        boolean foundSum = false;
        for (int i=0; i<nums.length-2; i++) {
            int lo=i+1, hi=nums.length-1;
            while (lo<hi) {
                int sum = nums[lo] + nums[hi] + nums[i];
                if (sum == target) {
                    closestSum = sum;
                    foundSum = true;
                    break;
                }
                else if (sum < target) lo++;
                else hi--;
                closestSum = Math.abs(target-sum)<Math.abs(target-closestSum)?sum:closestSum;
            }
            if (foundSum) break;
        }
        return closestSum;
    }
}
