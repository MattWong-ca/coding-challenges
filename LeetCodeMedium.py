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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in nums:
            print("First array: ", i)
            product = 1
            for j in nums:
                if i != j:
                    print(j)
                    product = product * j
            products.append(product)

        return products 
