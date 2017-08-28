/*
    Problem: https://leetcode.com/problems/next-permutation/description/
*/
class Solution {
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    private void reverse(int[] nums, int start, int end) {
        int temp;
        while(start<end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
    
    public void nextPermutation(int[] nums) {
        int i=-1;
        // find last index i such that nums[i] < nums[i+1]
        for (int k=0; k<nums.length-1; ++k) {
            if (nums[k] < nums[k+1]) i=k;
        }
        // if no permutation then sort
        if (i==-1) {
            Arrays.sort(nums);
        }
        else {
            // find last index j such that nums[i] > nums[i]
            int j=i+1;
            for (int k=i+1; k<nums.length; ++k) {
                if (nums[k] > nums[i]) j=k; 
            }
            // swap values at i and j
            swap(nums, i, j);
            // reverse nums[i+1] to end
            reverse(nums, i+1, nums.length-1);            
        }
        System.out.println(Arrays.toString(nums));
    }
}
