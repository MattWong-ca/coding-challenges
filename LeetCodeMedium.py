# 3. Longest Substring Without Repeating Characters
class Solution:
    # a) Sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        # { a: 0 }
        char_map = {}
        start = 0
        max_len = 0

        for end in range(len(s)):
            # If we've already seen the char AND it's in the current window,
            # then update start to be 1 unit after
            # the index of the one we've already seen

            # Ex: { a: 0, b: 1, c: 2 }
            # start was 0, now it's 0 + 1 = 1

            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1

            # Add / update the index value in char_map
            # Ex: for end = 3, a goes from 0 --> 3
            char_map[s[end]] = end
            
            max_len = max(max_len, end-start+1)

        return max_len

    # b) Nested for loop
    def lengthOfLongestSubstringBruteForce(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            seen = []
            counter = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.append(s[j])
                    counter += 1
                    if counter > max_len:
                        max_len = counter
        return max_len

# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Go through s and see if the 2 letters beside the current char are equal,
        # or if the current char and the one after are the same. Ex: aba or bb.
        # If yes, keep checking neighbours.
        if len(s) <= 1:
            return s

        longest_palindrome = ''
        
        # Fxn that returns the longest palindrome at specific char. As long as the
        # char is within s, we keep expanding. Ex: if s = 'aba', then at b, the loop
        # will stop at -1 and 2, which is why we return s[0:2]. In other words, the 
        # loop stops at one interval wider than what should be returned.
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left = left - 1
                right = right + 1
            
            return s[left+1:right]

        for i in range(len(s)):
            # Check for longest odd + even palindromes at each char,
            # if longer then update longest_palindrome
            longest_odd = expand_from_center(i,i)
            longest_even = expand_from_center(i,i+1)

            if len(longest_odd) > len(longest_palindrome):
                longest_palindrome = longest_odd
            if len(longest_even) > len(longest_palindrome):
                longest_palindrome = longest_even

        return longest_palindrome

# 11. Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxArea = 0

        while left < right:
            area = min(height[left],height[right]) * (right-left)
            if area > maxArea:
                maxArea = area
            
            if height[left] > height[right]:
                right = right-1
            else:
                left = left+1
        
        return maxArea

# 15. 3Sum (WIP)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            firstNum = nums[i]
            leftPointer = i+1
            rightPointer = len(nums)-1

            while leftPointer < rightPointer:

# 45. Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0
        n = len(nums)
        far, end = 0, 0

        for i in range(n-1):
            # Max jump index
            if i + nums[i] > far:
                far = i + nums[i]

            if i == end:
                end = far
                smallest += 1
        
        return smallest

# 49. Group Anagrams
# a) Using list()
# b) Using defaultdict()
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
    
    from collections import defaultdict
    def groupAnagramsDefaultdict(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        return list(anagrams.values())

# 53. Maximum Subarray (WORK IN PROGRESS) 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        # Read up on Kadane's algo
        # set a current max and max equal to nums[0]
        # Iterate through the array
        # If negative, we set something to zero and restart adding them sums?
        # For every num we go through, if it's positive then we can keep adding, but if negative, 
        # we don't want to add it to array so we keep going
        # ???

# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Go through array backwards
        # If the value at the n-1 index can reach the goal,
        # then that n-1 index should become the goal
        n = len(nums)
        goal = nums[n-1]

        for i in range(n-1,-1,-1):
            step = nums[i]

            if i + step >= goal:
                goal = i

        return goal == 0

# 130. Surrounded Regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # i is rows
        # j is columns
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
                return

            board[i][j] = 'T'
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        # x is columns
        # y is rows
        for x in range(len(board[0])):
            if board[0][x] == 'O':
                dfs(0, x)
            if board[len(board)-1][x] == 'O':
                dfs(len(board) - 1, x)
        for y in range(len(board)):
            if board[y][0] == 'O':
                dfs(y, 0)
            if board[y][len(board[0])-1] == 'O':
                dfs(y, len(board[0])-1)
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'T':
                    board[x][y] = 'O'

# 133. Clone Graph
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Tracks which nodes have been cloned
        hash_map = {}

        def dfs(node):
            # If already cloned, just return it so no duplicates
            if node in hash_map:
                return hash_map[node]
            
            # Clone and add to hash_map
            clone = Node(node.val, [])
            hash_map[node] = clone

            # For each neighbor node in input node, a cloned version is appended to clone node
            for neighbor_node in node.neighbors:
                clone.neighbors.append(dfs(neighbor_node))
            
            return clone
        
        return dfs(node)

# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        reversedWords = []

        words = s.split()
        for word in reversed(words):
            reversedWords.append(word)
        
        return ' '.join(reversedWords)

# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Do 3 rotations: entire nums, 1st part, 2nd part
        n = len(nums)
        k = k % n 

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        nums.reverse()
        reverse(0, k - 1)
        reverse(k, n - 1)

# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Like a virus spreading - once you get a '1', it checks all
        # neighboring cells and turns them into '0' so that we know
        # we have gone through a single island
        m = len(grid)
        n = len(grid[0])
        island_count = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    dfs(x,y)
                    island_count += 1

        return island_count

# 207. Course Schedule 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Create adjacency list to represent courses
        # 1 --> [0]
        # 0 --> [1]
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # 2. Represent each node by states
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        # Returns true if no cyclic path starting at node
        def dfs(node):
            if states[node] == VISITED: return True
            elif states[node] == VISITING: return False

            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED

            return True

        # 3. For each course, check if a cycle is possible,
        # if yes, then return false, else return true
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

# 210. Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        
        # 1 --> [0]
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED: return True
            elif states[node] == VISITING: return False
            states[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

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

# 347. Top K Frequent Elements
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        for i in range(len(nums)):
            nums_count[nums[i]] += 1
        sorted_result = sorted(nums_count.keys(), key=nums_count.get, reverse=True)
        return sorted_result[:k]

# 399. Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # equations = [["a","b"],["b","c"]]
        # values = [2.0,3.0]
        # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

        # Graph of a --> [b,2], which represents a/b = 2
        graph = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1

            # visit tracks which nodes have been visited
            q, visit = deque(), set()
            q.append([src,1])
            visit.add(src)
            while q:
                n,w = q.popleft()
                if n == target:
                    return w
                
                # For each neighbor node of current node, 
                # add it with updated weight
                for nei, weight in graph[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]

# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Ex: { A: 1, B: 1 }
        count = defaultdict(int)
        max_length = 0
        max_frequency = 0
        start = 0

        # When we get to end = 3, count = { A: 2, B: 1 }
        for end in range(len(s)):
            count[s[end]] += 1 # count = { A: 2, B: 2 }
            max_frequency = max(max_frequency, count[s[end]]) # max_frequency = 2
            
            # The window length subtract max_frequency: number of non-same letters in current window
            if (end - start + 1) - max_frequency > k: # (3-0+1) - 2 = 2, 2 > 2 is false
                count[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1) # max_length = 4

        return max_length

# Notes: for example in AABAB, the window length = 5, and max_freq = 3. So we calculate
# window length - max_freq = 5 - 3 = 2, which gives us the number of non-same letters (eg. B)
# in the window. We want to compare how many non A's there are to k. If there's more non A's 
# than k, we won't be able to substitue all of them, hence needing to enter if block and shift
# window's start 1 unit right.

# 433. Minimum Genetic Mutation
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        gene_chars = ['A', 'C', 'G', 'T']

        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            current_gene, mutation_count = queue.popleft()

            for i in range(len(current_gene)):
                for char in gene_chars:
                    if char == current_gene[i]:
                        continue
                    
                    mutated_gene = current_gene[:i] + char + current_gene[i + 1:]

                    if mutated_gene == endGene:
                        return mutation_count + 1
                    
                    if mutated_gene in bank and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutated_gene, mutation_count + 1))
        
        return -1

# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                duplicates.add(num)

        return list(duplicates)

# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Set pointers so binary search range is [ 1 : max(piles) ]
        l, r = 1, max(piles)
        res = r

        # k is from 1 --> max(piles), so we use midpoint value and shift l/r pointers
        # to efficiently iterate through all possible k values
        while l <= r:
            k = (l + r) // 2
            hours = 0

            # For current k value, count total hours
            for pile in piles:
                hours += math.ceil(pile/k)
            
            # If hours is greater than h, k is too small, so we shift left pointer right
            if hours > h:
                l = k + 1

            # If hours is less than or equal to h, it works, 
            # and k can potentially be new res value 
            # Either way, shift right pointer left to see if there's a smaller possible k
            if hours <= h:
                if k < res:
                    res = k
                r = k - 1

        return res

# 1268. Search Suggestions System
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        l = 0
        r = len(products)

        # 1. Sort products lexicographically
        products.sort()

        # 2. Iterate through searchWord, get prefix
        for i in range(1, len(searchWord)+1):
            prefix = searchWord[:i]

            while l < r and not products[l].startswith(prefix):
                l = l + 1
            
            while l < r and not products[r-1].startswith(prefix):
                r = r - 1
        
            # 3. Get min of (strings between l and r, or first 3)
            res.append(products[l : min(l + 3, r)])

        return res

# 1834. Single-Threaded CPU
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Add index to every task item, then sort by enqueueTime
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x: x[0])

        # time --> time we're at, i --> task we're at
        # heap --> CPU, res --> arr of indices we're storing
        time, i = 0, 0
        heap, res = [], []
        
        # Keep iterating until we get an array of indices w/ same length as tasks
        while(len(res) < len(tasks)):
            
            # 1. Add all tasks that have arrived by current time
            # If there's still tasks left + the time is past its enqueueTime, 
            # then add task to heap (CPU), then increment task
            while i < len(tasks) and tasks[i][0] <= time:
                enqueue, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            # 2. If CPU is idle and no available tasks
            # Set time to current task's enqueueTime and continue
            if not heap:
                time = tasks[i][0]
                continue

            # 3. Run best available task
            # Remove best available task by processingTime, then add its index to res
            # Heap contains tuples (processTime, idx) --> pops by smaller processTime, idx if tie 
            # Increment time to be after this task's processingTime
            processTime, idx = heapq.heappop(heap)
            res.append(idx)
            time += processTime

        return res

# 2043. Simple Bank System
class Bank:
    # balance = [10, 100, 20, 50, 30]
    # 1 --> 10
    # 2 --> 100
    # 3 --> 20

    def __init__(self, balance: List[int]):
        self.balance = balance
    
    def isValid(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.isValid(account1) or not self.isValid(account2):
            return False
        if money <= self.balance[account1-1]:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.isValid(account):
            return False
        if money <= self.balance[account-1]:
            self.balance[account-1] -= money
            return True
        return False
