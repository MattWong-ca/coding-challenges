// 1. Two Sum - LeetCode Easy

function twoSum(nums: number[], target: number): number[] {
    // Edge cases
    // empty nums array?
    // target = 0 ?
    // all +ve numbers ? 
    // if no sum added equal to target, return empty array?
    
    // Solution:
    // nested for loop to add each of the numbers
    // Ex: 2 --> try adding 7, 11, and 15 to it
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if ( i != j && target - nums[j] == nums[i] ) {
                return [i,j];
            }
        }
    }

    return [];
};
