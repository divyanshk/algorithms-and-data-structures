/*
   Leetcode problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
*/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s==null || s.isEmpty()) return 0;
        int[] visited = new int[128];
        for (int i=0; i<128; ++i) 
            visited[i] = -1;
        char[] str = s.toCharArray();
        visited[(int)str[0]-0] = 0;
        int max_len = 1, cur_len = 1, start = 0;
        for (int i=1; i<str.length; i++) {
            int index = (int)str[i]-0;
            if (visited[index] == -1 || start > visited[index])
                cur_len++;
            else {
                start = visited[index] + 1;
                cur_len = i - start + 1;
            }
            max_len = (cur_len > max_len)?cur_len:max_len;
            visited[index] = i;
        }
        return max_len;
    }
}
