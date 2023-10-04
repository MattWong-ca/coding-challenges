// 121. Best Time to Buy and Sell Stock

// Excedes time limit since it's a nested for loop, but works
function maxProfit(prices: number[]): number {
    let counter = 0;

    for(let i = 0; i < prices.length - 1; i++) {
        for(let j = i + 1; j < prices.length; j++) {
            const profit = prices[j] - prices[i];
            if ( profit > counter ) {
                counter = profit;
            }
        }
    }
    
    return counter;
};
