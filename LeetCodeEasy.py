# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[j] == nums[i] and i != j:
                    return [i,j]

# 20. Valid Parentheses (WORK IN PROGRESS)
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        sq_brackets = []
        curly_brackets = []
        char_array = list(s)
        for char in char_array:
            if char == '(':
                brackets.append('(')
            elif char == '[':
                sq_brackets.append('[')
            elif char == '{':
                curly_brackets.append('{')
            
            elif char == ')' and not len(brackets) == 0:
                brackets.pop()
            elif char == ']' and not len(sq_brackets) == 0:
                sq_brackets.pop()
            elif char == '}' and not len(curly_brackets) == 0:
                curly_brackets.pop()
        
        return len(brackets) == 0 and len(sq_brackets) == 0 and len(curly_brackets) == 0

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
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in the loop...
        # next = curr.next
        # curr.next = prev
        # prev = curr
        # curr = next

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
