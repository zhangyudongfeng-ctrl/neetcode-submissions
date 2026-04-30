# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归定义: 返回当前树的高度
        # 为什么只能返回左右子节点? 因为递归要求规模不断变小, 如果返回自己, 相当于是无限递归
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 