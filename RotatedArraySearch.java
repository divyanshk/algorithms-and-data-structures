/*
    Problem,: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
*/
class Solution {
    public int search(int[] nums, int target) {
        int lo = 0, hi = nums.length-1, mid = 0;
        boolean foundAtMid = false;
        if (nums.length < 1)
            return -1;
        while (lo < hi) {
            mid = lo + (hi - lo)/2;
            // if found, return mid
            if (nums[mid] == target) {
                foundAtMid = true;
                break;
            }
            // arr[lo..mid] is sorted
            else if (nums[lo] <= nums[mid]) {
                if (target < nums[mid] && target >= nums[lo])
                    hi = mid-1;
                else
                    lo = mid+1;
            }
            // arr[mid..hi] is sorted
            else {
                if (target > nums[mid] && target <= nums[hi])
                    lo = mid+1;
                else
                    hi = mid-1;
            }
        }
        if (foundAtMid)
            return mid;
        else if (nums[lo] == target)
            return lo;
        else 
            return -1;
    }
}
