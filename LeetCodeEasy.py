# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[j] == nums[i] and i != j:
                    return [i,j]

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
