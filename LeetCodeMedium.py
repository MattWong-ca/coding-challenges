# 3. Longest Substring Without Repeating Characters
# TO DO: make solution work for not just the substring that start at index 0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 1
        seen = []
        s_chars = list(s)

        for i in range(len(s_chars)):
            print("I: ", i)
            seen.append(s_chars[i])
            for j in range(len(s_chars)):
                if j > i:
                    print(j)
                    if s_chars[j] not in seen:
                        seen.append(s_chars[j])
                        if len(seen) > maxLen:
                            maxLen = len(seen)
                    else:
                        seen = []

        print(seen)
        print(maxLen)
        return maxLen

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


# 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Ex: [1,2,3,4,5] --> length = 5
        length = len(nums)

        # Create LHS, RHS, and final array with same length as nums
        # Ex: [1,1,1,1,1]
        prefix_products = [1] * length
        suffix_products = [1] * length
        result = [1] * length

        # After the loop we get prefix_products = [1, 1, 2, 6, 24]
        for i in range(1, length):
            # Ex: for i = 1, prefix_products[0] * nums[0] = 1
            # Ex: for i = 2, prefix_products[1] * nums[1] = 2
            # Ex: for i = 3, prefix_products[2] * nums[2] = 6
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]

        # After the loop we get suffix_products = [120, 60, 20, 5, 1]
        for i in range(length-2, -1, -1):
            # Ex: for i = 3, suffix_products[4] * nums[4] = 5
            # Ex: for i = 2, suffix_products[3] * nums[3] = 20
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]

        # Multiply each prefix with suffix and add product to result array
        for i in range(0, length):
            result[i] = prefix_products[i] * suffix_products[i]

        return result
