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
