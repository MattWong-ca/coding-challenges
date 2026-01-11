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
