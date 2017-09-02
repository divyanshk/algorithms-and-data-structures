/*
    Problem: https://leetcode.com/problems/subsets/description/]
*/
class Solution {
    void backtrack(int[] nums, int start, List<List<Integer>> list, List<Integer> tempList) {
        list.add(new ArrayList<Integer>(tempList));
        for (int i=start; i < nums.length; ++i) {
            tempList.add(nums[i]);
            backtrack(nums, i+1, list, tempList);
            tempList.remove(tempList.size()-1);
        }
    }
    
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        backtrack(nums, 0, list, new ArrayList<Integer>());
        return list;
    }
}
