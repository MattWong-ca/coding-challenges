// 238. Product of Array Except Self

function productExceptSelf(nums: number[]): number[] {
    // how big will the array be?
    // 

    // nested for loop
    // inner loop: if i != j, then product = 1, for every j, we multiply product x j;
    // set new array's position i to product
    let newArray = [];

    for(let i = 0; i < nums.length; i++) {
        let product = 1;

        for(let j = 0; j < nums.length; j++) {
            if( i != j ) {
                product = product * nums[j];
            }
        }

        newArray.push(product);
    }

    return newArray;
};
