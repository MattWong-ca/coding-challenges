# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if target - nums[j] == nums[i] and i != j:
                    return [i,j]

# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        reverse_x = str(x)[::-1]
        return x_str == reverse_x

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

# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        
        return len(nums)

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

# 69. Sqrt(x) (WORK IN PROGRESS)
class Solution:
    def mySqrt(self, x: int) -> int:
        square_root = 0
        numbers = list(range(1, x + 1))
        
        for i in range(len(numbers)):
            if numbers[i] * numbers[i] >= x:
                square_root = numbers[i]

        return square_root

# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
    
        # Ex: n = 5, dp = [0,0,0,0,0,0]
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # dp = [1,1,0,0,0,0]

        # Important: the number of steps it takes to level n
        # is equal to the sum of n-1 and n-2 steps

        # From dp[2] to dp[5]
        for i in range(2,n+1):
            # dp[2] = 2
            # dp[3] = 2 + 1 = 3
            # dp[4] = 3 + 2 = 5
            # dp[5] = 5 + 3 = 8
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

# 100. Same Tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # They're both null
        if not p and not q:
            return True
        # One tree is null
        if not p or not q:
            return False
        # If root values are different
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# 104. Maximum Depth of Binary Tree
class Solution:
    # Ex: [1,null,2]
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        # l = 0, r = 1
        l, r = self.maxDepth(root.left), self.maxDepth(root.right)

        # Returns 2
        return 1 + max(l, r)

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
        # Keep track of the lowest price and keep
        # comparing it to current profit
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

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

# 168. Excel Sheet Column Title (WORK IN PROGRESS)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            # Adjust for 0-indexing
            columnNumber -= 1

            remainder = columnNumber % 26

            # ord('A') --> gets ASCII of A, which is 65
            # chr() --> gets char given ASCII value
            result.append(chr(remainder + ord('A')))

            # Gets floor value of column_number / 26
            columnNumber //= 26
        
        return ''.join(result[::-1])

# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in range(len(nums)):
            if nums[num] in dict:
                print(nums[num])
                dict[nums[num]] += 1
            else:
                dict[nums[num]] = 1
        
        for value in dict:
            if dict[value] > (len(nums)/2):
                return value

# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            sum = 0
            array = [int(digit) for digit in str(n)]
            for digit in array:
                sum = sum + (digit * digit)
            n = sum
        return True

# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s,t):
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True

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

# 219. Contains Duplicate II (WIP)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            # If we've seen number X and current index subtract X's index
            # is less than k, we return true. Otherwise, we add the 
            # current num + index to index_map. This ensures we're 
            # always storing the most recent occurrence of num when
            # comparing differences.
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i
        
        return False

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = ''.join(sorted(s))
        y = ''.join(sorted(t))
        return x == y

# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        pattern_to_s = {}
        s_to_pattern = {}

        for letter, word in zip(pattern,s.split()):
            if letter in pattern_to_s and pattern_to_s[letter] != word:
                return False
            if word in s_to_pattern and s_to_pattern[word] != letter:
                return False

            pattern_to_s[letter] = word
            s_to_pattern[word] = letter
        
        return True

# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = {}
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1

        ransom_count = {}
        for char in ransomNote:
            if char in ransom_count:
                ransom_count[char] += 1
            else:
                ransom_count[char] = 1

        for char, count in ransom_count.items():
            if magazine_count.get(char, 0) < count:
                return False
    
        return True

# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i = i + 1
            j = j + 1
        return i == len(s)

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

# 506. Relative Ranks
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # turn into tuple
        tuple_array = []
        range_ = range(len(score))
        for i in range_:
            score_tuple = (score[i], i+1)
            tuple_array.append(score_tuple)
        
        sorted_data = sorted(tuple_array, key=lambda x: x[0], reverse=True)
        print(sorted_data)
        return_array = []
        for data in score:
            result = [t for t in sorted_data if t[0] == data][0]
            print(result)
            return_array.append(sorted_data.index(result)+1)
            
        print(return_array)
        # sort by score[i]
        # 10 9 8 4 3
        # 5 4 3 2 1 

        # turn 5 4 3 2 1 values into Gold Silver Bronze 4 5
        final_array = []
        for value in return_array:
            if value == 1:
                final_array.append('Gold Medal')
            elif value == 2:
                final_array.append('Silver Medal')
            elif value == 3:
                final_array.append('Bronze Medal')
            else:
                final_array.append(str(value))
        print(final_array)
        # create new array using original score list for right order
        return final_array

# 997. Find the Town Judge
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Judge trusts nobody --> will never show up as first in trust-pair
        # Judge is trusted by everyone except themself --> n-1 others

        # Initialize lists with size n+1 (to ignore 0-indexing)
        # Index positions correlate with person's label (n)
        trust_counts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        # Ex: in [1,2] --> a = 1, b = 2
        for a, b in trust: 
            # Ex: if a = 1, value at index 1 of trust_counts is incremented
            trust_counts[a] += 1
            trusted_by[b] += 1

        # Go through all possible people
        for i in range(1, n+1):
            # If their trust_count is 0 and they're trusted by n-1 people, they're the judge
            if trust_counts[i] == 0 and trusted_by[i] == n - 1:
                return i

        return -1

# 1684. Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_arr = list(allowed)
        allowed_set = set(allowed_arr)
        count = 0

        for word in words:
            arr = list(word)
            for letter in arr:
                if letter not in allowed_set:
                    break
            else:
                count += 1        
        
        return count

# 1791. Find Center of Star Graph
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Since it's a star graph, the center node will be common in every subarray

        # Turn the first subarray into a set so we can use .intersection()
        first_edge = set(edges[0])
        second_edge = edges[1]

        # Find common values between first and second subarray, turn into list
        common_elements = list(first_edge.intersection(second_edge))
        
        return common_elements[0]

# 1971. Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: 
            return True
        
        # Create defaultdict so each key represents all other nodes it's connected to
        # Ex: 0: [1,2]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            
            # graph[0] = [1,2] --> loops through 1 and 2
            for neighbor_node in graph[i]:
                if neighbor_node not in seen:
                    seen.add(neighbor_node)

                    # dfs(2) --> returns true since2 = destination
                    if dfs(neighbor_node):
                        return True

        return dfs(source)
