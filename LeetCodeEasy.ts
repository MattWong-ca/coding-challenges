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

// 268. Missing Number (WIP)

function missingNumber(nums: number[]): number {
    // Edge cases
    // Empty array?
    // Infinitely long array?

    // Sort the array
    // for loop to check if nums[i] + 1 and nums[i+1] are equal
    // Nested loop takes time though, is there a faster way?

    nums.sort()

    for(let i = 0; i < nums.length; i++) {
        if(nums.length == 1) {
            return ;
        }

        if(nums[i] + 1 != nums[i+1]) {
            return nums[i] + 1;
        }
    }
};
