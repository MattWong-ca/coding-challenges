# 124. Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def dfs(node):
            if not node:
                return 0
        
            # Best downward path from left and right
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # Case "^": path peaks at this node
            current_path = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path)

            # Case "/" or "\": return one arm upward
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum

# 329. Longest Increasing Path in a Matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        mapping = {} # (r,c) --> #

        def dfs(r, c, prevVal):
            # 1. Check if in range or if larger than prevVal
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prevVal:
                return 0

            # 2. Check if already in mapping
            if (r,c) in mapping:
                return mapping[(r,c)]

            # 3. Check all four directions, add to mapping, then return result
            res = -1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))

            mapping[(r,c)] = res
            return res

        # For loop - call dfs at each position
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        # Return max value in mapping
        return max(mapping.values())
