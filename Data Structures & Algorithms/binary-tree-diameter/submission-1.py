# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0 # 全局统计当前的最长边数

        # 递归定义: 返回当前节点的高度
        def depth(root):
            if not root: return 0
            left_len = depth(root.left)
            right_len = depth(root.right)
            nonlocal res 
            res = max(res, left_len + right_len)    # 更新最长边数
            return max(left_len, right_len) + 1 # 每次递归返回当前节点的高度
        depth(root)
        return res

