/*
    Problem: https://leetcode.com/problems/combination-sum-ii/description/
*/
class Solution {
    void backtrack(int[] nums, int remaining, int start, List<List<Integer>> list, ArrayList<Integer> tempList) {
        if (remaining == 0)
            list.add(new ArrayList<Integer>(tempList));
        else if (remaining < 0)
            return;
        else {
            for (int i=start; i<nums.length ; ++i) {
                if(i > start && nums[i] == nums[i-1]) continue;
                tempList.add(nums[i]);
                backtrack(nums, remaining-nums[i], i+1, list, tempList);
                tempList.remove(tempList.size()-1);
            }
        }
    }
    
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        backtrack(nums, target, 0, list, new ArrayList<Integer>());
        return list;
    }
}
