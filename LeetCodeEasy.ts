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

// 217. Contains Duplicate

// Initial naive solution that compares each value
// with every other value in the array
function containsDuplicate(nums: number[]): boolean {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[j] == nums[i] && i != j) {
                return true;
            }
        }
    }
    return false;
};

// Better solution using a set to compare values
function containsDuplicate(nums: number[]): boolean {
    const seenNumbers = new Set<number>();

    for (const num of nums) {
        if (seenNumbers.has(num)) {
            return true;
        } else {
            seenNumbers.add(num);
        }
    }
    return false;
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
