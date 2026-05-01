# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # 全局统计当前的最长边数

        # 递归定义: 以当前节点为端点的最长边数
        def depth(root):
            if not root: return 0
            left_len = depth(root.left)
            right_len = depth(root.right)
            self.res = max(self.res, left_len + right_len)
            return max(left_len, right_len) + 1 # 每次递归返回当前节点的最长边数
        depth(root)
        return self.res

