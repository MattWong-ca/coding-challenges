// 11. Container With Most Water

// Initial naive solution, going through nested loop to check every possible area
function maxArea(height: number[]): number {
    let maxArea = 0;
    for(let i = 0; i < height.length; i++) {
        for(let j = i + 1; j < height.length; j++) {
            let area = (j-i)*Math.min(height[i],height[j]);
            if(area > maxArea) {
                maxArea = area;
            }
        }
    }
    return maxArea;
};

// Better faster solution. Pointers left and right, moves towards center
// depending on which pointer is greater. 
function maxArea(height: number[]): number {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;

    while (left < right) {
        let area = (right-left)*Math.min(height[left],height[right]);
            if(area > maxArea) {
                maxArea = area;
            }        
            
        if (height[left] < height[right]) {
            left = left + 1;
        } else {
            right = right - 1
        }
    }
    return maxArea;
};

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

