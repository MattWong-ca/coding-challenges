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
