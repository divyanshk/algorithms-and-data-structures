/*
    Problem: https://leetcode.com/problems/subsets-ii/description/
*/
class Solution {
    void backtrack(int[] nums, int start, List<List<Integer>> list, List<Integer> tempList) {
        list.add(new ArrayList<Integer>(tempList));
        for (int i=start; i < nums.length; ++i) {
            if (i==start || nums[i]!=nums[i-1]) {
                tempList.add(nums[i]);
                backtrack(nums, i+1, list, tempList);
                tempList.remove(tempList.size()-1);   
            }
        }
    }
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        backtrack(nums, 0, list, new ArrayList<Integer>());
        // Set<List<Integer>> set = new LinkedHashSet<List<Integer>>();
        // set.addAll(list); list.clear(); list.addAll(set);
        return list;
    }
}
