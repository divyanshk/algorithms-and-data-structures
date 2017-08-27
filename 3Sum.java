/*
    Problem: https://leetcode.com/problems/3sum/
*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i=0; i<nums.length-2; ++i) {
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {
                int l=i+1, r=nums.length-1;
                while (l<r) {
                    if (nums[l] + nums[r] == -nums[i]) {
                        res.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[l], nums[r])));
                        while (l < r && nums[l] == nums[l+1]) l++;
                        while (l < r && nums[r] == nums[r-1]) r--;
                        l++;
                    }
                    else if (nums[l] + nums[r] > -nums[i]) {
                        r--;
                    }
                    else {
                        l++;
                    }
                }
            }
        }
        return res;
    }
}
