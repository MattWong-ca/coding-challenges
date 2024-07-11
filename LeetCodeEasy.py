# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[j] == nums[i] and i != j:
                    return [i,j]

# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixLetters = ""
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i >= len(min(strs[0], word)) or word[i] != strs[0][i]:
                    return prefixLetters
            prefixLetters = prefixLetters + strs[0][i]

        return prefixLetters

# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif bracket in brackets.values():
                if not stack or brackets[stack.pop()] != bracket:
                    return False
        
        return len(stack) == 0

# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_numbers = set(nums)
        unique_numbers_list = list(unique_numbers)
        unique_numbers_list.sort()
        
        for i in range(len(unique_numbers_list)):
            nums[i] = unique_numbers_list[i]
        
        return len(unique_numbers)

# 35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: 
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

# 58. Length of Last Word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Removes trailing whitespaces
        trimmed_s = s.strip()
        # Splits the words between the spaces into array of strings
        words = trimmed_s.split(" ")
        # Returns length of last word
        return len(words[-1])

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # List of int --> list of char
        char_list = [format(x, 'd') for x in digits]
        # List of char --> string
        digits_string = ''.join(char_list)
        # String --> int
        digits_int = int(digits_string)
        # Add 1 to int
        plus_one = digits_int + 1
        # Int --> string
        plus_one_str = str(plus_one)
        # String --> char array
        plus_one_char_list = list(plus_one_str)
        # List of char --> list of int
        plus_one_int_list = [int(x) for x in plus_one_char_list]
        
        return plus_one_int_list

# 70. Climbing Stairs (WORK IN PROGRESS)
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # return sum of (n-1) + (n-2)
        first = 1
        second = 2

        for i in (3, n-1):
            current = first + second
            first = second
            second = current

        return second

# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])

        for rowNumber in range(1, numRows):
            current_row = [0] * (rowNumber + 1)
            current_row[0] = 1
            current_row[-1] = 1

            for positionIndex in range(1, len(current_row)-1):
                current_row[positionIndex] = triangle[rowNumber-1][positionIndex-1] + triangle[rowNumber-1][positionIndex]

            triangle.append(current_row)
        
        return triangle
    
    # Example rowNumber = 2, positionIndex = 1
    # [0,0,0]
    # [1,0,1]
    # current_row[1] = triangle[1][0] + triangle[1][1]
    # current_row[1] = 1 + 1 = 2
    # [1,2,1]

# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(filter(str.isalnum, s)).lower()
        reversed_s = ''.join(reversed(clean_s))
        return clean_s == reversed_s

# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

# 206. Reverse Linked List 
# Visualization: https://www.youtube.com/watch?v=TSDl7sRxWdU&ab_channel=QuinstonPimenta
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s)
        s_array.sort()
        t_array = list(t)
        t_array.sort()
        return s_array == t_array

# 500. Keyboard Row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one_row_words = []
        first_row = list("qwertyuiop")
        second_row = list("asdfghjkl")
        third_row = list("zxcvbnm")

        for word in words:
            lower_case_word = word.lower()
            for i in range(len(lower_case_word)):
                if lower_case_word[i] in first_row:
                    if i == len(lower_case_word) - 1:
                        one_row_words.append(word)
                else:
                    break

        for word in words:
            lower_case_word = word.lower()
            for i in range(len(lower_case_word)):
                if lower_case_word[i] in second_row:
                    if i == len(lower_case_word) - 1:
                        one_row_words.append(word)
                else:
                    break

        for word in words:
            lower_case_word = word.lower()
            for i in range(len(lower_case_word)):
                if lower_case_word[i] in third_row:
                    if i == len(lower_case_word) - 1:
                        one_row_words.append(word)
                else:
                    break

        return one_row_words
