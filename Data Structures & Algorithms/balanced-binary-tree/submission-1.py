# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs(node) 返回：这棵子树的高度 + 这棵子树是否平衡
        def dfs(node: Optional[TreeNode]):
            if not node: return 0, True
            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            height = max(left_height, right_height) + 1
            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            return height, balanced

        if not root: return True 
        _, balanced = dfs(root)
        return balanced
