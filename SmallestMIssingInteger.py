# Find smallest positive integer that doesn't exist in given array of positive numbers

# Input: array of positive numbers
# Output: smallest positive number in array

def smallest_positive_number(positive_numbers: list[int]) -> int:
    # 1. Sort the array from small --> large
    # 2. Iterate, for every current number, compare if number + 1 === next number
    # 3. If not true, return that number+1
    sorted_arr = sorted(positive_numbers)

    if not sorted_arr or sorted_arr[0] != 1:
        return 1
    
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] == sorted_arr[i+1]:
            continue
        if sorted_arr[i] + 1 != sorted_arr[i+1]:
            return(sorted_arr[i]+1)

    return sorted_arr[-1] + 1

g = smallest_positive_number([7,3,4,5,100,40])
print(g)

# ALTERNATIVE SOLUTION:
# Turn the input array into a set, then iterate through it and return the first value that isn't there
def smallest_positive_number(nums: list[int]) -> int:
    s = {n for n in nums if n > 0}  # unique positives, O(n)
    x = 1
    while x in s:                   # O(1) average per lookup
        x += 1
    return x