//121. Best Time to Buy and Sell Stock - Leetcode Easy

public class Solution {
    public int MaxProfit(int[] prices) {
        int smallestNumber = prices[0];
        int profit = 0;
        
        for ( int i = 1; i < prices.Length; i++ ) {
            if ( prices[i] > smallestNumber ) {
                profit = Math.Max( profit, prices[i] - smallestNumber );
            } else {
                smallestNumber = prices[i];
            }
        }
        
        return profit;
    }
}
