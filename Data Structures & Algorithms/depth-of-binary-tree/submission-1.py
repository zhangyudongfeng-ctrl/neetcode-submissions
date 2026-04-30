# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归定义: 返回当前树的高度
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 