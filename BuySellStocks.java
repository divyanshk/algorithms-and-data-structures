/*
    Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
*/
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2)
            return 0;
        int minimumPrice=prices[0], maxProfitYet=0;
        for (int i=1; i<prices.length; ++i) {
            if (prices[i]<minimumPrice) {
                minimumPrice=prices[i];
                continue;
            }
            if (prices[i]-minimumPrice > maxProfitYet)
                maxProfitYet=prices[i]-minimumPrice;
        }
        return maxProfitYet;
    }
}
