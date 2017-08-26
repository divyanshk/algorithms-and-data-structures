/*
    Problem: https://leetcode.com/problems/longest-palindromic-substring/description/
*/
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        char[] str = s.toCharArray();
        // create and initialise a lookup table
        boolean[][] dp = new boolean[n][n];
        for (boolean row[]: dp)
            Arrays.fill(row, false);
        // handle strings of size 1 and 2
        for (int i=0; i<n; ++i) 
            dp[i][i] = true;
        int start=0,end=0;
        for (int i=0; i<n-1; ++i) {
            if (str[i] == str[i+1]) {
                start=i; end=i+1;
                dp[i][i+1] = true;
            }
        }
        // handle the remaining cases
        for (int l=3; l<=n; ++l) {
            for (int j=0; j<n-l+1; ++j) {
                if (str[j] == str[j+l-1] && dp[j+1][j+l-2] == true) {
                    dp[j][j+l-1] = true;
                    start=j; end=j+l-1;
                }
            }
        }
        return s.substring(start, end+1);
    }
}
