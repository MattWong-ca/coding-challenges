# 3. Longest Substring Without Repeating Characters
# TO DO: make solution work for not just the substring that start at index 0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        array = set()
        for char in s:
            if char in array:
                break
            else:
                array.add(char)
                length = length + 1
        
        return length

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary would be string --> string[]
        #   "aet" --> ["tea", "eat", "ate"]
        #   "ant" --> ["tan", "nat"]

        my_dict = {}
        # 1. Iterate through the array. For each string, sort it
        for s in strs:
            s_array = list(s)
            s_array.sort()
            x = "".join(s_array)
            # If the sorted string isn't a key in the dictionary, add it and the current string
            # Else the sorted string is already a key in the dictionary, so just append the current string to its value
            # Ex: "eat" --> add "aet" value to dictionary, with "tea" as one of the values
            if x not in my_dict:
                my_dict[x] = [s]
            else:
                my_dict[x].append(s)
        
        return list(my_dict.values())


# 238. Product of Array Except Self - WORK IN PROGRESS
# This solution exceeds time limit, need a better one
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Ex: [1,2,3,4,5] --> length = 5
        length = len(nums)

        # Create LHS, RHS, and final array with same length as nums
        # Ex: [1,1,1,1,1]
        prefix_products = [1] * length
        suffix_products = [1] * length
        result = [1] * length

        for i in range(1, length):
            # Ex: for i = 1, prefix_products[0] * nums[0] = 1
            # Ex: for i = 2, prefix_products[1] * nums[1] = 2
            # Ex: for i = 3, prefix_products[2] * nums[2] = 6
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
            
        # products = []
        # for i in range(len(nums)):
        #     # print("First array: ", nums[i])
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             # print(nums[j])
        #             product = product * nums[j]
        #     products.append(product)

        # return products 
# 1. Use left_product and right_product arrays
# 2. for left side, each time you iterate right, you use i-1 value to get product
#    eg. [1,2,3,4,5,6,7], on i = 3, multiply nums[2] * left[2]
# 3. do something similar for RHS, the return product of LHS and RHS
